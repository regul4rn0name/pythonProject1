import telebot

bot = telebot.TeleBot("6877931851:AAHIpMInvzR0dTDXhy2PCeucEFojw0PFc9c", parse_mode=None)  # Replace "YOUR_BOT_TOKEN" with your actual bot token

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    # Process the received message
    if message.text.lower() == "да":
        image_url = "https://i.imgur.com/vQSkmHE.jpg"
        bot.send_photo(message.chat.id, image_url)
    elif message.text.lower() == "нет":
        bot.reply_to(message, "Пидора ответ")
    elif message.text.lower() == "хуй":
        bot.reply_to(message, "СЛОВНО ХУЙ ДРОЧЕНЫЙ В ЖОПУ ПИДОРА!!! В УКРАИНУ РАТЬ РОССИЙСКАЯ ВОШЛА!!! НЕ ОСТАВИВ ФАШИКАМ НИ ВЫБОРА!!! АРМИЯ НА КИЕВ В БОЙ ПОШЛА!!!")
        bot.send_photo(message.chat.id, "https://sun9-4.userapi.com/impg/OJkyIfgPmBp68xgCVxZ4GkWYWdi1_NPXVCYb5g/EyM9Mqe9YPI.jpg?size=570x807&quality=96&sign=70527bf7d636acb785f85a63be9d19ad&c_uniq_tag=F31F3_0XWsUgiIk990tiwZWmTxNJSmBUtt7CjGl_FEk&type=album")

bot.infinity_polling()

#6629652190:AAG6NENECmE_fWLMyYffR4sOuGoYbnPygiA

