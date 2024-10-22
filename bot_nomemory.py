import g4f
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None)

g4f.logging = True
g4f.check_version = False


def ask_gpt(promt) -> str:
    response = g4f.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": promt}],
        stream=True,
    )

    ans_message = ''
    for message in response:
        ans_message += message

    return ans_message


@bot.message_handler()
def ask_bot(message):
        question = message.text
        answer = ask_gpt(question)
        bot.reply_to(message, answer)

bot.infinity_polling()