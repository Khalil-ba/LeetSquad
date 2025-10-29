import asyncio
import logging
from typing import Any
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest
from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH


async def test_green_agent() -> None:
    """Test client for the green agent (server.py)."""
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    base_url = 'http://localhost:9999'

    async with httpx.AsyncClient() as httpx_client:
        # Initialize A2ACardResolver
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )

        # Fetch Public Agent Card
        logger.info(
            f'Fetching agent card from: {base_url}{AGENT_CARD_WELL_KNOWN_PATH}'
        )
        agent_card = await resolver.get_agent_card()
        logger.info('Agent card fetched successfully:')
        logger.info(agent_card.model_dump_json(indent=2, exclude_none=True))

        # Initialize A2AClient
        client = A2AClient(
            httpx_client=httpx_client,
            agent_card=agent_card
        )
        logger.info('A2AClient initialized.\n')

        # Test 1: Register skill
        logger.info('=' * 50)
        logger.info('Testing: register skill')
        logger.info('=' * 50)
        register_input: dict[str, Any] = {
            'message': {
                'role': 'user',
                'parts': [
                    {
                        'kind': 'text',
                        'text': '{"skill": "register"}'
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
        logger.info(f'Response: {response.model_dump(mode="json", exclude_none=True)}\n')

        logger.info('All tests completed!')


if __name__ == '__main__':
    asyncio.run(test_green_agent())
