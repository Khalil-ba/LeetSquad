import boto3
import json

class BedrockClient:
    MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

    def __init__(self, region="us-west-2"):
        """
        Initialize the Bedrock clinet
        """
        self.region = region
        self.client = boto3.client("bedrock-runtime", region_name=region)

    def list_models(self):
        """
        List available text models
        """
        ctrl = boto3.client("bedrock", region_name=self.region)
        resp = ctrl.list_foundation_models(byOutputModality="TEXT")
        return [
            f"{m['modelId']} | provider={m['providerName']} | inputModalities={m.get('inputModalities')}"
            for m in resp.get("modelSummaries", [])
        ]

    def generate(self, prompt, max_tokens=512):
        """
        Send a prompt to the LLM and return the generated text.
        """
        body = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": prompt
                        }
                    ]
                }
            ],
            "max_tokens": max_tokens,
            "anthropic_version": "bedrock-2023-05-31"
        }

        response = self.client.invoke_model(
            modelId=self.MODEL_ID,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json"
        )

        result = json.loads(response["body"].read())
        parts = result.get("content", [])
        text = "\n".join(p.get("text", "") for p in parts if "text" in p)
        return text
