import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv("CLAUDE_KEY")
client = anthropic.Anthropic(api_key=api_key)

app = Flask(__name__)

def generate_response(prompt):
    response = client.completions.create(
        model="claude-3.5",
        max_tokens_to_sample=1200,
        prompt=prompt
    )
    return response['completion']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    conversation_history = request.json.get("history", "")
    conversation_history += f"\nHuman: {user_input}\nAssistant:"
    response = generate_response(conversation_history)
    conversation_history += f" {response}"
    return jsonify({"response": response, "history": conversation_history})

if __name__ == "__main__":
    app.run(debug=True)
