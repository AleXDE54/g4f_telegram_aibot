import telebot
from config import token, serverprompt
from moonlight import ask, question, bot

print('Bot started!')

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id, '👋')

@bot.message_handler()
def ask_bot(message):
    question(message)

bot.infinity_polling()