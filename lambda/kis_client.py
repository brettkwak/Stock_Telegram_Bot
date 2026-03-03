import os
import json
import boto3
import requests
from datetime import datetime, timezone

S3_BUCKET = os.environ.get("S3_BUCKET")
APP_KEY = os.environ.get("APP_KEY")
APP_SECRET = os.environ.get("APP_SECRET")

TOKEN_KEY = "stock_token.json"
KIS_BASE_URL = "https://openapi.koreainvestment.com:9443"

# Initialize S3
s3 = boto3.client("s3")

# Load token from S3
def _load_token() -> str:
    try:
        response = s3.get_object(Bucket=S3_BUCKET, Key=TOKEN_KEY)
        token_data = json.loads(response['Body'].read())
        return token_data.get('authorization', '')
    except Exception as e:
        print(f"Token not found in S3 or error reading it: {e}")
        return ''

# Save token to S3
def _save_token(token: str):
    try:
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=TOKEN_KEY,
            Body=json.dumps({"authorization": token})
        )
        print("Successfully saved new token to S3.")
    except Exception as e:
        print(f"Failed to save token to S3: {e}")

# Call KIS API to get new token
def fetch_new_token() -> str:
    print("Requesting new KIS API Token...")
    url = f"{KIS_BASE_URL}/oauth2/tokenP"
    headers = {"content-type": "application/json"}
    body = {
        "grant_type": "client_credentials",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET
    }

    res = requests.post(url, headers=headers, json=body)
    res.raise_for_status()

    new_token = res.json().get("access_token")
    if new_token:
        _save_token(new_token)
        return new_token
    else:
        raise Exception("Failed to parse token from KIS response.")

# Fetch daily QQQ price data
def fetch_qqq_daily_price() -> dict:
    token = _load_token()

    if not token:
        token = fetch_new_token()

    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "HHDFS76240000"
    }

    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    params = {
        "AUTH": "", "EXCD": "NAS", "SYMB": "QQQ",
        "GUBN": "0", "BYMD": date_str, "MODP": "1"
    }

    url = f"{KIS_BASE_URL}/uapi/overseas-price/v1/quotations/dailyprice"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 500:
        print("Invalid/Expired TOKEN Key. Fetching new token...")
        token = fetch_new_token()
        headers["authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    data = response.json()
    print(f"Retrieved {len(data.get('output2', []))} records from KIS API.")
    return data
