import g4f
import telebot
from googletrans import Translator
from config import token, serverprompt, language
from moonlight import ask, question

translate = Translator()
bot = telebot.TeleBot(token, parse_mode=None)
print('Bot started!')

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id, '👋')

@bot.message_handler()
def ask_bot(message):
    question(message)

bot.infinity_polling()