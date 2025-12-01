from .green_agent_client import GreenAgentClient

from agents import function_tool


# Define tools for OpenAI Agent API
@function_tool
async def register(name: str) -> str:
    async with GreenAgentClient() as client:
        result = await client.register(name)
        return result


@function_tool
async def retrieve_problem(id: str, name: str) -> str:
    async with GreenAgentClient() as client:
        result = await client.distribute_problem(id, name)
        return result


@function_tool
async def submit_answer(id: str, name: str, solution: str) -> str:
    async with GreenAgentClient() as client:
        result = await client.process_answer(id, name, solution)
        return result
