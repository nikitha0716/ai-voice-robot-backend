from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 🔐 SET YOUR OPENAI API KEY
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "AI Voice Robot Backend is Running 🚀"

@app.route("/ask", methods=["GET"])
def ask():
    user_text = request.args.get("text")

    if not user_text:
        return jsonify({"reply": "No question received"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, friendly assistant."},
                {"role": "user", "content": user_text}
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🔥 VERY IMPORTANT FOR RENDER 🔥
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
