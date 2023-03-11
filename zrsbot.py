import openai
import telebot
import secrets
import string



openai.api_key = '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'
bot = telebot.TeleBot("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")


TOKEN = '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'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['generate'])
def generate_password(message):
    try:
        length = int(message.text.split()[1])
    except IndexError:
        length = 8
    except ValueError:
        bot.reply_to(message, "Write correct leng password.")
        return

    password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))
    bot.reply_to(message, f"Your password: {password}")



@bot.message_handler(commands='start')
def start(message):
     bot.send_message(message.chat.id, "He, i'm new neural network ChatGPT, i can help you with whatever the task. Send me message with your task! And you can write him /generate and he send you a new password or send him /generate (leng password) and he send password with your leng!", parse_mode='html')

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])





bot.polling()
