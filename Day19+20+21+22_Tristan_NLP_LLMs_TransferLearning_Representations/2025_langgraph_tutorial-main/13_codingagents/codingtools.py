"""
Coding tools for LangGraph agents.
Based on the Go implementation from how-to-build-a-coding-agent.
"""

import json
import subprocess
from typing import List, Optional, Any
from pathlib import Path
from pydantic import BaseModel, Field
from langchain_core.tools import tool


class ReadFileInput(BaseModel):
    """Input for the read_file tool."""
    path: str = Field(..., description="The relative path of a file in the working directory.")


@tool
def read_file(input: ReadFileInput) -> str:
    """Read the contents of a given relative file path. 
    
    Use this when you want to see what's inside a file. 
    Do not use this with directory names.
    """
    try:
        file_path = Path(input.path)
        if not file_path.exists():
            return f"Error: File {input.path} does not exist"
        
        if file_path.is_dir():
            return f"Error: {input.path} is a directory, not a file"
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return content
    except PermissionError:
        return f"Error: Permission denied reading {input.path}"
    except UnicodeDecodeError:
        return f"Error: File {input.path} is not a text file or has encoding issues"
    except Exception as e:
        return f"Error reading file: {str(e)}"


class ListFilesInput(BaseModel):
    """Input for the list_files tool."""
    path: Optional[str] = Field(
        default=".", 
        description="Optional relative path to list files from. Defaults to current directory if not provided."
    )


@tool
def list_files(input: ListFilesInput) -> str:
    """List files and directories at a given path.
    
    If no path is provided, lists files in the current directory.
    Returns a JSON array of file and directory names.
    """
    try:
        dir_path = Path(input.path or ".")
        
        if not dir_path.exists():
            return f"Error: Directory {input.path} does not exist"
        
        if not dir_path.is_dir():
            return f"Error: {input.path} is not a directory"
        
        files = []
        
        # Walk through directory tree
        for item in sorted(dir_path.rglob("*")):
            # Skip hidden directories like .git, .devenv
            if any(part.startswith('.') for part in item.parts):
                continue
                
            rel_path = item.relative_to(dir_path)
            
            # Skip if it's the same as the directory itself
            if str(rel_path) == ".":
                continue
                
            if item.is_dir():
                files.append(str(rel_path) + "/")
            else:
                files.append(str(rel_path))
        
        # Also list immediate children for better visibility
        immediate_files = []
        for item in sorted(dir_path.iterdir()):
            if item.name.startswith('.'):
                continue
            if item.is_dir():
                immediate_files.append(item.name + "/")
            else:
                immediate_files.append(item.name)
        
        # Return immediate children if directory is large
        if len(files) > 100:
            return json.dumps(immediate_files, indent=2)
        
        return json.dumps(files if files else immediate_files, indent=2)
        
    except PermissionError:
        return f"Error: Permission denied accessing {input.path}"
    except Exception as e:
        return f"Error listing files: {str(e)}"


class BashInput(BaseModel):
    """Input for the bash tool."""
    command: str = Field(..., description="The bash command to execute.")


@tool
def bash(input: BashInput) -> str:
    """Execute a bash command and return its output.
    
    Use this to run shell commands. Returns combined stdout and stderr.
    If the command fails, returns the error message and any output.
    """
    try:
        # Run the command with shell=True to support bash features
        result = subprocess.run(
            input.command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout
        )
        
        # Combine stdout and stderr
        output = result.stdout
        if result.stderr:
            output += "\n" + result.stderr
        
        # If command failed, include that information
        if result.returncode != 0:
            return f"Command failed with exit code {result.returncode}\nOutput: {output.strip()}"
        
        return output.strip() if output else "Command executed successfully (no output)"
        
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 30 seconds"
    except Exception as e:
        return f"Error executing command: {str(e)}"


class CreateFileInput(BaseModel):
    """Input for the create_file tool."""
    path: str = Field(..., description="The path where the file should be created")
    content: str = Field(..., description="The content to write to the new file")


@tool
def create_file(input: CreateFileInput) -> str:
    """Create a new file with the given content.
    
    Creates a new file at the specified path with the provided content.
    If the file already exists, returns an error.
    If necessary directories don't exist, they will be created.
    """
    try:
        file_path = Path(input.path)
        
        # Check if file already exists
        if file_path.exists():
            return f"Error: File {input.path} already exists. Use edit_file to modify existing files."
        
        # Create parent directories if they don't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the content to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(input.content)
        
        return f"Successfully created file: {input.path}"
        
    except PermissionError:
        return f"Error: Permission denied creating {input.path}"
    except Exception as e:
        return f"Error creating file: {str(e)}"


