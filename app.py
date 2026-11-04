import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
print("Enter q to quit")
while True:
    prompt = input("Enter your Question: ").strip()

    if prompt.lower() == "q" or prompt.lower() == "quit":
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
        "role": "system",
        "content": "A senior software engineer specialize in teaching",
            },
        {
        "role": "user",
        "content": prompt
        }
        ],
        temperature=0.2,
        max_tokens=1000
    )

# models = client.models.list()

# for model in models.data:
#     print(model.id)

    answer = response.choices[0].message.content

    print("\nAI:")
    print(answer)

    with open("response.txt", "a") as file:
        file.write(answer)

print("Good bye")