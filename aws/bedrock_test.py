from bedrock_client import BedrockClient

def main():
    bedrock_client = BedrockClient()
    response = bedrock_client.generate("hello")
    print(response)


if __name__ == '__main__':
    main()
