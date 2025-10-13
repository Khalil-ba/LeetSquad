# leetcode-benchmark
Group project for Agentic AI. We're building a green (eval) agent that benchmarks white (participant) agents on code generation capabilities using Leetcode problems. 

## AWS Credentials Setup
This project uses AWS Bedrock for LLM access. The Bedrock client will fail if you do not set up AWS credentials properly.

To obtain AWS credentials:
1. Open AWS console
2. Go to IAM -> Users -> username -> Security credentials
3. Click on 'Create access key'
4. Save your access key ID and secret access key

For Windows:
1. Open a terminal in Powershell
2. run `pip install awscli`
3. run `aws configure`
4. Configure your AWS access key ID and secret access key

For Mac:
1. Open a terminal
2. run `brew update` and then `brew install awscli`
3. run `aws configure`
4. Configure your AWS access key ID and secret access key

`bedrock_test.py` is provided as a playground for Bedrock. You can also use it to test if AWS credentials have been set up properly on your machine.
