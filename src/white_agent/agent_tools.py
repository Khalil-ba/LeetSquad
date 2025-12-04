from .green_agent_client import GreenAgentClient

from agents import function_tool


# Define tools for OpenAI Agent API
@function_tool
async def register(name: str) -> str:
    """
    Registers this agent with the coordinating green agent that runs the benchmarking test
    """
    async with GreenAgentClient() as client:
        result = await client.register(name)
        return result


@function_tool
async def retrieve_problem(id: str, name: str) -> str:
    """
    Lets the green agent know it is ready for an additional programming challenge.
    """
    async with GreenAgentClient() as client:
        result = await client.distribute_problem(id, name)
        return result


@function_tool
async def submit_answer(id: str, name: str, solution: str) -> str:
    """
    Used to send the generated solution to a problem that was previously retrieved from
    the coordinating green agent for scoring.
    """
    async with GreenAgentClient() as client:
        result = await client.process_answer(id, name, solution)
        return result
