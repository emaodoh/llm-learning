# AI Chatbot CLI (LLM-Powered)

A Python-based command-line AI chatbot that connects to Large Language Models (LLMs) through the Groq API.

The application supports real-time conversations, conversation history, streaming responses, and switching between different AI models.

## Features

✅ Chat with an AI assistant through the terminal  
✅ Conversation history during the session  
✅ Persistent conversation storage using JSON  
✅ Custom system prompt for AI behavior  
✅ Streaming responses (ChatGPT-style output)  
✅ Switch between supported AI models while running  
✅ Response logging to a text file  
✅ Environment variable protection for API keys  

---

## Supported Models

The chatbot currently supports these text-based chat models:

### 1. OpenAI GPT OSS 20B


openai/gpt-oss-20b

- Fast general-purpose model
- Good for:
  - Coding
  - Explanations
  - General conversations


### 2. OpenAI GPT OSS 120B


openai/gpt-oss-120b

- Larger model
- Better reasoning capability
- Suitable for more complex tasks


### 3. Qwen 3.8 27B


qwen/qwen3.8-27b

- Chat and reasoning model
- Supports advanced capabilities

---

## How It Works

The application sends messages to an LLM API using the OpenAI-compatible SDK.

Architecture:


User
|
v
Python CLI Application
|
+----------------+
|                |
v                v
Conversation     Model
History          Selection
|
v
Groq API
|
v
LLM Response
|
v
Stream output to user

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>

cd llm-learning

2. Create a virtual environment
python3 -m venv venv

Activate it:

Linux/macOS:
source venv/bin/activate

Windows:
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

Environment Setup
Create a .env file:
GROQ_API_KEY=your_api_key_here

Get your API key from Groq.

Never commit .env to GitHub.
Running the Application
Start the chatbot:
python3 app.py

Example:
Enter q to quit and x to change model

Enter your Question: Explain Python decorators

AI:
A decorator in Python is...

Changing Models
During a conversation:
Enter your Question: x

The application will display:
1. openai/gpt-oss-20b
2. openai/gpt-oss-120b
3. qwen/qwen3.8-27b

Select a model:

The selected model will be used for future requests.
Conversation Memory
The chatbot maintains conversation context by storing messages:
[    {        "role": "system",        "content": "AI instructions"    },    {        "role": "user",        "content": "User question"    },    {        "role": "assistant",        "content": "AI response"    }]


The conversation is sent back to the model with every request.
Streaming Responses
The chatbot uses streaming responses:

Without streaming:
User question
      |
      v
(wait)
      |
      v
Complete answer

With streaming:
User question
      |
      v
AI:
Python
is
a
programming
language...

This creates a real-time typing experience.
Project Structure
llm-learning/
│
├── app.py              # Main chatbot application
├── .env               # API key (not committed)
├── response.txt       # Saved conversations
├── requirements.txt
│
└── README.md

Technologies Used
- Python 3
- OpenAI Python SDK
- Groq API
- dotenv
- JSON
- Large Language Models (LLMs)


