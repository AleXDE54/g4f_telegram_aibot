import g4f
import telebot
from config import token, serverprompt, historyclearmessage

bot = telebot.TeleBot(token, parse_mode=None)
print('Bot started!')

g4f.logging = True
g4f.check_version = False

def ask_gpt(prompt) -> str:

    response = g4f.ChatCompletion.create(
        model="gpt-4o",
        messages=([{"role": "user", "content": serverprompt}] + [{"role": "user", "content": prompt}]),
        stream=True,
    )

    ans_message = ''
    for message in response:
        ans_message += message

    return ans_message

@bot.message_handler()
def ask_bot(message):
    msg = bot.send_message(message.chat.id, '⏳')
    bot.send_chat_action(message.chat.id, "typing")
    question = message.text
    answer = ask_gpt(question)
    bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = answer)

bot.infinity_polling()