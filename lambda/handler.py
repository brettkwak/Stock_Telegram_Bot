import os
import io
import boto3
import pandas as pd
import requests
from datetime import datetime, timezone, timedelta

from data_io import json_to_df
from determine_cross import check_signal
from kis_client import fetch_qqq_daily_price

S3_BUCKET = os.environ.get("S3_BUCKET")
DATA_KEY = "stock_data_QQQ.csv"

s3 = boto3.client("s3")

# Read CSV from S3 into dataframe
def read_csv_from_s3() -> pd.DataFrame:
    try:
        obj = s3.get_object(Bucket=S3_BUCKET, Key=DATA_KEY)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()))
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except Exception as e:
        print(f"No existing CSV found in S3 (or read error). ({e})")
        return pd.DataFrame()

# Save updated dataframe into S3 as CSV
def write_csv_to_s3(df: pd.DataFrame):
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    s3.put_object(Bucket=S3_BUCKET, Key=DATA_KEY, Body=buf.getvalue())
    print("Successfully saved updated CSV to S3.")

# Telegram Environment Variables
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# Send Telegram alert
def send_telegram_alert(message: str, silent: bool = False):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram credentials missing")
        return

    et_time = datetime.now(timezone.utc) - timedelta(hours=5)
    kst_time = datetime.now(timezone.utc) + timedelta(hours=9)
    text = f"{message}\n🕐 {et_time.strftime('%H:%M')} ET\n🕐 {kst_time.strftime('%H:%M')} KST"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "disable_notification": silent,
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Telegram alert sent successfully.")
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

# Main entry point for AWS lambda
def lambda_handler(event, context):
    print(f"Execution started. Event: {event}")

    try:
        json_data = fetch_qqq_daily_price()
        new_df = json_to_df(json_data)
        if new_df.empty:
            print("Failed to parse any data from KIS API.")
            return {"statusCode": 500, "body": "No data from KIS API."}

    except Exception as e:
        print(f"Error fetching data from KIS: {e}")
        return {"statusCode": 500, "body": str(e)}

    try:
        existing_df = read_csv_from_s3()
        if not existing_df.empty:

            existing_df['Date'] = pd.to_datetime(existing_df['Date'])
            new_df['Date'] = pd.to_datetime(new_df['Date'])

            latest_existing_df = existing_df['Date'].max()

            existing_df = existing_df[existing_df['Date'] < latest_existing_df]

            new_filtered_data = new_df[new_df['Date'] >= latest_existing_df]

            merged = pd.concat([existing_df, new_filtered_data])


        else:
            merged = new_df
    except Exception as e:
        print(f"Error reading S3 data. Error: {e}")
        return {"statusCode": 500, "body": str(e)}

    write_csv_to_s3(merged)

    signal = check_signal(merged)
    print(f"Signal Result: {signal}")

    current_minute = datetime.now().minute

    if current_minute == 55:
        send_telegram_alert("🟢 Bot Waking Up", silent=True)

    if "Cross" in signal and "No Cross" not in signal:
        send_telegram_alert(signal)
    elif "Error" in signal:
        print(f"Error while checking signal: {signal}")

    if current_minute == 0:
        send_telegram_alert("🔴 Boot Sleeping", silent=True)

    return {"statusCode": 200, "signal": signal}