"""CLI entry point for LeetSquad"""

import logging
import click

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
# Turn down logging from noisy libraries
logging.getLogger("a2a").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.ERROR)


@click.group()
def cli():
    pass


@cli.group()
def launch():
    """Launch A2A web server"""
    pass


@cli.group()
def run():
    """Start agent execution"""
    pass


@cli.group()
def test():
    """Test agents"""
    pass


@launch.command(name="green")
@click.option("--host", default="0.0.0.0", type=str, show_default=True, help="Host to bind to")
@click.option("--port", default=9999, type=int, show_default=True, help="Port to listen on")
@click.option("--skip-tests", default=False, type=bool, show_default=True, help="Whether to skip accuracy tests")
@click.option("--skip-llm-judge", default=False, type=bool, show_default=True, help="Whether to skip LLM judge")
@click.option("--llm-judge-model", default=None, type=str, show_default=True, help="Model for LLM judge")
@click.option("--llm-provider", default=None, type=str, show_default=True, help="LLM provider (use openai or aws)")
@click.option("--limit-problems", default=None, type=int, show_default=True, help="Number of problems to use")
def launch_green(
    host: str,
    port: int,
    skip_tests: bool,
    skip_llm_judge: bool,
    llm_judge_model: str | None,
    llm_provider: str | None,
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
        llm_provider=llm_provider,
        limit_problems=limit_problems,
    )


@launch.command(name="white")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=9998, help="Port to listen on")
@click.option("--name", default="LeetCodeSolver", help="Agent name")
def launch_white(host: str, port: int, name: str):
    """Start the white agent (LeetCode solver agent)"""
    from .white_agent.tools import start_server
    start_server(host, port, name)
    

@run.command(name="green")
def start_white():
    print("Green agent is already running.")


@run.command(name="white")
@click.option("--host", default="localhost", help="Host to bind to")
@click.option("--port", default=9998, help="Port to listen on")
def start_white(host: str, port: int):
    from .white_agent.tools import start_solving
    import asyncio
    asyncio.run(start_solving(host, port))


@test.command(name="green")
@click.option("--host", default="localhost", type=str)
@click.option("--port", default=9999, type=int)
def test_green(host: str, port: str):
    """Run some predefined tests on green agent"""
    from .green_agent.tools import test_green_agent
    import asyncio
    asyncio.run(test_green_agent(host, port))


@test.command(name="white")
def test_white():
    print("White agent does not have a test.")


@cli.command(name="report")
def report_results():
    """Retrieve benchmark results from green agent"""
    from .green_agent.tools import report_results
    import asyncio
    asyncio.run(report_results())


if __name__ == "__main__":
    cli()
