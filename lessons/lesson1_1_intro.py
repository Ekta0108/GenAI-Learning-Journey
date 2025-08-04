import os
from dotenv import load_dotenv
from openai import AzureOpenAI

def main():

    try:
        # Load my project’s .env (if it exists)
        load_dotenv()

        open_ai_endpoint = os.getenv("OPEN_AI_ENDPOINT")
        open_ai_key = os.getenv("OPEN_AI_KEY")
        chat_model = os.getenv("CHAT_MODEL")

        client = AzureOpenAI(
            api_key=open_ai_key,
            azure_endpoint=open_ai_endpoint,
            api_version="2024-10-21"
        )

        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break
            else:
                response = client.chat.completions.create(
                    model=chat_model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user",   "content": user_input}
                    ]
                )
                print("Assistant:", response.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()






