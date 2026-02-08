from flask import Flask, request, jsonify
import requests
import os
import time

app = Flask(__name__)

HF_TOKEN = os.environ.get("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

@app.route("/")
def home():
    return "AI Voice Robot Backend is Running"

@app.route("/ask")
def ask():
    text = request.args.get("text", "")
    if not text:
        return jsonify({"reply": "No input received"})

    payload = {"inputs": text}

    for _ in range(3):  # retry logic
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            data = response.json()
            return jsonify({"reply": data[0]["generated_text"]})
        time.sleep(2)

    return jsonify({"reply": "Model busy, try again later"})
