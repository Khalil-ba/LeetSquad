"""Launcher module - initiates and coordinates the evaluation process."""

import json
from uuid import uuid4
import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest


async def _send_skill_message(url: str, skill_data: dict):
    async with httpx.AsyncClient() as httpx_client:
        resolver = A2ACardResolver(httpx_client=httpx_client, base_url=url)
        agent_card = await resolver.get_agent_card()
        client = A2AClient(httpx_client=httpx_client, agent_card=agent_card)
        
        payload = {
            "message": {
                "role": "user",
                "parts": [{"kind": "text", "text": json.dumps(skill_data)}],
                "messageId": uuid4().hex,
            }
        }
        
        request = SendMessageRequest(
            id=str(uuid4()), 
            params=MessageSendParams(**payload)
        )
        
        response = await client.send_message(request)
        result_dict = response.model_dump(mode="json", exclude_none=True)
        text_json_str = result_dict["result"]["parts"][0]["text"]
        return json.loads(text_json_str)


async def launch_remote_evaluation(green_url: str, white_url: str):
    print(f"Triggering white agent at {white_url}...")
    response = await _send_skill_message(white_url, {"skill": "start_solving"})
    print(f"Response: {response.get('status')}")