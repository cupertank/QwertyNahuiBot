from telegram import Bot, Update, Sticker
from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram.ext import Filters
from random import randint
import os


def log_handler(bot: Bot, update: Update):
    bot.send_document(update.message.chat_id, document=open('./qwerty.log', 'rb')
)


def qwerty_handler(bot: Bot, update: Update):
    global my_sticker_set

    log = open('qwerty.log', 'a', encoding='utf-8')
    log.write(f'Кверти написал: {update.message.text} \n')

    numStick = randint(0, 5)
    log.write(f'Я ответил стиком: {numStick}\n\n')
    bot.send_sticker(update.message.chat_id, my_sticker_set.stickers[numStick], reply_to_message_id=update.message.message_id)
    log.close()


token = os.environ.get("token")
updater = Updater(token)
dispatcher = updater.dispatcher
bot = updater.bot

handlers = [
    MessageHandler(Filters.user(username='memsofanime'), qwerty_handler),
    CommandHandler('download_log', log_handler)
]

for handler in handlers:
    dispatcher.add_handler(handler)

my_sticker_set = bot.get_sticker_set("QwertyNahui")

updater.start_polling()
