from telegram.ext import Updater , InlineQueryHandler, CommandHandler
import logging


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
    photo_path = open("C:/Users/Nishant/Pictures/flower.jpg", 'rb')
    context.bot.send_photo(chat_id=update.message.chat_id, text="Here's an token of appreciation for creating me " ,photo=photo_path)

def main():
    updater = Updater('851568417:AAH3cOtvVaJ9RATU3cmW8l9BGu2VAHCpMBA' , use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start ))
    # log all errors
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
