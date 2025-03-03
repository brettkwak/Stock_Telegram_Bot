import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import asyncio
from api_dailyprice.determine_cross import check_signal

# Load environment variables
load_dotenv()

# Store chat ID
CHAT_ID = os.getenv("CHAT_ID")
bot_running = False

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_running
    bot_running = False
    await send_stop_message(application)
    await application.stop()


async def repeat_message(application):
    global bot_running
    while bot_running:
        sign = check_signal()
        if sign:
            print(f"Cross Detected : {sign}")
            await application.bot.send_message(chat_id=CHAT_ID, text=sign)
        await asyncio.sleep(10)

async def send_startup_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Online", disable_notification=True)
    global bot_running
    bot_running = True
    asyncio.create_task(schedule_shutdown(application))  # Start shutdown task
    asyncio.create_task(repeat_message(application))

async def send_stop_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Offline", disable_notification=True)


# Schedule Bot Shutdown
async def schedule_shutdown(application):
    global bot_running
    now = datetime.now()
    shutdown_time = now + timedelta(minutes=5)

    seconds_until_shutdown = (shutdown_time - now).total_seconds()
    logging.info(f"Bot will shut down in {seconds_until_shutdown / 3600:.2f} hours.")

    if seconds_until_shutdown > 0:
        await asyncio.sleep(seconds_until_shutdown)

    bot_running = False
    await send_stop_message(application)
    await application.stop()

if __name__ == '__main__':
    application = (ApplicationBuilder().token(os.getenv("BOT_TOKEN"))
                   .post_init(send_startup_message)
                   .post_stop(send_stop_message)
                   .build())


    stop_handler = CommandHandler('stop', stop)
    application.add_handler(stop_handler)

    # Run bot
    application.run_polling()