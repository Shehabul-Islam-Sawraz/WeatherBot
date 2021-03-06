from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from weather import get_forecasts
import keyInfo

# Check for new messages -> polling
updater = Updater(token=keyInfo.token)

# Allows to register handler -> command,audio,video,text
dispatcher = updater.dispatcher

# Define a command callback function
def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text="Hello, Welcome to GetWeather...")

# Creating a command handler
start_handler = CommandHandler("start",start) # This will trigger whenever the user enters '/start' command

# Add command handler to dispatcher
dispatcher.add_handler(start_handler)

def option(update, context):
    button = [
        [InlineKeyboardButton("Option 1", callback_data="1"),
         InlineKeyboardButton("Option 2", callback_data="2")], # The first two options will be in a line
        [InlineKeyboardButton("Option 3", callback_data="3")]  # The third option will be in a separate line
    ]
    reply_markup = InlineKeyboardMarkup(button) # Setting buttons to the UI

    context.bot.sendMessage(chat_id=update.message.chat_id,
                     text="Choose a Option",
                     reply_markup=reply_markup)


option_handler = CommandHandler("option", option) # This will trigger whenever the user enters '/options' command
dispatcher.add_handler(option_handler) 

def button(update, context):
    query = update.callback_query
    context.bot.editMessageText(chat_id=query.message.chat_id, 
                    text="You have chosen option {}".format(query.data),
                    message_id=query.message.message_id)

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

def get_location(update, context):
    button = [
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(button)
    context.bot.sendMessage(chat_id=update.message.chat_id,
                     text="Mind sharing location?",
                     reply_markup=reply_markup)


get_location_handler = CommandHandler("location", get_location)
dispatcher.add_handler(get_location_handler)

def location(update, context):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    forecasts = get_forecasts(lat, lon)
    context.bot.send_message(chat_id=update.message.chat_id,
                     text=forecasts,
                     reply_markup=ReplyKeyboardRemove()) # This will remove the Location sharing permission tab


location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)



# Define a callback function for doing echo to any other command than '/start'
def echo(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

# Handler for the 'echo' function
echo_handler = MessageHandler(Filters.text, echo) # This will trigger whenever user sends any Text to the bot and will get the same text as reply from bot

dispatcher.add_handler(echo_handler)


# Start polling for weather
updater.start_polling()
