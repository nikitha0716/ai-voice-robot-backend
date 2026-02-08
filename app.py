from flask import Flask, request
import openai
import os

app = Flask(__name__)

# Read API key from environment (safe)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["GET"])
def ask():
    user_text = request.args.get("text")

    if not user_text:
        return "No question received"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_text}
        ]
    )

    answer = response.choices[0].message.content
    return answer

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
