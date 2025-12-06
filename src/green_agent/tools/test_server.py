import json
import textwrap
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest
from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH

"""
A runnable file that spins up a simple white agent and tests its interaction with
the green agent. To use, run these commands from the root dir in order:
1. uv run python -m src.main launch green
2. uv run python -m src.green_agent.test_server
"""


async def test_green_agent(host: str, port: str) -> None:
    base_url = f"http://{host}:{port}"

    async with httpx.AsyncClient() as httpx_client:
        # Fetch Public Agent Card
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )
        print_header("Testing: fetch agent card")
        print(f"Fetching agent card from: {base_url}{AGENT_CARD_WELL_KNOWN_PATH}")
        agent_card = await resolver.get_agent_card()
        print("Agent card fetched successfully:")
        print(agent_card)

        # Initialize A2AClient
        client = A2AClient(httpx_client=httpx_client, agent_card=agent_card)
        print("A2AClient initialized.\n")

        # Test: Register skill
        print_header("Testing: register correct_agent")
        register_input = {"skill": "register", "name": "correct_agent"}
        response = await send_message(client, register_input)
        response_message = retrieve_message(response)
        print(f"Response: {response_message}")
        id = response_message["id"]

        # Test: Distribute Problem
        print_header("Testing: distribute 1st problem")
        distribute_input = {
            "skill": "distribute_problem",
            "name": "correct_agent",
            "id": id,
        }
        response = await send_message(client, distribute_input)
        response_message = retrieve_message(response)
        print(f"Response: {json.dumps(response_message, indent=4)}")

        # Test: Submit Answer (correct answer)
        print_header("Testing: submit answer")
        solution = textwrap.dedent(
            """
            class Solution:
                def twoSum(self, nums: List[int], target: int) -> List[int]:
                    num_map = {}
                    for i, num in enumerate(nums):
                        complement = target - num
                        if complement in num_map:
                            return [num_map[complement], i]
                        else:
                            num_map[num] = i
            """
        )
        submit_input = {
            "skill": "process_answer",
            "name": "correct_agent",
            "id": id,
            "solution": solution,
        }
        response = await send_message(client, submit_input)
        response_message = retrieve_message(response)
        print(f"Response: {json.dumps(response_message, indent=4)}")

        # Test: Distribute Problem
        print_header("Testing: distribute 2nd problem")
        distribute_input = {
            "skill": "distribute_problem",
            "name": "correct_agent",
            "id": id,
        }
        response = await send_message(client, distribute_input)
        response_message = retrieve_message(response)
        print(f"Response: {json.dumps(response_message, indent=4)}")

        print_header("Testing: submit answer")
        solution = textwrap.dedent(
            """
            class Solution:
                def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                    dummy = ListNode(0)
                    cur = dummy
                    carry = 0

                    # Loop until both lists are exhausted and no carry remains
                    while l1 is not None or l2 is not None or carry != 0:
                        v1 = l1.val if l1 is not None else 0
                        v2 = l2.val if l2 is not None else 0

                        total = v1 + v2 + carry
                        carry = total // 10
                        digit = total % 10

                        cur.next = ListNode(digit)
                        cur = cur.next

                        if l1 is not None:
                            l1 = l1.next
                        if l2 is not None:
                            l2 = l2.next

                    return dummy.next
            """
        )
        submit_input = {
            "skill": "process_answer",
            "name": "correct_agent",
            "id": id,
            "solution": solution,
        }
        response = await send_message(client, submit_input)
        response_message = retrieve_message(response)
        print(f"Response: {json.dumps(response_message, indent=4)}")

        await two_sum_agent(
            client,
            "incorrect",
            textwrap.dedent(
                """
                class Solution:
                    def twoSum(self, nums: List[int], target: int) -> List[int]:
                        num_map = {}
                        for i, num in enumerate(nums):
                            complement = target - num
                            if complement in num_map:
                                return [complement, num]
                            else:
                                num_map[num] = i
                """
            ),
        )

        await two_sum_agent(
            client,
            "correct_O(n^2)",
            textwrap.dedent(
                """
                class Solution:
                    def twoSum(self, nums: List[int], target: int) -> List[int]:
                        n = len(nums)
                        # We iterate i from left to right, matching the original function
                        for i in range(n):
                            last_j = None
                            # Check all previous elements j < i
                            for j in range(i):
                                if nums[j] + nums[i] == target:
                                    # Keep updating to get the *last* such j < i
                                    last_j = j
                            # As soon as we find at least one match for this i,
                            # we return [last_j, i], matching the hashmap behavior.
                            if last_j is not None:
                                return [last_j, i]
                """
            ),
        )

        await two_sum_agent(
            client,
            "correct_bad_style",
            textwrap.dedent(
                """
                class Solution:
                    def twoSum(self, nums: List[int], target: int) -> List[int]:
                        foobar = None
                        foobar = {}
                        for i, x in enumerate(nums):
                            y = target - x
                            if y in foobar:
                                return [foobar[y], i]
                            else:
                                foobar[x] = i
                                continue
                """
            ),
        )


async def two_sum_agent(client: A2AClient, agent_name: str, solution: str):
    """
    This helper function registers a new agent (with given name), retrieves the first
    problem (two-sum), and submits the given answer
    """
    # Register
    register_input = {"skill": "register", "name": agent_name}
    response = await send_message(client, register_input)
    response_message = retrieve_message(response)
    id = response_message["id"]

    # Retrieve the first (two-sum) problem
    distribute_input = {
        "skill": "distribute_problem",
        "name": agent_name,
        "id": id,
    }
    response = await send_message(client, distribute_input)
    response_message = retrieve_message(response)

    # Submit Answer
    submit_input = {
        "skill": "process_answer",
        "name": agent_name,
        "id": id,
        "solution": solution,
    }
    response = await send_message(client, submit_input)
    response_message = retrieve_message(response)

    print_header(f"White agent {agent_name} successfully submitted solution for two-sum")


async def send_message(a2a_client, input_dict: dict):
    """
    Sends a message to the green agent. Sample input:
    {
        "skill": "register",
        "name": "correct_agent"
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
