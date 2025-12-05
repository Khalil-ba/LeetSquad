"""CLI entry point for LeetBench."""

import typer
import asyncio
import dotenv
dotenv.load_dotenv()

from src.launcher import launch_evaluation
from pydantic_settings import BaseSettings

class LeetSettings(BaseSettings):
    role: str = "unspecified"
    host: str = "127.0.0.1"
    agent_port: int = 9000

app = typer.Typer(help="Agentified Leetcode Solver Benchmark - Standardized agent assessment framework")

#@app.command()
#def green():

#@app.command()
#def white():

@app.command()
def run():
    """Start agent based on environment variable ROLE (green/white)"""
    settings = LeetSettings()
    
    if settings.role == "green":
        from src.green_agent.tools.start_server import start_server
        start_server(
            host=settings.host,
            port=settings.agent_port,
            skip_tests=False,
            skip_llm_judge=False,
            limit_problems=10
        )
    elif settings.role == "white":
        from src.white_agent.tools import start_server
        start_server(
            host=settings.host,
            port=settings.agent_port,
            name="LeetCodeSolver",
            max_turns=25,
            trace=False
        )
    else:
        raise ValueError(f"Unknown role: {settings.role}. Set ROLE env variable to 'green' or 'white'")

@app.command()
def launch_remote(green_url: str, white_url: str):
    """Trigger remote agents to start evaluation (agents must already be running)"""
    from launcher import launch_remote_evaluation
    asyncio.run(launch_remote_evaluation(green_url, white_url))

if __name__ == "__main__":
    app()