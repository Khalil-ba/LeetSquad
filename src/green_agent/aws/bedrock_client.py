import json

import boto3

DEFAULT_MODEL_ID = "anthropic.claude-3-5-haiku-20241022-v1:0"


class BedrockClient:
    def __init__(self, model_id=None, region="us-west-2"):
        """
        Initialize the Bedrock clinet
        """
        self.model_id = model_id or DEFAULT_MODEL_ID
        self.region = region
        self.client = boto3.client("bedrock-runtime", region_name=region)

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

    def generate(self, prompt, max_tokens=512):
        """
        Send a prompt to the LLM and return the generated text.
        """
        body = {
            "messages": [
                {"role": "user", "content": [{"type": "text", "text": prompt}]}
            ],
            "max_tokens": max_tokens,
            "anthropic_version": "bedrock-2023-05-31",
        }

        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json",
        )

        result = json.loads(response["body"].read())
        parts = result.get("content", [])
        text = "\n".join(p.get("text", "") for p in parts if "text" in p)
        return text
