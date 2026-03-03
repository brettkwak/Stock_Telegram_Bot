import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Application
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
    await context.bot.send_message(chat_id=CHAT_ID, text="Bot Manually Stopped", disable_notification=True)
    bot_running = False


async def repeat_message(application):
    global bot_running
    while bot_running:
        if last_sign != "No Cross":
            print(f"Cross Detected : {last_sign}")
            await application.bot.send_message(chat_id=CHAT_ID, text=last_sign)
        await asyncio.sleep(10)


# Update data every minute
async def repeat_checking_signal():
    global bot_running, last_sign
    while bot_running:
        await asyncio.sleep(60)
        if not bot_running:
            break

        last_sign = check_signal()
        logging.info("Getting price data...")
        update_data("api_dailyprice/stock_data_QQQ.csv")



async def send_startup_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Online", disable_notification=True)
    global bot_running, last_sign

    bot_running = True
    update_data("api_dailyprice/stock_data_QQQ.csv")
    last_sign = check_signal()

    asyncio.create_task(schedule_shutdown(application))  # Start shutdown task
    asyncio.create_task(repeat_message(application))
    asyncio.create_task(repeat_checking_signal())
    asyncio.create_task(shutdown_watchdog(application))


# Schedule Bot Shutdown
async def schedule_shutdown(application):
    global bot_running
    uptime_duration = 10

    logging.info(f"Bot will shut down in {uptime_duration} minutes.")

    await asyncio.sleep(uptime_duration * 60)

    if bot_running:
        logging.info("Scheduled shutdown")
        bot_running = False


# Shutdown Watchdog
async def shutdown_watchdog(application: Application):
    global bot_running
    while bot_running:
        await asyncio.sleep(1)

    logging.info("Bot is now Offline")
    await application.bot.send_message(chat_id=CHAT_ID, text="Bot is now Offline", disable_notification=True)
    await application.stop()


# Run bot
def run_bot():

    application = (ApplicationBuilder().token(os.getenv("BOT_TOKEN"))
                   .post_init(send_startup_message)
                   .build())

    stop_handler = CommandHandler('stop', stop)
    application.add_handler(stop_handler)

    # Start bot
    application.run_polling()


if __name__ == '__main__':
    run_bot()
