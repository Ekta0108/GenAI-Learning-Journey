import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

prompt = "Once upon a time, a robot and a cat"

# Try different temperatures here
for temp in [0, 0.5, 1.0]:
    print(f"\n--- Temperature: {temp} ---")
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        temperature=temp,
        messages=[
            {"role": "system", "content": "Continue the story in a creative way."},
            {"role": "user", "content": prompt}
        ]
    )
    print(response['choices'][0]['message']['content'])
