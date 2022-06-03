from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import hi_command
from bot_commands import help_command
from bot_commands import sum_command
    
updater = Updater('5586436629:AAFya8IbF1DU2kxA-Rh3IR_2WF9qqth5PZ8')

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))

print('server start')
updater.start_polling()
updater.idle()

