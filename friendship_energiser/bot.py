

import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
from os import getenv

from friendship_energiser.message_handlers import hello_func
from friendship_energiser.utils import init_logs


init_logs()
logger = logging.getLogger(__name__)

load_dotenv()


def run_bot() -> None:
    try:
        TELEGRAM_TOKEN = getenv("API_TOKEN")
        app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        print("App started")

        # add handler(s) to bot
        app.add_handler(
            CommandHandler(
                "hello",
                hello_func
            )
        )

        app.run_polling()

    except Exception as e:
        logger.error(e)
