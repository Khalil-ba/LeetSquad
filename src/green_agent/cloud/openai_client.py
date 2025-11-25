import os
from dotenv import load_dotenv
from openai import OpenAI


class OpenAIClient:
    DEFAULT_MODEL_ID = "gpt-5-mini"

    def __init__(self, model_id=None, base_url=None) -> None:
        load_dotenv()  # load OPENAI_API_KEY from .env
        if "OPENAI_API_KEY" not in os.environ:
            raise EnvironmentError("Please configure OPENAI_API_KEY in .env")

        self.model_id = model_id or OpenAIClient.DEFAULT_MODEL_ID
        self.client = OpenAI(base_url=base_url)

    def generate(self, system_prompt, message, max_tokens=1000):
        request_params = {
            "model": self.model_id,
            "instructions": system_prompt,
            "input": message,
            "store": False,  # this prevents OpenAI from storing results on their server
            # "temperature": 0,  # GPT-5 doesn't support temperature
        }
        if max_tokens is not None:
            request_params["max_output_tokens"] = max_tokens
        if self.model_id.startswith("gpt-5"):
            request_params["reasoning"] = {"effort": "low"}
        response = self.client.responses.create(**request_params)
        return response.output_text
