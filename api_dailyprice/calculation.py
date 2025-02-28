import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

# Load environment variables from .env
load_dotenv()


def get_access_token():
    try:
        with open('../stock_token.json', 'r') as token_file:
            token_data = json.load(token_file)
            return token_data.get('authorization', '')
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error loading token: {e}")
        return ''


# Load credentials
APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
ACCESS_TOKEN = get_access_token()


# API Request Header
headers = {
    "content-type": "application/json; charset=utf-8",
    "authorization": f"Bearer {ACCESS_TOKEN}",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
    "tr_id": "HHDFS76240000"
}

date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y%m%d")

# API Request Parameter
params = {
    "AUTH": "",
    "EXCD": "NAS",
    "SYMB": "QQQ",
    "GUBN": "0",
    "BYMD": date,
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
    print(f"Retrieved {len(data.get('output2', []))} new records")

    # Get Subsequent data
    last_date = data['output2'][-1]['xymd']
    last_date = (datetime.strptime(last_date, "%Y%m%d")
                     - timedelta(days=1)).strftime("%Y%m%d")
    print(f"Last available date: {last_date}")
    params['BYMD'] = last_date
    second_response = requests.get(
        url="https://openapi.koreainvestment.com:9443/uapi/overseas-price/v1/quotations/dailyprice",
        headers=headers,
        params=params
    )

    if second_response.status_code == 200:
            new_data = second_response.json()
            print(f"Retrieved {len(new_data.get('output2', []))} new records")

            # Append new data to existing data
            data['output2'].extend(new_data.get('output2', []))
            print(f"Total records: {len(data['output2'])}")

            start_date = data['output2'][-1]['xymd']
            print(f"\nStart date : {start_date}")
            end_date = datetime.now().strftime("%Y%m%d")
            print(f"End date : {end_date}\n")

            # Calculate MA 160
            prices = [float(item['clos']) for item in data['output2']]

            if len(prices) >= 160:
                ma_160 = sum(prices[:160]) / 160
            else:
                ma_160 = None

            if ma_160:
                print(f"QQQ 160일 이동평균가: {ma_160:.2f}")
            else:
                print("데이터 부족")


            # Save to JSON file
            try:
                with open('stock_data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print(f"File saved to: {os.path.abspath('stock_data.json')}")
            except Exception as e:
                print(f"Error saving file: {str(e)}")

    else:
        print(f"Second API request failed: {second_response.status_code}")

else:
    print(f"First API request failed: {response.status_code}")
