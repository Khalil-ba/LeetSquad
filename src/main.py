"""CLI entry point for LeetSquad"""

import logging
import click

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s"
)


@click.group()
def cli():
    """LeetSquad - Benchmark white agents on LeetCode problems"""
    pass


@cli.group()
def launch():
    """Launch agents (green, white, or both)"""
    pass


@launch.command(name="green")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=9999, help="Port to listen on")
def launch_green(host: str, port: int):
    """Start the green agent server (for multiprocessing)"""
    from .green_agent.start_server import start_server
    start_server(host, port)


@launch.command(name="white")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=9998, help="Port to listen on")
@click.option("--agent-id", default="white_agent_001", help="Agent ID")
@click.option("--agent-name", default="LeetCodeSolver", help="Agent name")
def launch_white(host: str, port: int, agent_id: str, agent_name: str):
    """Start the white agent (LeetCode solver agent)"""
    from .white_agent_consolidated.server import start_server
    start_server(host, port, agent_id, agent_name)


if __name__ == "__main__":
    cli()
