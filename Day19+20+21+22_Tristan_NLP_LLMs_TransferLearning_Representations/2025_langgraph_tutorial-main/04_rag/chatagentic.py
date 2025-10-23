import os
from pyexpat.errors import messages
import time
import dotenv
import gradio as gr
import glob
import json
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

# Define the namespace for the documents.
import_document_namespace = ("documents", "books", "artificial_intelligence")

async def query_handler(messages, query):
    """Handle the query in the Gradio interface"""

    # To the import with a store. 
    async with create_async_store() as store: 

        # Create the tools.
        tools = [
            create_search_memory_tool(namespace=import_document_namespace, store=store),
        ]

        # Create the ReAct agent.
        model = init_chat_model(
            os.environ["LANGCHAIN_CHAT_MODEL"]
        )   
        prompt = "You are a helpful assistant. Your goal is to answer the given question about the book by querying the vector database for relevant content. Do not hesitate to do multiple queries if needed to get a comprehensive answer. If you are looking for some information do not hesitate to do multiple searches with different queries. Do at least two searches."
        agent = create_react_agent(
            model,
            tools=tools,
            prompt=prompt
        )

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

        # Invoke the agent. 
        async for chunk in agent.astream(
            {"messages": langchain_messages},
            stream_mode="updates"
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:

                    # Handle an AI Message.
                    if isinstance(message, AIMessage):
                        assistant_message = message.content
                        if "</think>" in assistant_message:
                            assistant_message = assistant_message.split("</think>")[-1].strip()
                            assistant_message = assistant_message.replace("<think>\n", "**").replace("</think>", "**\n")
                        for tool_call in message.tool_calls:
                            tool_call_name = tool_call["name"]
                            tool_call_args = tool_call["args"]
                            assistant_message += f"\n\n🔧 Tool called: `{tool_call_name}` with args: `{tool_call_args}`"
                        if assistant_message:
                            messages.append({"role": "assistant", "content": assistant_message})
                            yield list(messages), ""
                    
                    # Unexpected message type.
                    else:
                        raise ValueError(f"Unexpected message type: {message}")

            elif "tools" in chunk and "messages" in chunk["tools"]:
                for tool_message in chunk["tools"]["messages"]:
                    assert isinstance(tool_message, ToolMessage)
                    tool_message_content = tool_message.content
                    tool_message_content = json.dumps(json.loads(tool_message_content), indent=2)
                    assistant_message = f"🔧 Tool Response:\n\n```\n{tool_message_content}\n```"
                    messages.append({"role": "assistant", "content": assistant_message})
                    yield list(messages), ""

            else:
                raise ValueError(f"Unexpected chunk: {chunk}")

        print("DONE")
        return


# Create the Gradio interface
with gr.Blocks(title="LLM Tool Assistant") as demo:
    gr.Markdown("# LLM Tool Assistant")
    gr.Markdown("Ask a question and the assistant will use available tools to help answer it.")
    
    with gr.Column():   
        # dropdown for selecting tools
        chatbot = gr.Chatbot(type="messages")
        query_input = gr.Textbox(
            value="Wer ist der Chef?",
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
        outputs=[chatbot, query_input],
    )

    # Handle the query submission for the Enter key.
    query_input.submit(
        fn=query_handler,
        inputs=[
            chatbot,
            query_input
        ],
        outputs=[chatbot, query_input],
    )


if __name__ == "__main__":
    # Check if environment variables are set
    try:
        print("Starting Gradio app...")
        demo.launch()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set the required environment variables in a .env file.")