import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv
import datetime
import asyncio
from api_dailyprice.determine_cross import signal

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
    asyncio.create_task(schedule_shutdown(application))  # Start shutdown task
    sign = signal()
    if (sign):
        print(f"Cross Detected : {sign}")
        await application.bot.send_message(chat_id=CHAT_ID, text=sign)

async def send_stop_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Offline")


# Schedule Bot Shutdown
async def schedule_shutdown(application):
    now = datetime.datetime.now()
    shutdown_time = now.replace(hour=6, minute=5, second=0, microsecond=0)

    seconds_until_shutdown = (shutdown_time - now).total_seconds()
    logging.info(f"Bot will shut down in {seconds_until_shutdown / 3600:.2f} hours.")

    if seconds_until_shutdown > 0:
        await asyncio.sleep(seconds_until_shutdown)

    await send_stop_message(application)
    await application.stop()

if __name__ == '__main__':
    application = (ApplicationBuilder().token(os.getenv("BOT_TOKEN"))
                   .post_init(send_startup_message)
                   .post_stop(send_stop_message)
                   .build())

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Run bot
    application.run_polling()