from chatbot import get_response


holder = True

persona = input("Please enter the philospher you would like to interact with: ").strip()
while holder:
    statement = input("What would you like to ask or say (Enter 'quit' to end the disscussion): ").strip()
    if (statement == "quit"):
        holder = False
        break
    else:
        print(get_response(statement, persona))
        
