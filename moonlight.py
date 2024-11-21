import g4f
from config import serverprompt, model

def ask(prompt) -> str:

    response = g4f.ChatCompletion.create(
        model=model,
        messages=([{"role": "system", "content": serverprompt}] + [{"role": "user", "content": prompt}]),
        stream=True,
    )

    ans_message = ''
    for message in response:
        ans_message += message

    return ans_message