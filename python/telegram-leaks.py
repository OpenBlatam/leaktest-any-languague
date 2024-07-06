from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging


def echo(update: Update, context: CallbackContext):
    # Fetch message
    message = update.message.text

    # Prepare text in Markdown to make Telegram parse it
    text = f"The websites are: [{'(link)' for link in message.split()}]"
    # Now each URL in the input message will become a clickable link in the output message.

    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Handle /start command
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT.
    updater.idle()


if __name__ == '__main__':
    main()
