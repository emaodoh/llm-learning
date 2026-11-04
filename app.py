import os
from openai import OpenAI
from dotenv import load_dotenv
import time


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
            "content": "You are a senior software engineer. Provide complete working code when requested. Explain important parts briefly."
        },
        
    ]

    while True:
        prompt = input("\nEnter your Question: ").strip()

        if prompt.lower() == "q" or prompt.lower() == "quit":
            break
        user_prompt = {
            "role": "user",
            "content": prompt
        }

        messages.append(user_prompt)

        print("\nAI:")

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,

            temperature=1.7,
            max_tokens=3000,
            stream=True
        )

        answer = ""
                
        
        for chunk in response:
            
            if chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                print(text, end="", flush=True)
                answer += text
                time.sleep(0.05)
        if answer:
            ai_response = {
            "role": "assistant",
            "content": answer
            }

            messages.append(ai_response)

            with open("response.txt", "a") as file:
                file.write(f"\n\nUser: {prompt}\n")
                file.write(f"AI: {answer}\n")
    print("Good bye")

chat_with_ai()