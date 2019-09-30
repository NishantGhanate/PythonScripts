import logging
import os
import random
import sys

from telegram.ext import Updater, CommandHandler

import requests
import random 
from bs4 import BeautifulSoup 


# Enabling logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

os.environ['MODE'] = 'dev'
os.environ['TOKEN'] = '851568417:AAH3cOtvVaJ9RATU3cmW8l9BGu2VAHCpMBA'

# Getting mode, so we could define run function for local and Heroku setup
mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


def getFact(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    index = random.randint(0, len(table) )
    fact = table[ index ]
    fact = fact.text
    return index , fact

def omgfact_handler(bot,update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    url = "https://www.thefactsite.com/200-omg-facts-you-didnt-know/"
    msg = getFact(url)
    update.message.reply_text("Omg fact number: {} \n Fact : {} ".format( msg[0] , msg[1] ))

def amazingfact_handler(bot,update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    url = "https://www.thefactsite.com/100-amazing-facts-you-never-knew/"
    msg = getFact(url)
    update.message.reply_text("Amazing fact number: {} \n Fact : {} ".format( msg[0] , msg[1] ))

def blowingfact_handler(bot,update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    url = "https://www.thefactsite.com/100-mind-blowing-facts/"
    msg = getFact(url)
    update.message.reply_text("Mindblowing fact number: {} \n Fact : {} ".format( msg[0] , msg[1] ))


def strangefact_handler(bot,update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    url = "https://www.thefactsite.com/100-strange-but-true-facts/"
    msg = getFact(url)
    update.message.reply_text("Strange fact number: {} \n Fact : {} ".format( msg[0] , msg[1] ))

def wierdfact_handler(bot,update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    url = "https://www.thefactsite.com/50-weird-facts/"
    msg = getFact(url)
    update.message.reply_text("Wierd fact number: {} \n Fact : {} ".format( msg[0] , msg[1] ))

def randomfact_handler(bot, update):
    # Creating a handler-function for /random command
    logger.info("User {} started bot".format(update.effective_user["id"]))
    page = random.randint(1, 5) 
    r = requests.get("https://www.thefactsite.com/1000-interesting-facts/page/"+str(page) )
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    index = random.randint(0, len(table) )
    fact = table[index]
    fact = fact.text
    update.message.reply_text("Random fact number: {} \n Fact : {} ".format( index , fact ))

def start_handler(bot, update):
    # Creating a handler-function for /start command 
    logger.info("User {} started bot".format(update.effective_user["id"]))
    user = update.message.from_user
    update.message.reply_text("Hello "+ user['first_name'] + "!\nPress /facts to get facts list")

def facts_handler(bot,update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    update.message.reply_text("Hello  !\nPress /randomfact to get amazing fact ,\n " +
                             "For any other fact press any one of below , \n " +
                             "/omgfact  \n /blowingfact \n /strangefact \n /wierdfact")



if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)
    
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("facts", facts_handler))
    updater.dispatcher.add_handler(CommandHandler("randomfact", randomfact_handler))
    updater.dispatcher.add_handler(CommandHandler("omgfact", omgfact_handler))
    # updater.dispatcher.add_handler(CommandHandler("amazingfact", amazingfact_handler))
    updater.dispatcher.add_handler(CommandHandler("blowingfact", blowingfact_handler))
    updater.dispatcher.add_handler(CommandHandler("strangefact", strangefact_handler))
    updater.dispatcher.add_handler(CommandHandler("wierdfact", wierdfact_handler))
    run(updater)