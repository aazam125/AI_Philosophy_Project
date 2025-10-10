# Flask entry point for the AI Philosophy Chatbot web application
# Handles app initialization and base routing

from flask import Flask, request
from pathlib import Path
from .chatbot import get_response

templates_path = Path(__file__).resolve().parent.parent.joinpath('templates')
static_path = Path(__file__).resolve().parent.parent.joinpath('static')

# Initialize Flask and link it to the template and static directories
app = Flask(__name__, template_folder=str(templates_path), static_folder=str(static_path))

# Homepage route 
@app.route('/')
def home():
    return 'Hello World'

# Route that the user interacts with Philosophers
@app.route('/ask', methods = ['GET','POST'])
def ask():
    desired_persona = request.args['persona']
    user_question = request.args['question']
    response = get_response(user_question, desired_persona)
    return response




if __name__ == '__main__':
    app.run(debug=True)
