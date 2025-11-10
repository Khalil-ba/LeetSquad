# LeetSquad

Group project for Agentic AI. We're building a green (eval) agent that benchmarks white (participant) agents on code generation capabilities using Leetcode problems.

**Important: All commands below assume you are running from the project's root directory.**

## 1. Setup

### 1.1. AWS Setup

The green agent uses AWS Bedrock for LLM access. You MUST configure AWS credentials to run the green agent. To obtain AWS credentials (assuming you already have an AWS account):

1. Open AWS console
2. Go to IAM -> Users -> username -> Security credentials
3. Click on 'Create access key'
4. Copy your access key ID and secret access key
5. Create `.env` file under project root folder and configure:
```
AWS_ACCESS_KEY_ID="<replace>"
AWS_SECRET_ACCESS_KEY="<replace>"
```

*For CS 294 course staff: please contact the author if you need temporary AWS credentials*

### 1.2. Python Runtime Setup

```bash
# Create a virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv sync
```

## 2. Usage

```bash
# Start green agent (evaluation agent)
uv run python -m src.main launch green [--optional-params]

# Start white agent (solver agent)
uv run python -m src.main launch white [--optional-params]

# Retrieve benchmarking results from green agent
uv run python -m src.green_agent.report_results
```

To see optional param usage:

```bash
uv run python -m src.main launch green --help
uv run python -m src.main launch white --help
```

Once the green agent is running:

```bash
# Run some simple test cases on green agent
uv run python -m src.green_agent.test_server
```

## 3. Agent Interaction

The communication between green and white agents is handled through A2A protocol. The green agent exposes the following skills:

### 3.1 Register

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
    "status": "accepted",
    "id": "<assigned ID>"
}
```

### 3.2 Distribute Problem

The white agent invokes this skill to get a new coding problem from the green agent.

Input schema:

```json
{
    "skill": "distribute_problem",
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
    "entry_point": "<entry point in starter code>"
}
```

### 3.3 Process Answer

The white agent invokes this skill to submit its answer to the green agent. The green agent will then evaluate the generated code based on its correctness and readability, and record the scores.

Input schema:

```json
{
    "skill": "process_answer",
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

### 3.4 Report Results

This skill is NOT included in the public agent card and should NOT be used by white agents. Rather, it provides an interface to collect benchmarking results from the green agent.

Input schema:

```json
{
    "skill": "report_results"
}
```

Output schema:

```json
{
    "status": "accepted/rejected",
    "error": "<reason for rejection, only exists if rejected>",
    "results": "<benchmarking results>"
}
```

## 4. For Developers

```bash
# Lint code
uv run ruff check

# Auto-format code
uv run ruff format

# To add a new dependency, modify `pyproject.toml` file , then run
uv lock
uv sync
```