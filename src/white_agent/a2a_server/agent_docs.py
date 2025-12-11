import json
import os

from a2a.types import AgentCapabilities, AgentCard, AgentSkill


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
    url=os.getenv("AGENT_URL"),  # AGENT_URL is set by AgentBeats controller
    version="1.0.0",
    default_input_modes=["text"],
    default_output_modes=["text"],
    capabilities=AgentCapabilities(streaming=False),
    skills=[
        start_solving_skill,
    ],
    supports_authenticated_extended_card=False,
)
