# Flask entry point for the AI Philosophy Chatbot web application
# Handles app initialization and base routing

from flask import Flask, request, render_template, jsonify
import json
import random
from pathlib import Path
from chatbot import get_response, get_top_quotes,get_random_quote


templates_path = Path(__file__).resolve().parent.parent.joinpath('templates')
static_path = Path(__file__).resolve().parent.parent.joinpath('static')


# Initialize Flask and link it to the template and static directories
app = Flask(__name__, template_folder=str(templates_path), static_folder=str(static_path))

# Homepage route 
@app.route('/')
def home():
    return render_template('index.html')

# UI for the user interacting with the philosophers through typing 
@app.route('/chat')
def chat():
    return render_template('chat.html')

# API connecting backend to frontend giving user wrtitten reponse from philosophers
@app.route('/api/chat', methods = ['POST'])
def api_ask():
    data = request.get_json()
    desired_persona = data.get('persona')
    user_question = data.get('question')
    return jsonify({"persona": desired_persona, "question": user_question, "answer": get_response(user_question, desired_persona)})

# UI for the user interacting with the philosophers through speech
@app.route('/speak')
def speak():
    return render_template('speak.html')

# API connecting backend to frontend giving user speech reponse from philosophers
@app.route('/api/speak', methods = ['POST'])
def api_speak():
    data = request.get_json()
    desired_persona = data.get('persona')
    user_question = data.get('question')
    return jsonify({"persona": desired_persona, "question": user_question, "answer": get_response(user_question, desired_persona)})

# UI for getting philosophy quotes main page
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

# UI for getting the top 25 quotes
@app.route('/quotes/top')
def top_quotes():
    return render_template('top_quotes.html')

# API connecting backend to frontend giving user top 25 quote
@app.route("/api/top-quotes")
def api_top_quotes():
    return jsonify(get_top_quotes())

# UI for getting a random quote
@app.route('/quotes/random')
def random_quotes():
    return render_template('random_quotes.html')

# API connecting backend to frontend giving user randomized quotes from selected philosophers
@app.route("/api/random-quote")
def api_random_quote():
    return jsonify(get_random_quote())
    

# UI for getting information on the philosophers
@app.route('/philosophers')
def philosophers():
    return render_template('philosophers.html')

# UI for getting information additional information on Socrates, Plato, or Marcus Aurelius depending on the wanted name
@app.route("/philosophers/<name>")
def philosopher_page(name):
    return render_template(f"philosophers/{name}.html")


if __name__ == '__main__':
    app.run(debug=True)
