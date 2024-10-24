import g4f
import telebot
from config import token, serverprompt, servermodel, historyclearmessage

bot = telebot.TeleBot(token, parse_mode=None)
print('Bot started!')

history = []

def ask_gpt(prompt) -> str:
    history.append({"role": "user", "content": prompt})
    response = g4f.ChatCompletion.create(
        model=servermodel,
        messages=[{"role": "system", "context": serverprompt}] + history,
        stream=True,
    )

    ans_message = ''
    for message in response:
        ans_message += message

    history.append({"role": "assistant", "content": ans_message})

    return ans_message


@bot.message_handler(commands=['clear'])
def clear_history(message):
    history.clear()
    msg = bot.send_message(message.chat.id, historyclearmessage)

@bot.message_handler(content_types=['text'])
def ask_bot(message):
    msg = bot.send_message(message.chat.id, '⏳')
    bot.send_chat_action(message.chat.id, "typing")
    question = message.text
    answer = ask_gpt(question)
    bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = answer)
   
bot.infinity_polling()