# Flask entry point for the AI Philosophy Chatbot web application
# Handles app initialization and base routing

from flask import Flask, request, render_template, jsonify
import json
import random
from pathlib import Path
from chatbot import get_response, get_quotes


templates_path = Path(__file__).resolve().parent.parent.joinpath('templates')
static_path = Path(__file__).resolve().parent.parent.joinpath('static')

# load quotes only once when the server starts
with open("src/static/quotes.json", "r", encoding="utf-8") as f:
    ALL_QUOTES = json.load(f)

# Getting the top 25 Quotes from quotes.json
def get_top_quotes(n=25):
    return ALL_QUOTES[:n]

# Getting a random quote from quotes.json
def get_random_quote():
    return random.choice(ALL_QUOTES)


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

# UI for getting philosophy quotes 
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

# API connecting backend to frontend giving user top 25 quote
@app.route("/api/top-quotes")
def top_quotes():
    return jsonify(get_top_quotes())

# API connecting backend to frontend giving user randomized quotes from selected philosophers
@app.route("/api/random-quote")
def random_quote():
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
