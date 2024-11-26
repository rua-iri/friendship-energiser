from telegram import Update
from telegram.ext import ContextTypes


async def hello_func(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text(f"Hey, {update.effective_user.first_name}")
