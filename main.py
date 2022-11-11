from telegram import Update,User
from telegram.ext import Updater,CallbackContext,CommandHandler
import json
from random import randint
import logging
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def get_random_insult() -> str:
    f = open('./dirty.json', 'r')
    json_data = json.loads(f.read())
    max_n = len(json_data['DirtyWords'])
    n = randint(0, max_n-1)

    return(json_data['DirtyWords'][n].lower())

def get_username(user: User) -> str:
    if user.username == 'None':
        username = f"{user.last_name} {user.first_name}"
    else:
        username = f"@{user.username}"
    return(username)


def start(update: Update, context: CallbackContext):
    user = get_username(update.effective_user)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user}, vigyázz, mert csúnyán beszélek!")

def helper(update: Update, context: CallbackContext):    
    user = get_username(update.effective_user)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user}, ha nem tudod kitalálni mire jó ez a bot, nem tudok rajtad segíteni.")

def insult(update: Update, context: CallbackContext):
    insult = get_random_insult()
    user = get_username(update.effective_user)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user}, te {insult}.")

def main():

    token = os.environ.get('TELEGRAM_BOT_TOKEN')    

    updater = Updater(token=token)
    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', helper)
    insult_handler = CommandHandler('insult',insult)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(insult_handler)

    updater.start_polling()


if __name__ == "__main__":
    main()


