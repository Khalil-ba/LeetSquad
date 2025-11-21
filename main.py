"""CLI entry point for LeetBench."""

import typer
import asyncio

from src.launcher import launch_evaluation

app = typer.Typer(help="Agentified Leetcode Solver Benchmark - Standardized agent assessment framework")

#@app.command()
#def green():

#@app.command()
#def white():

@app.command()
def run():
    settings = TaubenchSettings()
    if settings.role == "green":
        start_green_agent(host=settings.host, port=settings.agent_port)
    elif settings.role == "white":
        start_white_agent(host=settings.host, port=settings.agent_port)
    else:
        raise ValueError(f"Unknown role: {settings.role}")
    return

@app.command()
def launch():
    """Launch the complete evaluation workflow."""
    asyncio.run(launch_evaluation())

if __name__ == "__main__":
    app()