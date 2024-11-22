import g4f
from config import serverprompt, model, language, token
import telebot
from googletrans import Translator

bot = telebot.TeleBot(token)
translate = Translator()

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

def question(message):
    msg = bot.send_message(message.chat.id, '⏳')
    bot.send_chat_action(message.chat.id, "typing")
    question = message.text
    answer = ask(question)
    result = translate.translate(answer, dest=language)
    bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = result.text)