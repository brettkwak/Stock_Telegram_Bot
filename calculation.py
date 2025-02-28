import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env
load_dotenv()


def get_access_token():
    try:
        with open('stock_token.json', 'r') as token_file:
            token_data = json.load(token_file)
            return token_data.get('authorization', '')
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error loading token: {e}")
        return ''


# Load credentials
APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
ACCESS_TOKEN = get_access_token()

# Set start & end date
end_date = datetime.now().strftime("%Y%m%d")
start_date = (datetime.now() - timedelta(days=160)).strftime("%Y%m%d")
print(f"start date : {start_date}")
print(f"end date : {end_date}")

# API Request Header
headers = {
    "content-type": "application/json; charset=utf-8",
    "authorization": f"Bearer {ACCESS_TOKEN}",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
    "tr_id": "HHDFS76240000"
}

# API Request Parameter
params = {
    "AUTH": "",
    "EXCD": "NAS",
    "SYMB": "QQQ",
    "GUBN": "0",
    "BYMD": "",
    "MODP": "1",
}

# API request
response = requests.get(
    url="https://openapi.koreainvestment.com:9443/uapi/overseas-price/v1/quotations/dailyprice",
    headers=headers,
    params=params
)

# 데이터 처리
if response.status_code == 200:
    data = response.json()

    # Save to JSON file
    try:
        with open('stock_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"File saved to: {os.path.abspath('stock_data.json')}")
    except Exception as e:
        print(f"Error saving file: {str(e)}")


else:
    print("API 호출 실패:", response.status_code)
