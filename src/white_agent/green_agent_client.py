import json
import logging
import os
from typing import Any, Dict
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest

logger = logging.getLogger(__name__)


def get_green_agent_url() -> str:
    """Get the green agent URL from environment or use localhost fallback."""
    green_agent_host = os.getenv("GREEN_AGENT_HOST")
    if green_agent_host:
        https_enabled = os.getenv("HTTPS_ENABLED", "true").lower() == "true"
        protocol = "https" if https_enabled else "http"
        return f"{protocol}://{green_agent_host}"
    return "http://localhost:9999"


class GreenAgentClient:
    """
    Client for invoking the green agent's skills.

    Sample Usage:

    async with GreenAgentClient() as client:
        result = await client.register(name)
    """

    def __init__(self, base_url: str | None = None):
        self.base_url = base_url or get_green_agent_url()
        self._client: A2AClient | None = None
        self._httpx_client: httpx.AsyncClient | None = None

    async def __aenter__(self):
        """Async context manager entry"""
        self._httpx_client = httpx.AsyncClient()

        # Fetch agent card and initialize client
        resolver = A2ACardResolver(
            httpx_client=self._httpx_client, base_url=self.base_url
        )

        agent_card = await resolver.get_agent_card()

        self._client = A2AClient(httpx_client=self._httpx_client, agent_card=agent_card)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self._httpx_client:
            await self._httpx_client.aclose()

    async def _call_skill(self, skill: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generic method to call a skill on the green agent"""
        if not self._client:
            raise RuntimeError("Client not initialized. Use async context manager.")

        # Prepare payload with skill name and data
        payload = {"skill": skill, **data}
        message_text = json.dumps(payload)

        # Create A2A message request
        send_message_payload = {
            "message": {
                "role": "user",
                "parts": [{"kind": "text", "text": message_text}],
                "messageId": uuid4().hex,
            }
        }

        request = SendMessageRequest(
            id=str(uuid4()), params=MessageSendParams(**send_message_payload)
        )

        # Send message and get response
        response = await self._client.send_message(request)

        # Extract text content from response
        # Response structure: response.root.result.parts[0].root.text
        if response.root and hasattr(response.root, "result"):
            result = response.root.result
            if hasattr(result, "parts") and result.parts:
                for part in result.parts:
                    if hasattr(part, "root") and hasattr(part.root, "text"):
                        result_text = part.root.text
                        return json.loads(result_text)

        raise RuntimeError(f"No valid response from green agent for skill: {skill}")

    async def distribute_problem(self, agent_id: str, agent_name: str) -> Dict[str, Any]:
        """
        Request a problem from the green agent.

        Returns dict with keys:
        - status: "accepted" | "rejected" | "finished"
        - problem_description: str (if accepted)
        - starter_code: str (if accepted)
        - entry_point: str (if accepted)
        - prompt: str (if accepted)
        - error: str (if rejected)
        """
        logger.info(
            f"Requesting problem from green agent for {agent_name} (ID: {agent_id})"
        )
        return await self._call_skill(
            "distribute_problem", {"id": agent_id, "name": agent_name}
        )

    async def process_answer(
        self, agent_id: str, agent_name: str, solution: str
    ) -> Dict[str, Any]:
        """
        Submit a solution to the green agent.

        Returns dict with keys:
        - status: "accepted" | "rejected" | "finished"
        - error: str (if rejected)
        """
        logger.info(f"Submitting solution for {agent_name} (ID: {agent_id})")
        return await self._call_skill(
            "process_answer", {"id": agent_id, "name": agent_name, "solution": solution}
        )

    async def register(self, agent_name: str) -> Dict[str, Any]:
        """
        Register with the green agent.

        Returns dict with keys:
        - status: "accepted" | "rejected"
        - id: str (if accepted)
        - error: str (if rejected)
        """
        logger.info(f"Registering agent: {agent_name}")
        return await self._call_skill("register", {"name": agent_name})
