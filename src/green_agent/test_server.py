import asyncio
from typing import Any
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest
from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH


async def test_green_agent() -> None:
    base_url = 'http://localhost:9999'

    async with httpx.AsyncClient() as httpx_client:
        # Initialize A2ACardResolver
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )

        # Fetch Public Agent Card
        print(f'Fetching agent card from: {base_url}{AGENT_CARD_WELL_KNOWN_PATH}')
        agent_card = await resolver.get_agent_card()
        print('Agent card fetched successfully:')
        print(agent_card.model_dump_json(indent=2, exclude_none=True))

        # Initialize A2AClient
        client = A2AClient(
            httpx_client=httpx_client,
            agent_card=agent_card
        )
        print('A2AClient initialized.\n')

        # Test: Register skill
        print('=' * 50)
        print('Testing: register skill')
        print('=' * 50)
        register_input: dict[str, Any] = {
            'message': {
                'role': 'user',
                'parts': [
                    {
                        'kind': 'text',
                        'text': '{"skill": "register", "name": "dummy_agent"}'
                    }
                ],
                'messageId': uuid4().hex,
            },
        }
        request = SendMessageRequest(
            id=str(uuid4()),
            params=MessageSendParams(**register_input)
        )
        response = await client.send_message(request)
        print(f'Response: {response.model_dump(mode="json", exclude_none=True)}\n')


if __name__ == '__main__':
    asyncio.run(test_green_agent())
