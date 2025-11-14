"""CLI entry point for LeetSquad"""

import logging
import click

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s"
)
# Turn down logging from noisy libraries
logging.getLogger("a2a").setLevel(logging.ERROR)


@click.group()
def cli():
    pass


@cli.group()
def launch():
    """Launch agents (green, white, or both)"""
    pass


@launch.command(name="green")
@click.option("--host", default="0.0.0.0", type=str, show_default=True, help="Host to bind to")
@click.option("--port", default=9999, type=int, show_default=True, help="Port to listen on")
@click.option("--skip-tests", default=False, type=bool, show_default=True, help="Whether to skip accuracy tests")
@click.option("--skip-llm-judge", default=False, type=bool, show_default=True, help="Whether to skip LLM judge")
@click.option("--llm-judge-model", default=None, type=str, show_default=True, help="Model for LLM judge")
@click.option("--limit-problems", default=None, type=int, show_default=True, help="Number of problems to use")
def launch_green(
    host: str,
    port: int,
    skip_tests: bool,
    skip_llm_judge: bool,
    llm_judge_model: str | None,
    limit_problems: int | None,
):
    """Start the green agent (LeetCode eval agent)"""
    from .green_agent.tools.start_server import start_server
    start_server(
        host,
        port,
        skip_tests=skip_tests,
        skip_llm_judge=skip_llm_judge,
        llm_judge_model=llm_judge_model,
        limit_problems=limit_problems,
    )

@launch.command(name="white")
@click.option("--host", default="localhost", help="Host to bind to")
@click.option("--port", default=9999, help="Port to listen on")
@click.option("--agent-id", default="white_agent_001", help="Agent ID")
@click.option("--agent-name", default="LeetCodeSolver", help="Agent name")
def launch_white(host: str, port: int, agent_id: str, agent_name: str):
    """Start the white agent (LeetCode solver agent)"""
    from .white_agent.server import start_server
    start_server(host, port, agent_id, agent_name)


@cli.group()
def test():
    """Test agents (green or white)"""
    pass


@test.command(name="green")
@click.option("--host", default="localhost", type=str)
@click.option("--port", default=9999, type=int)
def test_green(host: str, port: str):
    """Run some predefined tests on green agent"""
    from .green_agent.tools import test_green_agent
    import asyncio
    asyncio.run(test_green_agent(host, port))


@test.command(name="white")
@click.option("--host", default="localhost", type=str)
@click.option("--port", default=9999, type=int)
def test_white(host: str, port: str):
    """Run some predefined tests on white agent"""
    pass # to be implemented


@cli.command(name="report")
def report_results():
    """Retrieve benchmark results from green agent"""
    from .green_agent.tools import report_results
    import asyncio
    asyncio.run(report_results())


if __name__ == "__main__":
    cli()
