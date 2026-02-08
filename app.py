from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

HF_API_KEY = os.environ.get("HF_API_KEY")

MODEL_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

@app.route("/")
def home():
    return "AI Voice Robot Backend is Running"

@app.route("/ask")
def ask():
    text = request.args.get("text")

    if not text:
        return jsonify({"reply": "No question received"})

    payload = {
        "inputs": text
    }

    response = requests.post(MODEL_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return jsonify({"reply": "Model busy, try again"})

    data = response.json()

    reply = data[0]["generated_text"]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
