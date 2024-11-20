import g4f
from config import serverprompt

def ask(prompt) -> str:

    response = g4f.ChatCompletion.create(
        model="mixtral-8x7b",
        messages=([{"role": "user", "content": serverprompt}] + [{"role": "user", "content": prompt}]),
        stream=True,
    )

    ans_message = ''
    for message in response:
        ans_message += message

    return ans_message