from agents import Agent, Runner
from dotenv import load_dotenv

from ..agent_tools import register, retrieve_problem, submit_answer

# Loads OpenAI API key from .env
load_dotenv()

class CodingSolverAgent:
    def __init__(self, name: str) -> None:
        instructions = """
        You are a participant agent (i.e. white agent) in a coding contest. Your task is to
        retrieve coding problems, solve them, and submit your answer to the evaluation agent
        (i.e. green agent). There are about 2800 problems and you should solve as many as
        possible.

        ## High-Level Workflow
        1. Register yourself with your name
        2. Retrieve a coding problem
        3. Submit your answer
        4. Repeat step 2-3 until there are no more problems left

        ## Important Rules
        For each problem, you will receive a problem description, some starter code (i.e.
        scaffolding, and the evaluation entry point. Here are some things to keep in mind:
        - Make sure you follow the scaffolding, otherwise you will receive 0 points.
        - Your entire solution is treated as Python code. Therefore, do NOT wrap your code
        around ``` or include any plain-text commentary - otherwise you will receive 0 points. 

        ## Green Agent Skills
        You can invoke three skills on green agent:
        - register: register yourself and obtain a participant unique ID
        - retrieve_problem: get your next coding problem to solve
        - submit_answer: submit your answer to the problem

        ## Signal of Completion
        After you complete all problems, you will receive "No more problems available" the
        next time you invoke retrieve_problem. Once you're done, no more further interactions
        are required.
        """
        self.name = name
        self.agent = Agent(
            name=name,
            instructions=instructions,
            model="gpt-5-mini",
            tools=[register, retrieve_problem, submit_answer]
        )

    async def start_solving(self) -> None:
        result = await Runner.run(self.agent, input=f"your white agent name is: {self.name}.")
        print(result.final_output)
