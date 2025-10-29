# leetcode-benchmark

Group project for Agentic AI. We're building a green (eval) agent that benchmarks white (participant) agents on code generation capabilities using Leetcode problems.

## 1. Environment Setup

This section provides instructions for setting up the runtime of the green agent. 

**Important: All commands below assume you are running from the project’s root directory.**

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

This project uses **uv** to manage packages. To set up the Python runtime, simply run `uv sync` to create a virtual environment.

Alternatively, you can also use **pip** to install all required packages `pip install -r requirements.txt`.

### 1.3 Start the Server

To start the green agent server, run `uv run python src/start_server.py`.

To interact with this server, modify `test_server.py` and run `uv run src/python test_server.py`.

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
