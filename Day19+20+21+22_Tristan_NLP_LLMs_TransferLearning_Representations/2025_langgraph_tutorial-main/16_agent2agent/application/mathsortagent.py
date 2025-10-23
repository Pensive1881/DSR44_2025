import os
from collections.abc import AsyncIterable
from typing import Any, List
import httpx
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent


# We will save the state of the agent in memory.
memory = MemorySaver()

# ---

class ResponseFormat(BaseModel):
    """Response format for the MathSortAgent."""

    status: str = Field(
        ...,
        description="The status of the response.",
        enumerate=["completed", "error"],
    )

    message: str = Field(
        ...,
        description="The message to the user. Includes the result of the operation or an error message.",
    )

# ---

class MathToolInput(BaseModel):
    """Input for the math tool."""
    operand1: float = Field(..., description="The first operand for the math operation.")
    operand2: float = Field(..., description="The second operand for the math operation.")
    operator: str = Field(..., description="The operator for the math operation", enumerate=["+", "-", "*", "/"])

@tool
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

@tool
def sort_tool(input: SortToolInput) -> List[float]:
    """Sort a list of numbers in ascending or descending order."""
    if input.order == "asc":
        return sorted(input.numbers)
    elif input.order == "desc":
        return sorted(input.numbers, reverse=True)
    else:
        raise ValueError(f"Unknown order: {input.order}")

# ---

class MathSortAgent:
    """MathSortAgent - a specialized assistant for currency convesions."""

    SUPPORTED_CONTENT_TYPES = ["text", "text/plain"]

    def __init__(self):

        # Create the model.
        self.model = init_chat_model(os.environ["LANGCHAIN_CHAT_MODEL_ANTHROPIC"])

        # Set the tools.
        self.tools = [
            math_tool,
            sort_tool,
        ]

        prompt = "You are a specialized assistant doing math and sorting operations."

        # Create the agent.
        self.graph = create_react_agent(
            self.model,
            tools=self.tools,
            checkpointer=memory,
            prompt=prompt,
            #response_format=ResponseFormat,
        )

    async def invoke(self, query, context_id) -> AsyncIterable[dict[str, Any]]:
        messages = {"messages": [("user", query)]}
        config = {"configurable": {"thread_id": context_id}}

        print(f"Streaming response for query: {query}")

        result = self.graph.invoke(messages, config=config)
        content = result["messages"][-1].content
        if "</think>" in content:
            content = content.split("</think>")[-1].strip()
        print(f"Result content: {content}")

        yield {
            "is_task_complete": True,
            "require_user_input": False,
            "content": content
        }
        return
