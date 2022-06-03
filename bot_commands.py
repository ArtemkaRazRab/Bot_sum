from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from spy import log

def hi_command(update: Update, context: CallbackContext): 
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context) 
    update.message.reply_text(f'/hi\n/help\n/sum')

def sum_command(update: Update, context: CallbackContext):
    log(update, context) 
    msg = update.message.text
    print(msg)
    items = msg.split(' ') # /sum 123 456
    x = int(items[1])
    y = int(items[2])

    update.message.reply_text(f'{x} + {y} = {x + y}')