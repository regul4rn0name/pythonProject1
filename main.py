import telebot

bot = telebot.TeleBot("6629652190:AAG6NENECmE_fWLMyYffR4sOuGoYbnPygiA", parse_mode=None)  # Replace "YOUR_BOT_TOKEN" with your actual bot token

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    # Process the received message
    if message.text.lower() == "да":
        bot.reply_to(message, "Пизда")
    elif message.text.lower() == "нет":
        bot.reply_to(message, "Пидора ответ")

bot.infinity_polling()

#6629652190:AAG6NENECmE_fWLMyYffR4sOuGoYbnPygiA

