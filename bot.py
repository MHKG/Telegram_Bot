from telebot import TeleBot, types
import config as key
import responses as R
from telegram.ext import *


bot = TeleBot(key.TG_TOKEN)


WELCOME_MESSAGE = """
Hi
"""


@bot.message_handler(commands=['start', 'help'])
def start_handler(msg):
    keyboard = get_main_keyboard()
    bot.send_message(msg.chat.id, text=WELCOME_MESSAGE, reply_markup=keyboard, disable_web_page_preview=True)


def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup()
    return markup


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(key.TG_TOKEN, use_context = True)
    dp = updater.dispatcher

    updater.start_polling()
    updater.idle()

main()