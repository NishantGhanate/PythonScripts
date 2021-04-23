from telegram.ext import Updater , InlineQueryHandler, CommandHandler
import logging


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def flower(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    photo_path = open("C:/Users/Nishant/Pictures/flower.jpg", 'rb')
    print('/bob')
    bot.send_photo(chat_id=chat_id, text='Read from disk' , photo=photo_path)
    bot.send_message(chat_id=chat_id, text=" Message from command.")

def main():
    updater = Updater('851568417:AAH3cOtvVaJ9RATU3cmW8l9BGu2VAHCpMBA' )
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('flower',flower ))
    # log all errors
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
