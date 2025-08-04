import os
from dotenv import load_dotenv
import openai

# Load credentials from .env
load_dotenv()

# Set up OpenAI client for Azure
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

response = openai.ChatCompletion.create(
    engine=deployment_name,  # this is your Azure deployment name

    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a fun bedtime story about a robot and a cat."}
    ]
)

print(response['choices'][0]['message']['content'])

