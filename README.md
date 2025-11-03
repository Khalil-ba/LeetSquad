# leetcode-benchmark

Group project for Agentic AI. We're building a green (eval) agent that benchmarks white (participant) agents on code generation capabilities using Leetcode problems.

## 1. Environment Setup

This section provides instructions for setting up the runtime of the agents.

**Important: All commands below assume you are running from the project's root directory.**

### 1.1 AWS Credentials Setup

The green agent uses AWS Bedrock for LLM access and DynamoDB for data storage. The Bedrock & DynamoDB clients will fail if you do not set up AWS credentials properly.

To obtain AWS credentials (assuming you already have an AWS account):

1. Open AWS console
2. Go to IAM -> Users -> username -> Security credentials
3. Click on 'Create access key'
4. Save your access key ID and secret access key

For Windows:

1. Open a terminal in Powershell
2. run `pip install awscli`
3. run `aws configure`
4. Configure your AWS access key ID and secret access key

For Mac:

1. Open a terminal
2. run `brew update` and then `brew install awscli`
3. run `aws configure`
4. Configure your AWS access key ID and secret access key

`bedrock_test.py` is provided as a playground for Bedrock. You can also use it to test if AWS credentials have been set up properly on your machine.

### 1.2 Python Runtime

This project uses **uv** to manage packages. To set up the Python runtime:

1. Create a virtual environment: `uv venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Install dependencies: `uv sync`

Alternatively, you can use **pip**: `pip install -r requirements.txt`

**Development Tools:**

- Format code: `uv run ruff format` (auto-formats with ruff)
- Lint code: `uv run ruff check`
- Add dependencies: Add to `pyproject.toml`, then run `uv lock` followed by `uv sync`
- Update requirements.txt: `uv pip compile pyproject.toml -o requirements.txt` (for pip users only, not needed once everyone uses uv)

We use pinned dependencies (via `uv.lock`) to ensure reproducibility across developers and deployment environments.

### 1.3 CLI Commands

The main entry point is `python -m src.main` with the following commands:

**Launch Commands** (primary workflow):

```bash
# Start green agent (evaluation server)
python -m src.main launch green [--host HOST] [--port PORT]

# Start white agent (solver)
python -m src.main launch white [--host HOST] [--port PORT] [--agent-id ID] [--agent-name NAME]

# Start both agents
python -m src.main launch both [--green-port PORT] [--white-port PORT]
```

**Test Commands** (quick testing, green only for now):

```bash
# Run tests on green agent
python -m src.main test green \
  [--model MODEL_ID] \
  [--skip-tests] \
  [--skip-llm-judge] \
  [--limit N] \
  [--task-id ID] \
  [--agents agent1,agent2] \
  [--csv-path PATH]
```

**Note:** The test workflow is currently more developed but should eventually converge with the launch workflow to call the same underlying logic. For production use, prefer the `launch` commands.

## 2. Agent Interaction

The communication between green and white agents is handled through A2A protocol.

The green agent exposes the following skills:

- register
- distribute_problem
- process_answer

### 2.1 Register

The white agent invokes this skill to register itself with the green agent. Upon receiving the request, the green agent will assign an ID to the white agent.

Input schema:

```json
{
    "skill": "register",
    "name": "<white agent name>"
}
```

Output schema:

```json
{
    "id": "<assigned ID>"
}
```

### 2.2 Distribute Problem

The white agent invokes this skill to get a new coding problem from the green agent.

Input schema:

```json
{
    "id": "<assigned ID>",
    "name": "<white agent name, acts as a simple auth token>"
}
```

Output schema:

```json
{
    "status": "accepted/rejected",
    "error": "<reason for rejection, only exists if rejected>",
    "problem_description": "<problem description>",
    "starter_code": "<starter code>",
    "entry_point": "<entry point in starter code>",
    "prompt": "<prompt>"
}
```

### 2.3 Process Answer

The white agent invokes this skill to submit its answer to the green agent. The green agent will then evaluate the generated code based on its correctness and readability, and record the scores.

Input schema:

```json
{
    "id": "<assigned ID>",
    "name": "<white agent name, acts as a simple auth token>",
    "solution": "<generated code>"
}
```

Output schema:

```json
{
    "status": "accepted/rejected",
    "error": "<reason for rejection, only exists if rejected>"
}
```
