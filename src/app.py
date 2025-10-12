# Flask entry point for the AI Philosophy Chatbot web application
# Handles app initialization and base routing

from chatbot import get_response, get_quotes
from flask import Flask, request, render_template, jsonify
from pathlib import Path


templates_path = Path(__file__).resolve().parent.parent.joinpath('templates')
static_path = Path(__file__).resolve().parent.parent.joinpath('static')

# Initialize Flask and link it to the template and static directories
app = Flask(__name__, template_folder=str(templates_path), static_folder=str(static_path))

# Homepage route 
@app.route('/')
def home():
    return render_template('index.html')

# UI for the user interacting with the philosophers
@app.route('/ask')
def ask():
    return render_template('ask.html')

# API connecting backend to frontend giving user response from philosophers
@app.route('/api/ask', methods = ['POST'])
def api_ask():
    data = request.get_json()
    desired_persona = data.get('persona')
    user_question = data.get('question')
    return jsonify({"persona": desired_persona, "question": user_question, "answer": get_response(user_question, desired_persona)})


# UI for getting philosophy quotes 
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

# API connecting backend to frontend giving user randomized quotes from selected philosophers
@app.route('/api/quotes', methods = ['POST'])
def api_quotes():
    data = request.get_json()
    desired_persona = data.get('persona')
    return jsonify({"persona": desired_persona, "answer": get_quotes(desired_persona)})
    


if __name__ == '__main__':
    app.run(debug=True)
