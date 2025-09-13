from bot import run_bot
from update_data import update_data

if __name__ == '__main__':
    stock_data_path = "api_dailyprice/stock_data_QQQ.csv"
    update_data(stock_data_path)
    run_bot()
