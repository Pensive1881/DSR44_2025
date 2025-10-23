import dotenv
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langfuse.langchain import CallbackHandler
from fastapi import FastAPI
import uvicorn
import nest_asyncio

# Load environment variables from .env file.
dotenv.load_dotenv()

# Initialize the Langfuse handler
langfuse_handler = CallbackHandler()

# Allow nested event loops.
nest_asyncio.apply()

# Create the FastAPI app.
app = FastAPI()

# Create an endpoint to serve the agent.
@app.post("/invoke_agent")
async def invoke_agent(message: str = None):

    # Initialize the chat model.
    model = init_chat_model(
        "ollama:mistral-small3.2:latest"
    )

    # Create the react agent without any tools.
    agent = create_react_agent(
        model=model,
        tools=[],
    )

    # Get the response from the agent.
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message,
                }
            ]
        },
        config={"callbacks": [langfuse_handler]}
    )
    
    # Return the last message's content.
    return response["messages"][-1].content

# Run the FastAPI app.
uvicorn.run(app, host="127.0.0.1", port=8000)