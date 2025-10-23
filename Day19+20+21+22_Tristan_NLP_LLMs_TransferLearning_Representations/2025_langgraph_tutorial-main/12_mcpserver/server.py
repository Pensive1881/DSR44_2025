import os
from typing import List
from pydantic import BaseModel, Field
from fastmcp import FastMCP

# Create the MCP server instance.
mcp = FastMCP("A simple MCP Server with Streamable HTTP", version="0.1.0")

class MathToolInput(BaseModel):
    """Input for the math tool."""
    operand1: float = Field(..., description="The first operand for the math operation.")
    operand2: float = Field(..., description="The second operand for the math operation.")
    operator: str = Field(..., description="The operator for the math operation", enumerate=["+", "-", "*", "/"])

@mcp.tool
def math_tool(input: MathToolInput) -> float:
    """Perform a math operation based on the input."""
    if input.operator == "+":
        return input.operand1 + input.operand2
    elif input.operator == "-":
        return input.operand1 - input.operand2
    elif input.operator == "*":
        return input.operand1 * input.operand2
    elif input.operator == "/":
        if input.operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return input.operand1 / input.operand2
    else:
        raise ValueError(f"Unknown operator: {input.operator}")

class SortToolInput(BaseModel):
    """Input for the sort tool."""
    numbers: List[float] = Field(..., description="A list of numbers to sort.")
    order: str = Field(..., description="The order to sort the numbers", enumerate=["asc", "desc"])

@mcp.tool
def sort_tool(input: SortToolInput) -> List[float]:
    """Sort a list of numbers in ascending or descending order."""
    if input.order == "asc":
        return sorted(input.numbers)
    elif input.order == "desc":
        return sorted(input.numbers, reverse=True)
    else:
        raise ValueError(f"Unknown order: {input.order}")
    
if __name__ == "__main__":
    # Use 0.0.0.0 when running in Docker, 127.0.0.1 otherwise
    host = os.environ.get("MCP_HOST", "127.0.0.1")
    port = int(os.environ.get("MCP_PORT", "8666"))
    mcp.run(transport="http", host=host, port=port, path="/mcp")