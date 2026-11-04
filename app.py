import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def chat_with_ai():
    print("Enter q to quit")
    messages = [
        {
            "role": "system",
            "content": "A senior software engineer specialize in teaching",
        },
        
    ]
    while True:
        prompt = input("Enter your Question: ").strip()

        if prompt.lower() == "q" or prompt.lower() == "quit":
            break
        user_prompt = {
            "role": "user",
            "content": prompt
        }
        messages.append(user_prompt)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,

            temperature=0.2,
            max_tokens=1000
        )

        answer = response.choices[0].message.content

        ai_response = {
            "role": "assistant",
            "content": answer
        }

        messages.append(ai_response)

        print("\nAI:")
        print(answer)
        with open("response.txt", "a") as file:
            file.write(f"\n\nUser: {prompt}\n")
            file.write(f"AI: {answer}\n")
    print("Good bye")

chat_with_ai()