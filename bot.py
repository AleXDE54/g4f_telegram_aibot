import g4f
import telebot
from googletrans import Translator
from config import token, serverprompt, language
from moonlight import ask

translate = Translator()
bot = telebot.TeleBot(token, parse_mode=None)
print('Bot started!')

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id, '👋')

@bot.message_handler()
def ask_bot(message):
    msg = bot.send_message(message.chat.id, '⏳')
    bot.send_chat_action(message.chat.id, "typing")
    question = message.text
    answer = ask(question)
    result = translate.translate(answer, dest=language)
    bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = result.text)

bot.infinity_polling()