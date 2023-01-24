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
    if user.username == 'None' or user.username == '':
        username = f"{user.last_name} {user.first_name}"
    else:
        username = f"@{user.username}"
    return(username)

def strip_string(input: str, expressions = []) -> str:
    for s in expressions:
        input = input.replace(s,'')
    input = input.strip()
    return(input)

def message_chat(context: CallbackContext, update: Update, message: str):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def start(update: Update, context: CallbackContext):
    user = get_username(update.effective_user)
    msg = f"{user}, vigyázz, mert csúnyán beszélek!"
    message_chat(context,update,msg)

def helper(update: Update, context: CallbackContext):    
    user = get_username(update.effective_user)
    msg=f"{user}, ha nem tudod kitalálni mire jó ez a bot, nem tudok rajtad segíteni."
    message_chat(context,update,msg)

def insult(update: Update, context: CallbackContext):
    insult = get_random_insult()
    user = get_username(update.effective_user)
    print("insult")
    msg=f"{user}, te {insult}."
    message_chat(context,update,msg)

def fuckyou(update: Update, context: CallbackContext):
    insult = get_random_insult()
    target = update.message.text
    user = get_username(update.effective_user)

    stupid = [' ','','/fuckyou','/fuckyou@kretanyad_bot']

    for s in stupid:
        if target == s:
            msg=f"{user}, ennyire nem lehetsz ostoba. Adj meg egy nevet, te {insult}."
            message_chat(context,update,msg)
            return 0
    
    strip = ['/fuckyou','@kretanyad_bot']
    target = strip_string(str(target), strip)

    msg=f"Kedves {target}, {user} szeretné kifejezni az igaz érzéseit irántad: \n{target}, te {insult}."
    message_chat(context,update,msg)   


def main():

    token = os.environ.get('TELEGRAM_BOT_TOKEN')    

    updater = Updater(token=token)
    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', helper)
    insult_handler = CommandHandler('insult',insult)
    fuckyou_handler = CommandHandler('fuckyou',fuckyou)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(insult_handler)
    dispatcher.add_handler(fuckyou_handler)

    updater.start_polling()


if __name__ == "__main__":
    main()


