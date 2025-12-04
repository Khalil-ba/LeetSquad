import asyncio
import logging

from agents import Agent, Runner, set_tracing_disabled
from agents.exceptions import MaxTurnsExceeded
from dotenv import load_dotenv
from pydantic import BaseModel

from ..agent_tools import register, retrieve_problem, submit_answer

logger = logging.getLogger(__name__)


class CompletionSignal(BaseModel):
    """Output this only when no more problems are available."""

    message: str


class CodingSolverAgent:
    def __init__(self, name: str, max_turns: int, trace: bool) -> None:
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
        - register: register yourself and obtain a participant unique ID (Note: you should do this only once)
        - retrieve_problem: get your next coding problem to solve
        - submit_answer: submit your answer to the problem

        ## Signal of Completion
        IMPORTANT: You must keep solving problems by calling tools until you receive a message
        containing "No more problems available" from retrieve_problem. Only then should you
        output the CompletionSignal with a summary message. Do NOT output a final response
        until all problems are exhausted - keep calling retrieve_problem and submit_answer.
        """
        load_dotenv()  # Loads OpenAI API key from .env

        self._start_lock = asyncio.Lock()
        self.name = name
        self.max_turns = max_turns
        self.agent = Agent(
            name=name,
            instructions=instructions,
            model="gpt-5-mini",
            tools=[register, retrieve_problem, submit_answer],
            output_type=CompletionSignal,
        )
        if not trace:
            set_tracing_disabled(True)

    async def start_solving(self) -> None:
        if self._start_lock.locked():
            logger.info("start_solving is already running; ignoring this call.")
            return

        async with self._start_lock:
            try:
                result = await Runner.run(
                    self.agent,
                    input=f"your white agent name is: {self.name}.",
                    max_turns=self.max_turns,
                )
                logger.info(
                    "White agent execution completed. Final output: %s",
                    result.final_output,
                )
            except MaxTurnsExceeded as ex:
                logger.info("White agent execution terminated early. Error: %s", ex)
