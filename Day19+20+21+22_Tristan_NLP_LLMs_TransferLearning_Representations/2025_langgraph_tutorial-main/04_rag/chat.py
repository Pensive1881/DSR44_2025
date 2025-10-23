import os
import dotenv
import gradio as gr
import glob
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langmem import create_search_memory_tool
from store import create_async_store
from chatworkflow import chat_graph

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file
dotenv.load_dotenv()

async def query_handler(messages, query):
    """Handle the query in the Gradio interface"""

    # To the import with a store. 
    async with create_async_store() as store: 

        # Add the user query to the messages.
        messages.append({"role": "user", "content": query})
        yield messages, ""

        # Convert the messages to LangChain.
        langchain_messages = []
        for message in messages:
            if message["role"] == "user":
                langchain_messages.append(HumanMessage(content=message["content"]))
            elif message["role"] == "assistant":
                langchain_messages.append(AIMessage(content=message["content"]))
            else:
                raise ValueError(f"Unknown message role: {message['role']}")

        # Invoke the workflow. 
        graph = chat_graph(checkpointer=None, store=store)
        result = await graph.ainvoke({
            "messages": langchain_messages,
        })
        last_message = result["messages"][-1]
        assert isinstance(last_message, AIMessage)
        messages.append({"role": "assistant", "content": last_message.content})

        # Done.
        yield messages, ""

    return

# Create the Gradio interface
with gr.Blocks(title="LLM Tool Assistant") as demo:
    gr.Markdown("# LLM Tool Assistant")
    gr.Markdown("Ask a question and the assistant will use available tools to help answer it.")
    
    with gr.Column():   
        # dropdown for selecting tools
        chatbot = gr.Chatbot(type="messages")
        query_input = gr.Textbox(
            label="Your Question",
            placeholder="Enter your question here...",
            lines=3
        )
        submit_btn = gr.Button("Submit")
        
    # Handle the query submission for the button.
    submit_btn.click(
        fn=query_handler,
        inputs=[
            chatbot,
            query_input
        ],
        outputs=[chatbot, query_input]
    )

    # Handle the query submission for the Enter key.
    query_input.submit(
        fn=query_handler,
        inputs=[
            chatbot,
            query_input
        ],
        outputs=[chatbot, query_input]
    )


if __name__ == "__main__":
    # Check if environment variables are set
    try:
        print("Starting Gradio app...")
        demo.launch()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set the required environment variables in a .env file.")