import json
import logging
from uuid import uuid4
from a2a.client import A2AClient
from a2a.types import MessageSendParams, SendMessageRequest
import httpx

logger = logging.getLogger(__name__)


async def start_solving(host="localhost", port=9998):
    base_url = f"http://{host}:{port}"
    async with httpx.AsyncClient() as httpx_client:
        client = A2AClient(httpx_client=httpx_client, url=base_url)
        message = {
            "role": "user",
            "parts": [
                {
                    "kind": "text",
                    "text": json.dumps({"skill": "start_solving"}),
                }
            ],
            "messageId": uuid4().hex,
        }
        request = SendMessageRequest(
            id=str(uuid4()), params=MessageSendParams(message=message)
        )
        response = await client.send_message(request)
        result_dict = response.model_dump(mode="json", exclude_none=True)
        text_json_str = result_dict["result"]["parts"][0]["text"]
        status = json.loads(text_json_str).get("status")
        if status == "accepted":
            logger.info(f"Successfully triggered white agent running on {base_url}")
        else:
            logger.error(f"Failed to trigger white agent running on {base_url}")