class EditFileInput(BaseModel):
    """Input for the edit_file tool."""
    path: str = Field(..., description="The path to the file")
    old_str: str = Field(
        ..., 
        description="Text to search for - must match exactly and must only have one match exactly"
    )
    new_str: str = Field(..., description="Text to replace old_str with")


@tool
def edit_file(input: EditFileInput) -> str:
    """Make edits to a text file.
    
    Replaces 'old_str' with 'new_str' in the given file. 
    'old_str' and 'new_str' MUST be different from each other.
    
    If the file specified with path doesn't exist and old_str is empty,
    it will create a new file with new_str as content.
    """
    try:
        # Validate inputs
        if input.old_str == input.new_str:
            return "Error: old_str and new_str must be different"
        
        file_path = Path(input.path)
        
        # Handle file creation case
        if not file_path.exists():
            if input.old_str == "":
                # Create new file
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(input.new_str)
                return f"Created new file: {input.path}"
            else:
                return f"Error: File {input.path} does not exist"
        
        # Read existing file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Special case: appending to file
        if input.old_str == "":
            new_content = content + input.new_str
        else:
            # Count occurrences
            count = content.count(input.old_str)
            
            if count == 0:
                return f"Error: old_str not found in file"
            
            if count > 1:
                return f"Error: old_str found {count} times in file, must be unique"
            
            # Replace the string
            new_content = content.replace(input.old_str, input.new_str, 1)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return "File edited successfully"
        
    except PermissionError:
        return f"Error: Permission denied accessing {input.path}"
    except UnicodeDecodeError:
        return f"Error: File {input.path} is not a text file or has encoding issues"
    except Exception as e:
        return f"Error editing file: {str(e)}"


class CodeSearchInput(BaseModel):
    """Input for the code_search tool."""
    pattern: str = Field(..., description="The search pattern or regex to look for")
    path: Optional[str] = Field(
        default=".", 
        description="Optional path to search in (file or directory)"
    )
    file_type: Optional[str] = Field(
        default=None,
        description="Optional file extension to limit search to (e.g., 'py', 'js', 'go')"
    )
    case_sensitive: bool = Field(
        default=False,
        description="Whether the search should be case sensitive"
    )


@tool
def code_search(input: CodeSearchInput) -> str:
    """Search for code patterns using ripgrep (rg) or grep as fallback.
    
    Use this to find code patterns, function definitions, variable usage, 
    or any text in the codebase. You can search by pattern, file type, or directory.
    
    Returns matching lines with file names and line numbers.
    """
    try:
        # Try ripgrep first (it's faster and better)
        try:
            args = ["rg", "--line-number", "--with-filename", "--color=never"]
            
            if not input.case_sensitive:
                args.append("--ignore-case")
            
            if input.file_type:
                args.extend(["--type", input.file_type])
            
            args.append(input.pattern)
            args.append(input.path or ".")
            
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            # ripgrep returns exit code 1 when no matches found
            if result.returncode == 1:
                return "No matches found"
            elif result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, args)
            
            output = result.stdout.strip()
            
            # Limit output length to prevent overwhelming responses
            lines = output.split('\n')
            if len(lines) > 100:
                return '\n'.join(lines[:100]) + f"\n\n... and {len(lines) - 100} more matches"
            
            return output if output else "No matches found"
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to grep if ripgrep is not available
            args = ["grep", "-r", "-n", "--color=never"]
            
            if not input.case_sensitive:
                args.append("-i")
            
            if input.file_type:
                args.extend(["--include", f"*.{input.file_type}"])
            
            # Add pattern and path
            args.append(input.pattern)
            args.append(input.path or ".")
            
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 1:  # grep returns 1 when no matches
                return "No matches found"
            elif result.returncode != 0:
                return f"Error: Search failed with exit code {result.returncode}"
            
            output = result.stdout.strip()
            
            # Limit output length
            lines = output.split('\n')
            if len(lines) > 100:
                return '\n'.join(lines[:100]) + f"\n\n... and {len(lines) - 100} more matches"
            
            return output if output else "No matches found"
            
    except subprocess.TimeoutExpired:
        return "Error: Search timed out after 10 seconds"
    except Exception as e:
        return f"Error during search: {str(e)}"


# Export all tools as a list for easy import
coding_tools: List[Any] = [
    read_file,
    list_files,
    bash,
    create_file,
    edit_file,
    code_search
]


# Also export a dictionary mapping for convenience
coding_tools_by_name = {
    tool.name: tool for tool in coding_tools
}