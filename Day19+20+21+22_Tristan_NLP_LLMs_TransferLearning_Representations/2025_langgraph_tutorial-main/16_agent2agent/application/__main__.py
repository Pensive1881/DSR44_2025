import os
import logging
import sys
import click
import httpx
import uvicorn
import dotenv
from a2a.server.apps import A2AStarletteApplication
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryPushNotifier, InMemoryTaskStore

from application.mathsortagent import MathSortAgent
from application.mathsortagentexecutor import MathSortAgentExecutor


# Load environment variables from .env file.
dotenv.load_dotenv()

# Create a logger.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option("--host", "host", default="localhost")
@click.option("--port", "port", default=10000)
def main(host, port):

    try:

        # Define the agent capabilities.
        capabilities = AgentCapabilities(streaming=True, pushNotifications=True)

        # Define the math skill for the agent.
        math_skill = AgentSkill(
            id="do_math_operations",
            name="Math Operations",
            description="Performs basic math operations like addition, subtraction, multiplication, and division.",
            tags=["math", "operations"],
            examples=["What is 5 + 3?", "Calculate 10 * 2."],
        )

        # Define the sort skill for the agent.
        sort_skill = AgentSkill(
            id="sort_numbers",
            name="Sort Numbers",
            description="Sorts a list of numbers in ascending or descending order.",
            tags=["sort", "numbers"],
            examples=["Sort these numbers: 5, 3, 8, 1.", "Order these numbers: 10, 2, 5 in descending order."],
        )

        # Create the agent card.
        agent_card = AgentCard(
            name="MathSortAgent",
            description="A specialized agent for performing math operations and sorting numbers.",
            author="Tristan Behrens",
            url=f"http://{host}:{port}/",
            version="1.0.0",
            defaultInputModes=MathSortAgent.SUPPORTED_CONTENT_TYPES,
            defaultOutputModes=MathSortAgent.SUPPORTED_CONTENT_TYPES,
            capabilities=capabilities,
            skills=[math_skill, sort_skill],
        )

        # --8<-- [start:DefaultRequestHandler]
        httpx_client = httpx.AsyncClient()
        request_handler = DefaultRequestHandler(
            agent_executor=MathSortAgentExecutor(),
            task_store=InMemoryTaskStore(),
            push_notifier=InMemoryPushNotifier(httpx_client),
        )
        server = A2AStarletteApplication(
            agent_card=agent_card, http_handler=request_handler
        )

        uvicorn.run(server.build(), host=host, port=port)
        # --8<-- [end:DefaultRequestHandler]

    except Exception as e:
        logger.error(f"An error occurred during server startup: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
