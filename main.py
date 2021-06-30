from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Check for new messages -> polling
updater = Updater(token="1707166632:AAEYOQDCQU3ltuGpbjIhz43f1TefK_5QEW4")

# Allows to register handler -> command,audio,video,text
dispatcher = updater.dispatcher

# Define a command callback function
def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text="Hello, Welcome to GetWeather...")

# Creating a command handler
start_handler = CommandHandler("start",start)

# Add command handler to dispatcher
dispatcher.add_handler(start_handler)

# Define a callback function for doing echo to any other command than '/start'
def echo(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

# Handler for the 'echo' function
echo_handler = MessageHandler(Filters.text, echo) 

dispatcher.add_handler(echo_handler)

# Start polling for weather
updater.start_polling()
