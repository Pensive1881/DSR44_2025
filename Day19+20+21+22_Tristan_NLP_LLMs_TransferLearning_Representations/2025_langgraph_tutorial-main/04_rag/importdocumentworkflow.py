import asyncio
import os
import glob
from langgraph.graph import START, END, StateGraph
from pydantic import BaseModel, Field
import tqdm
import dotenv
from markitdown import MarkItDown
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.store.base import BaseStore
from logger import create_logger
from store import create_store, create_async_store

# Load the environment variables
dotenv.load_dotenv()

# Create the logger.
logger = create_logger(__name__)

# Define the namespace for the import document workflow.
import_document_namespace = ("documents", "books", "artificial_intelligence")

async def run_document_import():

    # Use glob to find all the files in documents.
    document_files = glob.glob("documents/**/*", recursive=True)
    print(f"Found {len(document_files)} document files.")
    if len(document_files) == 0:
        raise ValueError("No document files found in documents/ directory.")

    # To the import with a store. 
    async with create_async_store() as store: 
        await store.setup()
        for file_path in document_files:
            graph = import_document_graph(checkpointer=None, store=store)
            await graph.ainvoke({
                "file_path": file_path
            })


class ImportDocumentState(BaseModel):
    """State for importing a document."""
    file_path: str = Field(..., description="Path to the document to import.")


def import_document_graph(checkpointer=None, store=None) -> StateGraph:
    """Graph to import a document into the workflow."""
    builder = StateGraph(ImportDocumentState)

    # Add a node that imports a document.
    builder.add_node(import_document_node)

    # Define the edges.
    builder.add_edge(START, "import_document_node")
    builder.add_edge("import_document_node", END)

    graph = builder.compile(checkpointer=checkpointer, store=store)
    return graph


async def import_document_node(state: ImportDocumentState, store: BaseStore, config) -> ImportDocumentState:

    # Check if the file path is provided.
    file_path = state.file_path
    if not os.path.exists(file_path):
        raise ValueError(f"File {file_path} does not exist.")
    
    # Import the document.
    logger.info(f"Importing document from {file_path}...")
    extension = os.path.splitext(file_path)[1].lower()
    
    # Handle text data.
    if extension in [".txt", ".md"]:

        # Load the document.
        with open(file_path, "r") as file:
            content = file.read()


    # Use markitdown to convert other extensions.
    elif extension in [".pptx", ".docx", ".xls", ".xlsx", ".pdf"]:
        logger.info(f"Converting {extension} document to text...")
        md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
        result = md.convert(file_path)
        content = result.text_content

    # File extension could not be handled.
    else:
        raise ValueError(f"Unsupported file type: {extension}. Supported types are .txt and .md.")

        # Split the document into chunks.
    chunk_size = 1000
    chunk_overlap = 100
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=int(chunk_size),
        chunk_overlap=int(chunk_overlap)
    )
    texts = text_splitter.split_text(content)

    # Add the chunks to the store.
    logger.info(f"Storing {len(texts)} chunks to the store...")
    for i, text in enumerate(tqdm.tqdm(texts)):
        key = f"{os.path.basename(file_path)}_{i}"
        await store.aput(
            namespace=import_document_namespace,
            key=key,
            value={
                "text": text
            }
        )

    # Done.
    return {
        "input": "",
    }


if __name__ == "__main__":
    asyncio.run(run_document_import())