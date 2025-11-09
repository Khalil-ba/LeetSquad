import asyncio
import json
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest
from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH


async def test_green_agent() -> None:
    base_url = "http://localhost:9999"

    async with httpx.AsyncClient() as httpx_client:
        # Initialize A2ACardResolver
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )

        # Fetch Public Agent Card
        print_header("Testing: fetch agent card")
        print(f"Fetching agent card from: {base_url}{AGENT_CARD_WELL_KNOWN_PATH}")
        agent_card = await resolver.get_agent_card()
        print("Agent card fetched successfully:")
        # print(agent_card.model_dump_json(indent=2, exclude_none=True))

        # Initialize A2AClient
        client = A2AClient(httpx_client=httpx_client, agent_card=agent_card)
        print("A2AClient initialized.\n")

        # Test: Register skill
        print_header("Testing: register dummy_agent")
        register_input = {"skill": "register", "name": "dummy_agent"}
        response = await send_message(client, register_input)
        response_message = retrieve_message(response)
        print(f"Response: {response_message}")
        id = response_message["id"]

        # Test: Distribute Problem
        print_header("Testing: distribute 1st problem")
        distribute_input = {
            "skill": "distribute_problem",
            "name": "dummy_agent",
            "id": id,
        }
        response = await send_message(client, distribute_input)
        response_message = retrieve_message(response)
        print(f"Response: {json.dumps(response_message, indent=4)}")

        # Test: Distribute Problem (w/o answer submitted)
        print_header("Testing: distribute problem w/o answer submitted")
        distribute_input = {
            "skill": "distribute_problem",
            "name": "dummy_agent",
            "id": id,
        }
        response = await send_message(client, distribute_input)
        response_message = retrieve_message(response)
        print(f"Response: {json.dumps(response_message, indent=4)}")


async def send_message(a2a_client, input_dict: dict):
    """
    Sends a message to the green agent. Sample input:
    {
        "skill": "register",
        "name": "dummy_agent"
    }
    """
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
    response = await a2a_client.send_message(request)
    return response


def retrieve_message(response):
    """
    Unpacks the response from green agent and retrieves the message.
    """
    result_dict = response.model_dump(mode="json", exclude_none=True)
    text_json_str = result_dict["result"]["parts"][0]["text"]
    return json.loads(text_json_str)


def print_header(header: str):
    """
    Helper for formatting console output.
    """
    print()
    print("=" * 50)
    print(header)
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(test_green_agent())
