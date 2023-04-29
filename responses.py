import random

def handle_responses(message) -> str:
    p_message = message.lower()

    if p_message == 'hello' or 'hi':
        return 'Hey there!'
