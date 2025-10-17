from bedrock_client import BedrockClient

#####################################################################
# Use this file as a Bedrock playground or test your AWS connection #
##################################################################### 

def main():
    bedrock_client = BedrockClient()

    # use this line to list all available LLMs on Bedrock
    # print(bedrock_client.list_models())

    response = bedrock_client.generate("hello")
    print(response)


if __name__ == '__main__':
    main()
