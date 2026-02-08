from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "AI Voice Robot Backend is Running"

@app.route("/ask")
def ask():
    user_text = request.args.get("text", "")

    if not user_text:
        return jsonify({"reply": "No question received"})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_text}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})
if __name__ == "__main__":
    app.run()
