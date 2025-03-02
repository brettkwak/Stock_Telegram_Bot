import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")




if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Run bot
    application.run_polling()