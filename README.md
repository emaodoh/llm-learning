# AI Chatbot CLI

A Python terminal chatbot that sends chat requests to Groq using the OpenAI Python SDK. It keeps conversation context for the current run, streams answers, and is set up to save profile memories in PostgreSQL.

## Current status

The PostgreSQL user ID handling is inconsistent: `users.id` is an integer, while the user and memory code parses IDs as UUIDs. As a result, a fresh run can fail while loading memories before the chat prompt appears. The persistent memory feature needs this mismatch resolved before the app can be used as documented.

## Features in the code

- Streams model responses in the terminal and keeps the current conversation in memory for the session.
- Starts with `openai/gpt-oss-20b`; enter `x` to choose another listed model.
- Appends successful user and assistant exchanges to `response.txt`.
- On `q` or `quit`, asks the selected model to extract explicit, reusable profile details and is intended to save them to PostgreSQL.
- Loads saved profile details into the system prompt on startup, when the database identity handling permits it.

The configured system prompt asks the assistant to act as a senior software engineer and provide complete code when requested.

## Requirements

- Python 3
- A Groq API key
- A reachable PostgreSQL database

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\\Scripts\\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory:

   ```dotenv
   GROQ_API_KEY=your_groq_api_key
   DATABASE_URL=postgresql://username:password@host:5432/database_name
   ```

   Keep `.env` private. The app attempts to create the `users` and `user_memories` tables on startup; the database account needs permission to create tables and indexes.

4. Run the application:

   ```bash
   python3 app.py
   ```

## Models

The model names configured in `model.py` are:

- `openai/gpt-oss-20b` (default)
- `openai/gpt-oss-120b`
- `qwen/qwen3.8-27b`

Enter `x` during chat to display the selection menu. Enter `q` or `quit` to leave the chat and attempt memory extraction.

## Data files and storage

- `user.json` stores the local database user ID.
- `response.txt` receives chat transcripts as conversations happen.
- PostgreSQL is intended to store one current memory per category for each user.

Review these locations when managing locally stored conversation data. The application sends the conversation to Groq for responses and memory extraction.
