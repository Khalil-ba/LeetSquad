import json
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest
from a2a.utils.constants import EXTENDED_AGENT_CARD_PATH

"""
A runnable file that collects benchmarking results from the green agent.
"""


async def report_results() -> None:
    base_url = "http://localhost:9999"

    async with httpx.AsyncClient() as httpx_client:
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )
        auth_headers_dict = {"Authorization": "reporting_agent"}
        agent_card = await resolver.get_agent_card(
            relative_card_path=EXTENDED_AGENT_CARD_PATH,
            http_kwargs={"headers": auth_headers_dict},
        )
        client = A2AClient(httpx_client=httpx_client, agent_card=agent_card)

        input_dict = {"skill": "report_results"}
        input = {
            "message": {
                "role": "user",
                "parts": [
                    {
                        "kind": "text",
                        "text": json.dumps(input_dict),
                    }
                ],
                "messageId": uuid4().hex,
            },
        }
        request = SendMessageRequest(id=str(uuid4()), params=MessageSendParams(**input))
        response = await client.send_message(request)
        result_dict = response.model_dump(mode="json", exclude_none=True)
        text_json_str = result_dict["result"]["parts"][0]["text"]
        results = json.loads(text_json_str).get("results")

        # Print results to console (can be changed to a file)
        print(json.dumps(results, indent=4))
