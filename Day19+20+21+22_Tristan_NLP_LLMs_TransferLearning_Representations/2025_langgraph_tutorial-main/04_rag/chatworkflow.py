import asyncio
import os
import glob
from langgraph.graph import START, END, StateGraph
from typing import Annotated, List
from pydantic import BaseModel, Field
import tqdm
import dotenv
from markitdown import MarkItDown
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage, AnyMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.store.base import BaseStore
from langgraph.graph.message import add_messages
from logger import create_logger
from store import create_store, create_async_store
import colorama

# Load the environment variables
dotenv.load_dotenv()

# Create the logger.
logger = create_logger(__name__)

# Define the namespace for the import document workflow.
import_document_namespace = ("documents", "books", "artificial_intelligence")

async def run_chat():

    # To the import with a store. 
    async with create_async_store() as store: 
        graph = chat_graph(checkpointer=None, store=store)
        result = await graph.ainvoke({
            "messages": [HumanMessage(content="Tell be about the A* algorithm.")],
        })
        print(result["messages"][-1].content)


class ChatState(BaseModel):
    """State for chat."""
    messages: Annotated[List[AnyMessage], add_messages] = Field(..., description="List of messages in the chat.")


def chat_graph(checkpointer=None, store=None) -> StateGraph:
    """Graph to import a document into the workflow."""
    builder = StateGraph(ChatState)

    # Add a node that imports a document.
    builder.add_node(chat_node)

    # Define the edges.
    builder.add_edge(START, "chat_node")
    builder.add_edge("chat_node", END)

    graph = builder.compile(checkpointer=checkpointer, store=store)
    return graph


async def chat_node(state: ChatState, store: BaseStore, config) -> ChatState:

    print(state)

    # Get the last message.
    last_message = state.messages[-1]
    assert isinstance(last_message, HumanMessage)

    # Search the store.
    search_results = await store.asearch(
        ("documents",),
        query=last_message.content
    )

    # Print the search results.
    colors = [colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN]
    for i, search_result in enumerate(search_results):
        color = colors[i % len(colors)]
        print(color + f"Search result {i}: {search_result}" + colorama.Style.RESET_ALL)
    print("-" * 80)

    # Create the model.
    model = init_chat_model(
        os.environ["LANGCHAIN_CHAT_MODEL"]
    )     

    # Create the system message.
    system_message_components = []
    system_message_components += ["You are a helpful assistant. You are an academic expert."]
    system_message_components += ["You have access to the following documents."]
    for search_result in search_results:
        system_message_components += [f"Found document:\n\n```\n{search_result}\n```"]
    system_message_content = "\n".join(system_message_components)
    system_message = SystemMessage(content=system_message_content)

    # Invoke the model.
    logger.info("Invoking the model...")
    response = await model.ainvoke(
        [system_message] + state.messages
    )
    
    # Remove thinking.
    response_content = response.content
    if "</think>" in response_content:
        response_content = response_content.split("</think>")[1]

    # Update the state.
    return {
        "messages": [AIMessage(content=response_content)]
    }


if __name__ == "__main__":
    asyncio.run(run_chat())