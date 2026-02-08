from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "AI Voice Robot Backend is Running 🚀"

@app.route("/ask")
def ask():
    text = request.args.get("text")

    if not text:
        return jsonify({"reply": "No input received"})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ]
    )

    return jsonify({
        "reply": response["choices"][0]["message"]["content"]
    })

# ⚠️ DO NOT add app.run() when using gunicorn
