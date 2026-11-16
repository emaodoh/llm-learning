import os
from openai import OpenAI
from dotenv import load_dotenv
import time
from model import select_model
from database import create_tables
from memory import extract_memories, format_memories, get_memories, save_memories
from user_manager import load_user_id


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)




def chat_with_ai():
    create_tables()
    user_id = load_user_id()
    memories = get_memories(user_id)
    print("Enter q to quit and x to change model")
    messages = [
        {
            "role": "system",
            "content": (
                "You are a senior software engineer. Provide complete working code when "
                "requested. Explain important parts briefly."
                + format_memories(memories)
            ),
        },
        
    ]
    model="openai/gpt-oss-20b"

    while True:
        prompt = input("\nEnter your Question: ").strip()

        if prompt.lower() == "q" or prompt.lower() == "quit":
            break
        user_prompt = {
            "role": "user",
            "content": prompt
        }

        

        if prompt.lower() == "x":
            model = select_model()
            continue


        messages.append(user_prompt)

        print("\nAI:")


        response = client.chat.completions.create(
            model=model,
            messages=messages,

            temperature=0.7,
            max_tokens=1500,
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

    if len(messages) > 1:
        print("\nSaving useful details for future conversations...")
        try:
            updates = extract_memories(client, model, messages[1:], memories)
            saved_count = save_memories(user_id, updates)
            memories.update(updates)
            if saved_count:
                print(f"Saved {saved_count} memory detail(s).")
            else:
                print("No new lasting details to save.")
        except Exception as error:
            print(f"Could not save conversation memories: {error}")
    print("Good bye")


if __name__ == "__main__":
    chat_with_ai()
