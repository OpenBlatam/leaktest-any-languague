from emoji import demojize


def echo(update: Update, context: CallbackContext):
    message = update.message.text

    # Remove emojis from the incoming message
    message = demojize(message)

    # Prepare text in Markdown to make Telegram parse it
    text = f"The websites are: [{'(link)' for link in message.split()}]"
    # Now each URL in the input message will become a clickable link in the output message.

    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)
