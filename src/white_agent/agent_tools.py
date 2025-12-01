from .green_agent_client import GreenAgentClient

from agents import function_tool


# Define tools for OpenAI Agent API
@function_tool
async def register(name: str) -> str:
    print(f"White agent invoking skill 'register' with name {name}")
    async with GreenAgentClient() as client:
        result = await client.register(name)
        return result

@function_tool
async def retrieve_problem(id: str, name: str) -> str:
    print(f"White agent invoking skill 'retrieve_problem' with id {id} & name {name}")
    async with GreenAgentClient() as client:
        result = await client.distribute_problem(id, name)
        return result

@function_tool
async def submit_answer(id: str, name: str, solution: str) -> str:
    print(f"White agent invoking skill 'submit_answer' with id {id} & name {name}. Solution:\n{solution}")
    async with GreenAgentClient() as client:
        result = await client.process_answer(id, name, solution)
        return result
    