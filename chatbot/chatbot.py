import random
import json

with open('chatbot/intents.json') as f:
    data = json.load(f)

def get_response(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that."
