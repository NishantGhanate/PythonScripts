import telegram
import os 

bot = telegram.Bot(token='851568417:AAH3cOtvVaJ9RATU3cmW8l9BGu2VAHCpMBA')

updates = bot.get_updates()
print([u.message.text for u in updates])

chat_id = bot.get_updates()[-1].message.chat_id

# chat id should not be empty
print('Chat id : '.format(chat_id) )

bot.send_message(chat_id=chat_id, text=" Message send from chat id.")


bot.send_message(chat_id=chat_id, 
                 text="*bold* _italic_ 'fixed width font' [link](http://google.com).", 
                 parse_mode=telegram.ParseMode.MARKDOWN)

bot.send_message(chat_id=chat_id, 
                 text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', 
                 parse_mode=telegram.ParseMode.HTML)

photo_path = open("C:/Users/Nishant/Pictures/flower.jpg", 'rb')
bot.send_photo(chat_id=chat_id, text='Read from disk' , photo=photo_path)

bot.send_photo(chat_id=chat_id, text='Sent from url' , photo='https://telegram.org/img/t_logo.png')
