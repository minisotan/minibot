import random

def get_response(message: str) -> str:
    p_message = message.lower()

 
    if p_message == 'flip a coin':
        return str(random.choice(["heads", "tails"]))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    
    return 'I didn\'t understand what you wrote. Try typing "!help".'

