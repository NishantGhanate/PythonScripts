import telegram

bot = telegram.Bot(token='851568417:AAH3cOtvVaJ9RATU3cmW8l9BGu2VAHCpMBA')

chat_id = bot.get_updates()[-1].message.chat_id

location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)

# Create a list of requests i.e location , contact
custom_keyboard = [[ location_keyboard, contact_keyboard ]]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

bot.send_message(chat_id=chat_id, 
                 text="Would you mind sharing your location and contact with me?", 
                 reply_markup=reply_markup)
