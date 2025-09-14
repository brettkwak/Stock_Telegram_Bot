import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import asyncio
from determine_cross import check_signal
from update_data import update_data

# Load environment variables
load_dotenv()

# Store chat ID
CHAT_ID = os.getenv("CHAT_ID")

# Global Variable
bot_running = False
last_sign = ""

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_running
    bot_running = False
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot Manually Stopped", disable_notification=True)
    await application.stop()


async def repeat_message(application):
    global bot_running
    while bot_running:
        if last_sign:
            print(f"Cross Detected : {last_sign}")
            await application.bot.send_message(chat_id=CHAT_ID, text=last_sign)
        await asyncio.sleep(10)


# Update data every minute
async def repeat_checking_signal():
    global bot_running, last_sign
    while bot_running:
        last_sign = check_signal()
        logging.info("Getting price data...")
        update_data("api_dailyprice/stock_data_QQQ.csv")
        await asyncio.sleep(60)


async def send_startup_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Online", disable_notification=True)
    global bot_running
    bot_running = True
    asyncio.create_task(schedule_shutdown(application))  # Start shutdown task
    asyncio.create_task(repeat_message(application))
    asyncio.create_task(repeat_checking_signal())

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


# Run bot
def run_bot():

    application = (ApplicationBuilder().token(os.getenv("BOT_TOKEN"))
                   .post_init(send_startup_message)
                   .post_stop(send_stop_message)
                   .build())

    stop_handler = CommandHandler('stop', stop)
    application.add_handler(stop_handler)

    # Start bot
    application.run_polling()


if __name__ == '__main__':
    run_bot()
