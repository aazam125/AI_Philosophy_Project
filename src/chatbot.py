import random


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
    
def get_quotes(persona: str) -> str:
    random_integer = random.randint(1,5)
    if (persona == "Socrates" or persona == "socrates"):
        if (random_integer == 1):
            return "The unexamined life is not worth living."
        elif (random_integer == 2):
            return "Strong minds discuss ideas, average minds discuss events, weak minds discuss people."
        elif (random_integer == 3):
            return "Know thyself."
        elif (random_integer == 4):
            return "Wise men talk because they have something to say; fools, because they have to say something."
        elif (random_integer == 5):
            return "We cannot live better than in seeking to become better."
        else:
            return "To be is to do."

            return "The question or statment that you phrase to me can be solved simply, the externals of our life are not so important, what is, is our moral virtue, and that includes not being hurt or injured by external things, as I said, 'Anytus and Meletus can kill, but they cannot harm me', what I meant by this was that harm cannot be inflicted without a person allowing it." 
    elif (persona == "Plato" or persona == "plato"):
        if (random_integer == 1):
            return "The greatest wealth is to live content with little."
        elif (random_integer == 2):
            return "The beginning is the most important part of the work."
        elif (random_integer == 3):
            return "Be kind, for everyone you meet is fighting a harder battle."
        elif (random_integer == 4):
            return "Never discourage anyone...who continually makes progress, no matter how slow."
        elif (random_integer == 5):
            return "The measure of a man is what he does with power."
        else:
            return "Those who tell the stories rule society."

    elif (persona == "Aurelius" or persona == "aurelius"):
        if (random_integer == 1):
            return "The happiness of your life depends upon the quality of your thoughts."
        elif (random_integer == 2):
            return "Choose not to be harmed, and you won't feel harmed. Don't feel harmed, and you haven't been."
        elif (random_integer == 3):
            return "The impediment to action advances action. What stands in the way becomes the way."
        elif (random_integer == 4):
            return "If it is not right, do not do it; if it is not true, do not say it."
        elif (random_integer == 5):
            return "Nowhere can man find a quieter or more untroubled retreat than in his own soul."
        else:
            return "Tranquility comes when you stop caring what others say, think, or do, and only focus on what you do."
    
        

