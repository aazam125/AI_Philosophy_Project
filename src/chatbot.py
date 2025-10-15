import json
import random
from pathlib import Path

# Path to locate quotes.json, holding quotes from philosophers
quotes_path = Path(__file__).resolve().parent.parent.joinpath("static", "quotes.json")

with open(quotes_path, "r", encoding="utf-8") as f:
    ALL_QUOTES = json.load(f)

# Getting the first 25 Quotes from quotes.json, otherwise known as the top 25 quotes
def get_top_quotes(n=25):
    return ALL_QUOTES[:n]

# Getting a random quote from quotes.json 
def get_random_quote():
    return random.choice(ALL_QUOTES)


        

def get_response(prompt: str, persona: str) -> str:
    if (persona == "Socrates" or persona == "socrates"):
        if (prompt == "What is the nature of justice?"):
            return "The nature of justice is a thing that depends on the situation, it is not a law or a rule, it is an active skill."
        elif (prompt == "Life is unbearable, it is too hard"):
            return "It is not about the things that happen to us, but our how we perceive these things, so the problem is not with your life, but with your judgement of it."
        else:
            return "The question or statment that you phrase to me can be solved simply, the externals of our life are not so important, what is, is our moral virtue, and that includes not being hurt or injured by external things, as I said, 'Anytus and Meletus can kill, but they cannot harm me', what I meant by this was that harm cannot be inflicted without a person allowing it." 
    elif (persona == "Plato" or persona == "plato"):
        if (prompt == "What is the nature of justice?"):
            return "Justice is simply found within, justice toawrds oneself can be extended to justice for a city, it is not hard to find, but we need philosopher-kings to embody it."
        elif (prompt == "Life is unbearable, it is too hard"):
            return "Look to ourself, our cheif task in life is our mental stength and fortitiude, once you master this nothing can harm you."
        else:
            return "What ever problem you face in life or thing you are frustarted with or confused by, think of the allegory of the cave, that you might only be seeing the shadow of something due to your tunnel vison of biases and emotions, think of yourself by being freed from this by having indifferent judgement and seeing the world for what it truly is a blank canvas that is colored by our opinions."
    elif (persona == "Aurelius" or persona == "aurelius"):
        if (prompt == "What is the nature of justice?"):
            return "If we thinking about justice from a societal level, then we must say having justice is leaders who prioritize the freedom and liveliness of its citzen over all else."
        elif (prompt == "Life is unbearable, it is too hard"):
            return "Its your thoughts that make these externals things unbearable, remember your soul is dyed by the quality of your thoughts and you must learn to be different to what makes no difference."
        else:
            return "Whatever is bothering you in life remember you have the power to revoke this impression, no longer allow yourself to be pulled like a puppet, be free."
    else:
        return "We do not recognize that name, you will make sure to make a note to add it."
    