from telegram.ext import Updater, CommandHandler

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

# Start polling for weather
updater.start_polling()
