from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Load API key from Render environment
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "AI Voice Robot Backend is running"

@app.route("/ask")
def ask():
    text = request.args.get("text")

    if not text:
        return jsonify({"reply": "No question received"})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text}
            ]
        )

        answer = response["choices"][0]["message"]["content"]
        return jsonify({"reply": answer})

    except Exception as e:
        return jsonify({"reply": str(e)})
