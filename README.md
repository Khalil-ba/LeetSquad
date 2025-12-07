# LeetSquad

Group project for Agentic AI. We're building a green (eval) agent that benchmarks white (participant) agents on code generation capabilities using Leetcode problems.

**Important: All commands below assume you are running from the project's root directory.**

## 1. Setup

### 1.1. API Key Setup

Create a `.env` file under the project root directory and configure:

```
OPENAI_API_KEY="<your API key>"
```

Both the green and white agent use LLM. The default model is GPT-5-Mini.

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
# 1. Launch green agent
uv run python -m src.main launch green [--optional-params]

# 2. In a separate terminal, launch white agent (it won't start solving problems yet)
uv run python -m src.main launch white [--optional-params]

# 3. In a separate terminal, signal white agent to begin solving problems
uv run python -m src.main run white [--optional-params]

# 4. Wait until completion and retrieve benchmarking results
uv run python -m src.main report
```

Use `--help` to view the optional parameters for each command. You may also omit them to use the default settings.

**Note:**

- The full dataset contains 2,641 problems. By default, the green agent loads only 10. You can use `--limit-problems` to change this.
- By default, the white agent may invoke green-agent skills up to 25 times (enough for 10 problems). You can adjust this using `--max-turns`.
- As a rule of thumb: `max_turns = 2 × limit_problems + 5`

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

### 3.4 *Report Results

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

# Run test cases on green agent
uv run python -m src.main test green
```