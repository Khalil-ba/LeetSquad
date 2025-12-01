import asyncio
import json
from uuid import uuid4
from a2a.client import A2AClient
from a2a.types import MessageSendParams, SendMessageRequest
import httpx


def start_solving(host="localhost", port=9998):
    base_url = f"http://{host}:{port}"

    async def runner():
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
            
            request = SendMessageRequest(id=str(uuid4()), params=MessageSendParams(message=message))
            print("Sending message")
            await client.send_message(request)

    asyncio.run(runner())
