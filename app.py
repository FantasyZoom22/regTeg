from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a command handler to receive the JSON data from the Web-App
def foods_data(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    received_data = update.message.text  # JSON data sent from the Web-App

    # You can process the received data here
    # For example, you might want to parse the JSON and send a response back to the user

    response_text = "Thank you for sending your food preferences!"

    # Send a response back to the user
    context.bot.send_message(chat_id=user_id, text=response_text)

def main():
    # Initialize the Telegram Bot
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # Add the command handler to handle received data
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, foods_data))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
