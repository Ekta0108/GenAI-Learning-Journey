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

# 1. Zero-Shot Example

prompt_1 = [
    {"role": "user", "content": "Translate this into French: I have a red car."}
]

# 2. Few-Shot Example

prompt_2 = [
    {"role": "user", "content": 
    """Translate the following into French:
    English: I love coffee
    French: J'aime le café

    English: I have a red car
    French:"""}
]

# 3. Chain of Thought Example
prompt_3 = [
    {"role": "user", "content": 
     "If a train leaves Delhi at 3 PM and travels at 60 km/h, how far will it go in 4 hours? Think step by step."}
]

# 4. Custom Prompt Example
prompt_4 = [
    {"role": "system", "content": "You are a sarcastic assistant who answers like a Gen Z TikToker."},
    {"role": "user", "content": "Should I go to the gym today?"}
]

# Custom Function to Ask GPT

def ask_gpt(prompt_messages):
    response = client.chat.completions.create(
        model=chat_model,
        messages= prompt_messages
    )
    return response.choices[0].message.content


# This code sets up an OpenAI client for Azure and sends a prompt to the GPT model.

print("Responses from GPT-3.5 Turbo with different prompting techniques:\n")
print("Zero-Shot Example: ")
print(ask_gpt(prompt_1))
print("Few-Shot Example: ")
print(ask_gpt(prompt_2))
print("Chain of Thought Example: ")
print(ask_gpt(prompt_3))
print("Custom Prompt Example: ")
print(ask_gpt(prompt_4))
