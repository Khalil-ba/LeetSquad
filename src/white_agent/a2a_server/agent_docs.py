import json
import os

from a2a.types import AgentCapabilities, AgentCard, AgentSkill


def get_agent_url() -> str:
    """Get the agent URL from environment or use localhost fallback."""
    cloudrun_host = os.getenv("CLOUDRUN_HOST")
    if cloudrun_host:
        https_enabled = os.getenv("HTTPS_ENABLED", "true").lower() == "true"
        protocol = "https" if https_enabled else "http"
        return f"{protocol}://{cloudrun_host}/"
    return "http://localhost:9998/"


start_solving_skill = AgentSkill(
    id="start_solving",
    name="Start Solving",
    description="""Start the solving process. The white agent will first register itself
    with the green agent, then repeatedly retrieve problem and submit answer until there
    is no more problems left.
    """,
    tags=["white agent", "solve", "automatic"],
    examples=[
        json.dumps(
            {
                "skill": "start_solving",
                "name": "<white agent name>",
            }
        )
    ],
)

# Public agent card
agent_card = AgentCard(
    name="Coding Solver Agent",
    description="Solver agent that solves coding problems distributed by the green agent",
    url=get_agent_url(),
    version="1.0.0",
    default_input_modes=["text"],
    default_output_modes=["text"],
    capabilities=AgentCapabilities(streaming=False),
    skills=[
        start_solving_skill,
    ],
    supports_authenticated_extended_card=False,
)
