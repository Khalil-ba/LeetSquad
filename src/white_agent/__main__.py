import uvicorn
from pathlib import Path

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
    AgentExecutor,
    ExecuteRequest,
    TaskOutput,
)


class LeetCodeSolutionExecutor(AgentExecutor):
    def __init__(self, solutions_dir: str = "./solutions"):
        self.solutions_dir = Path(solutions_dir)
        self.solutions_dir.mkdir(exist_ok=True)
    
    async def execute(self, request: ExecuteRequest) -> TaskOutput:
        task_id = request.input_data.get("task_id")
        
        if not task_id:
            return TaskOutput(
                output_data={"error": "task_id is required"},
                output_mode="text"
            )
        
        solution_file = self.solutions_dir / f"{task_id}.txt"
        
        if not solution_file.exists():
            return TaskOutput(
                output_data={"error": f"Solution not found for task_id: {task_id}"},
                output_mode="text"
            )
        
        solution = solution_file.read_text()
        
        return TaskOutput(
            output_data={
                "task_id": task_id,
                "solution": solution
            },
            output_mode="text",
            artifacts=[{
                "type": "code",
                "content": solution,
                "filename": f"{task_id}_solution.py"
            }]
        )


if __name__ == '__main__':
    skill = AgentSkill(
        id='leetcode_solution',
        name='LeetCode Solution Provider',
        description='Returns pre-written solutions for LeetCode problems based on task_id',
        tags=['leetcode', 'coding', 'solutions'],
        examples=['solve two-sum', 'get solution for task_id: two-sum'],
    )

    agent_card = AgentCard(
        name='LeetCode Solution Agent',
        description='Provides LeetCode solutions from prepared files',
        url='http://localhost:9999/',
        version='1.0.0',
        default_input_modes=['text'],
        default_output_modes=['text'],
        capabilities=AgentCapabilities(streaming=False),
        skills=[skill],
    )

    request_handler = DefaultRequestHandler(
        agent_executor=LeetCodeSolutionExecutor(solutions_dir="./solutions"),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler,
    )

    print("Starting LeetCode Solution Server on port 9999")
    uvicorn.run(server.build(), host='0.0.0.0', port=9999)