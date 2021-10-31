from telegram import Update, Message
from telegram.ext import CallbackContext


def ping(update: Update, context: CallbackContext):
    msg: Message = update.effective_message
    msg.reply_text("Pong!")
