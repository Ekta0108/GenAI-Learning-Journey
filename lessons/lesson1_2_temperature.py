import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

open_ai_endpoint = os.getenv("OPEN_AI_ENDPOINT")
open_ai_key = os.getenv("OPEN_AI_KEY")
chat_model = os.getenv("CHAT_MODEL")

client = AzureOpenAI(
    api_key=open_ai_key,
    azure_endpoint=open_ai_endpoint,
    api_version="2024-10-21"
)

prompt = "Once upon a time, a robot and a cat"

# Try different temperatures here
for temp in [0, 0.5, 1.0]:
    print(f"\n--- Temperature: {temp} ---")
    response = client.chat.completions.create(
        model=chat_model,
        temperature=temp,
        messages=[
            {"role": "system", "content": "Continue the story in a creative way."},
            {"role": "user", "content": prompt}
        ]
    )
    print(response.choices[0].message.content)
