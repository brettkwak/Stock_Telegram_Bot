import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import generate_token




def get_access_token():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    data_path = os.path.join(parent_dir, "stock_token.json")

    try:
        with open(data_path, 'r') as token_file:
            token_data = json.load(token_file)
            return token_data.get('authorization', '')
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error loading token: {e}")
        return ''


def get_price_data():


    # Load environment variables from .env
    load_dotenv()

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

    date = (datetime.now(timezone.utc)).strftime("%Y%m%d")

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

    if response.status_code == 500:
        print("Invalid TOKEN Key")
        print("Requesting TOKEN..")
        generate_token.get_token()
        headers["authorization"] = f"Bearer {get_access_token()}"

        response = requests.get(
            url="https://openapi.koreainvestment.com:9443/uapi/overseas-price/v1/quotations/dailyprice",
            headers=headers,
            params=params
        )

    # 데이터 처리
    if response.status_code == 200:
        data = response.json()
        print(f"Retrieved {len(data.get('output2', []))} new records")

        # Save to JSON file
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, 'stock_data.json')

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"File saved to: {file_path}")

        except Exception as e:
            print(f"Error saving file: {str(e)}")



    else:
        print(f"First API request failed: {response.status_code}")



if __name__ == '__main__':
    get_price_data()


