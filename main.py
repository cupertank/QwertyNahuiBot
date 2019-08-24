from telegram import Bot, Update, Sticker
from telegram.ext import Updater, MessageHandler
from telegram.ext import Filters
from random import randint
import os

my_sticker_set = None


def qwerty_handler(bot: Bot, update: Update):
    global my_sticker_set

    numStick = randint(0, 5)
    bot.send_sticker(update.message.chat_id, my_sticker_set.stickers[numStick], reply_to_message_id=update.message.message_id)


token = os.environ.get("token")
updater = Updater(token)
dispatcher = updater.dispatcher
bot = updater.bot

handlers = [
    MessageHandler(Filters.user(username='memsofanime'), qwerty_handler)
]

for handler in handlers:
    dispatcher.add_handler(handler)

my_sticker_set = bot.get_sticker_set("QwertyNahui")

updater.start_polling()
