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
def send_telegram_alert(message: str):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram credentials missing")
        return

    et_time = datetime.now(timezone.utc) - timedelta(hours=5)
    kst_time = datetime.now(timezone.utc) + timedelta(hours=9)
    text = f"{message}\n🕐 {et_time.strftime('%H:%M')} ET\n🕐 {kst_time.strftime('%H:%M')} KST"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Telegram alert sent successfully.")
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")