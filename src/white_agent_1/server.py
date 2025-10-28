from a2a_sdk import ServerFunction

def create_white_agent_server():
    server = ServerFunction(
        name="leetcode_solver",
        agent_card_path="agents/white_agent/agent_card.json"
    )
    return server