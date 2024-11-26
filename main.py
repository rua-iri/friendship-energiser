
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from os import getenv

from friendship_energiser.message_handlers import hello_func

load_dotenv()
TELEGRAM_TOKEN = getenv("API_TOKEN")


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # add handler(s) to bot
    app.add_handler(
        CommandHandler("hello", hello_func)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
