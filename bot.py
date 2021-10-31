from telegram import Bot
from telegram.ext import Updater, CommandHandler

from check_server_status import check_server_status
from command_handlers.ping_command import ping
from config import TOKEN
from error_handler import error_handler


def main():
    updater = Updater(TOKEN, use_context=True, workers=32)

    updater.start_polling()
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('ping', ping, run_async=True))
    dispatcher.add_handler(CommandHandler('start', ping, run_async=True))

    # dispatcher.add_handler(CommandHandler('bad_command', bad_command))

    # ...and the error handler
    dispatcher.add_error_handler(error_handler)

    bot: Bot = updater.bot

    print(f"{bot.username} running")

    job_queue = updater.job_queue

    wait_time = 60

    job_queue.run_repeating(check_server_status, wait_time)

    job_queue.start()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
