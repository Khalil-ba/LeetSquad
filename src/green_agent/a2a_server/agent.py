import json
import uuid


class CodingEvaluationAgent:
    async def register(self, input) -> str:
        """
        Register the white agent with the green agent.
        See README.md for input and output schema.
        """
        # generate random ID for white agent
        id = uuid.uuid4().hex[:8]

        # TODO: store white agent ID in database
        result = {
            "status": "accepted",
            "id": id
        }
        return json.dumps(result)


    async def distribute_problem(self, input) -> str:
        """
        Distribute a new coding problem to the white agent.
        See README.md for input and output schema.
        """
        # TODO: look up white agent in DB and determine if it's registered
        registered = True
        if not registered:
            return json.dumps({
                "status": "rejected",
                "error": "Agent not registered. Please register first."
            })

        # TODO: check if name matches ID
        name_matches_id = True
        if not name_matches_id:
            return json.dumps({
                "status": "rejected",
                "error": "Name does not match ID."
            })

        # TODO: determine if a problem has already been distributed
        problem_distributed = False
        if problem_distributed:
            return json.dumps({
                "status": "rejected",
                "error": "Problem already distributed. Please submit your answer first."
            })

        # TODO: distribute problem to white agent
        result = {
            "status": "accepted",
            "problem_description": "Problem description",
            "starter_code": "Starter code",
            "entry_point": "Entry point",
            "prompt": "Prompt"
        }
        return json.dumps(result)


    async def process_answer(self, input) -> str:
        """
        Process the answer from the white agent.
        See README.md for input and output schema.
        """
        # TODO: look up white agent in DB and determine if it's registered
        registered = True
        if not registered:
            return json.dumps({
                "status": "rejected",
                "error": "Agent not registered. Please register first."
            })

        # TODO: check if name matches ID
        name_matches_id = True
        if not name_matches_id:
            return json.dumps({
                "status": "rejected",
                "error": "Name does not match ID."
            })

        # TODO: run the solution against test cases (based on task ID, which is
        #       hidden from white agent)

        # TODO: perform readability analysis

        # TODO: record the scores in DB

        return json.dumps({
            "status": "accepted"
        })
