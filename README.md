# LeetSquad

Group project for Agentic AI. We're building a green (eval) agent that benchmarks white (participant) agents on code generation capabilities using Leetcode problems.

**Important: All commands below assume you are running from the project's root directory.**

## 1. Setup

### 1.1. LLM API Key Setup

The green agent uses LLM to evaluate time/space complexity and readability. The default LLM provider is OpenAI, but you can also use AWS Bedrock.

| Provider    | Default Model                    | Quality | Cost             | Latency  |
|-------------|----------------------------------|---------|------------------|----------|
| OpenAI      | GPT 5.1 Mini                     | Higher  | Slightly Higher  | Higher   |
| AWS         | Qwen3 Coder 480B A35B Instruct   | Lower   | Slightly Lower   | Lower    |

You MUST configure corresponding API key by creating a `.env` file under the project root folder. 

If you choose OpenAI, add
```
OPENAI_API_KEY="<replace>"
```

If you choose AWS Bedrock, add
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
uv run python -m src.main report
```

To see optional param usage:

```bash
uv run python -m src.main launch green --help
uv run python -m src.main launch white --help
```

Once the green agent is running:

```bash
# Run some simple test cases on green agent
uv run python -m src.main test green

# Wait for a while and get aggregated results
uv run python -m src.main report
```

## 3. Agent Interaction

The communication between green and white agents is handled through A2A protocol. The green agent exposes the following skills:

### 3.1 Get Instructions
The white agent invokes this skill to get a kick-off message with instructions for subsequent interactions. **We assume all white agents have prior knowledge to use this skill as the starting point.**

Input schema:

```json
{
    "skill": "get_instructions"
}
```

Output schema:

```json
{
    "status": "accepted",
    "instructions": "<a long kick-off message>"
}
```

### 3.2 Register

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

### 3.3 Distribute Problem

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

### 3.4 Process Answer

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

### 3.5 *Report Results

This skill is NOT included in the public agent card and should NOT be used by white agents. Rather, it's included as a convenience skill to collect benchmarking results from the green agent.

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