import boto3
from botocore.config import Config

# DEFAULT_MODEL_ID = "anthropic.claude-3-5-haiku-20241022-v1:0"
DEFAULT_MODEL_ID = "deepseek.v3-v1:0"


class BedrockClient:
    def __init__(self, model_id=None, region="us-west-2"):
        """
        Initialize the Bedrock client

        Args:
            model_id: Model ID to use (defaults to DEFAULT_MODEL_ID)
            region: AWS region (defaults to us-west-2)
        """
        self.model_id = model_id or DEFAULT_MODEL_ID
        self.region = region

        # Setting max_retries=0 disables boto3's automatic retries
        # This allows application-level retry logic to handle throttling
        config = Config(retries={"max_attempts": 1, "mode": "standard"})
        self.client = boto3.client("bedrock-runtime", region_name=region, config=config)

    def list_models(self):
        """
        List available text models
        """
        ctrl = boto3.client("bedrock", region_name=self.region)
        resp = ctrl.list_foundation_models(byOutputModality="TEXT")
        return [
            (
                f"{m['modelId']} | provider={m['providerName']}"
                f" | inputModalities={m.get('inputModalities')}"
            )
            for m in resp.get("modelSummaries", [])
        ]

    def generate(self, system_prompt, message, max_tokens=1000):
        """
        Send a prompt to the LLM and return the generated text.
        """
        content = [{"text": message}]

        response = self.client.converse(
            modelId=self.model_id,
            system=[{"text": system_prompt}],
            messages=[{"role": "user", "content": content}],
            inferenceConfig={"maxTokens": max_tokens},
        )

        # Join all text parts into a single string
        text = "".join(p["text"] for p in response["output"]["message"]["content"])

        # LLM sometimes wraps json inside ```. Remove them if so.
        if text.startswith("```json"):
            text = text[7:].strip()
        elif text.startswith("```"):
            text = text[3:].strip()
        if text.endswith("```"):
            text = text[:-3].strip()

        return text
