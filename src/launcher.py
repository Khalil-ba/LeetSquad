"""Launcher module - initiates and coordinates the evaluation process."""

import multiprocessing
import time
import json
from uuid import uuid4
import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import MessageSendParams, SendMessageRequest


def _start_green(host, port, **kwargs):
    """Start green agent in separate process"""
    from .green_agent.tools.start_server import start_server
    start_server(host, port, **kwargs)


def _start_white(host, port, agent_id, agent_name):
    """Start white agent in separate process"""
    from .white_agent.server import start_server
    start_server(host, port, agent_id, agent_name)


async def _trigger_white_agent(white_url: str):
    """Send a message to white agent to start solving"""
    async with httpx.AsyncClient() as httpx_client:
        # Get white agent card
        resolver = A2ACardResolver(httpx_client=httpx_client, base_url=white_url)
        agent_card = await resolver.get_agent_card()
        
        # Create client
        client = A2AClient(httpx_client=httpx_client, agent_card=agent_card)
        
        # Send solve_problem skill invocation
        payload = {
            "message": {
                "role": "user",
                "parts": [{"kind": "text", "text": json.dumps({"skill": "solve_problem"})}],
                "messageId": uuid4().hex,
            }
        }
        
        request = SendMessageRequest(
            id=str(uuid4()), 
            params=MessageSendParams(**payload)
        )
        
        print("Triggering white agent to start solving problems...")
        response = await client.send_message(request)
        print(f"White agent response: {response}")


async def launch_evaluation():
    """Launch both green and white agents"""
    
    # Start green agent
    print("Starting green agent...")
    green = multiprocessing.Process(
        target=_start_green,
        args=("0.0.0.0", 9999),
        kwargs={"skip_tests": False, "skip_llm_judge": False, "limit_problems": 5}
    )
    green.start()
    
    # Wait for green to be ready
    time.sleep(3)
    print("Green agent ready at http://localhost:9999")
    
    # Start white agent
    print("Starting white agent...")
    white = multiprocessing.Process(
        target=_start_white,
        args=("0.0.0.0", 9998, "white_agent_001", "LeetCodeSolver")
    )
    white.start()
    
    # Wait for white to be ready
    time.sleep(3)
    print("White agent ready at http://localhost:9998")
    
    # Trigger white agent to start solving
    await _trigger_white_agent("http://localhost:9998")
    
    # Keep processes alive
    try:
        print("\nBoth agents running. Press Ctrl+C to stop.")
        green.join()
        white.join()
    except KeyboardInterrupt:
        print("\nShutting down...")
        green.terminate()
        white.terminate()
        green.join()
        white.join()
        print("Done.")

'''import multiprocessing
import time


def _start_green(host, port, **kwargs):
    """Start green agent in separate process"""
    from .green_agent.tools.start_server import start_server
    start_server(host, port, **kwargs)


def _start_white(host, port, agent_id, agent_name):
    """Start white agent in separate process"""
    from .white_agent.server import start_server
    start_server(host, port, agent_id, agent_name)


async def launch_evaluation():
    """Launch both green and white agents"""
    
    # Start green agent
    green = multiprocessing.Process(
        target=_start_green,
        args=("0.0.0.0", 9999),
        kwargs={"skip_tests": False, "skip_llm_judge": False}
    )
    green.start()
    
    # Start white agent
    white = multiprocessing.Process(
        target=_start_white,
        args=("0.0.0.0", 9998, "white_agent_001", "LeetCodeSolver")
    )
    white.start()'''