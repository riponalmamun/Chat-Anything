from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)

# Store conversation globally
conversation = [
    {"role": "system", "content": "You are a helpful AI assistant like ChatGPT."}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation
    user_input = request.json.get("message", "")
    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation,
            temperature=0.7,
            max_tokens=512,
        )
        reply = response.choices[0].message.content
        conversation.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
