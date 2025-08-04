import os, sys
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load credentials from .env
load_dotenv()

# Set up OpenAI client for Azure

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

# response = client.chat.completions.create(
#     model=deployment_name,  # this is your Azure deployment name

#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Write a fun bedtime story about a robot and a cat."}
#     ]
# )

# print(response['choices'][0]['message']['content'])

try:
    client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMEN"), 
        messages=[{"role":"system","content":"ping"}]
    )
    print("Chat call succeeded")
except Exception as e:
    print("Error:", repr(e))
    sys.exit(1)

