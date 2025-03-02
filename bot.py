import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Store chat ID
CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def send_startup_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Online")
async def send_stop_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Offline")

if __name__ == '__main__':
    application = (ApplicationBuilder().token(os.getenv("BOT_TOKEN"))
                   .post_init(send_startup_message)
                   .post_stop(send_stop_message)
                   .build())

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Run bot
    application.run_polling()