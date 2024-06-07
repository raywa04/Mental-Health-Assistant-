
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt")
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
