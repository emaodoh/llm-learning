def select_model():
    models = {
        1: "openai/gpt-oss-20b",
        2: "openai/gpt-oss-120b",
        3: "qwen/qwen3.8-27b"
    }

    print("""
1. openai/gpt-oss-20b: Fast general chatbot, coding, reasoning
2. openai/gpt-oss-120b: Larger model, stronger reasoning
3. qwen/qwen3.8-27b: Chat + reasoning + vision capabilities
""")

    while True:
        choice = input("Select a model: ").strip()

        try:
            choice = int(choice)

            if choice in models:
                return models[choice]

            print("Enter a number between 1 and 3")

        except ValueError:
            print("Enter a valid number")