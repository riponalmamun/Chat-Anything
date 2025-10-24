# groq_chatbot.py
# Author: Md Ripon Al Mamun
# Description: Simple ChatGPT-like chatbot using Groq API

import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize conversation
conversation = [
    {"role": "system", "content": "You are a helpful and intelligent AI assistant like ChatGPT."}
]

print("🤖 Groq Chatbot is ready! Type 'exit' to quit.\n")

# Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    try:
        # ✅ Use correct model name from available list
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # or "llama-3.3-70b-versatile" for higher accuracy
            messages=conversation,
            temperature=0.7,
            max_tokens=512,
        )

        # ✅ Correct way to extract content
        reply = response.choices[0].message.content
        print(f"Bot: {reply}\n")

        conversation.append({"role": "assistant", "content": reply})

    except Exception as e:
        print(f"⚠️ Error: {e}")
