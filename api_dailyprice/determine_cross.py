import pandas as pd
import os

def check_signal():

    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "stock_data_QQQ.csv")

    # Load CSV into pandas DataFrame
    df = pd.read_csv(data_path)

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date', ascending=False).reset_index(drop=True)

    # Set MA value
    short_MA = 3
    long_MA = 160

    # Pre-Calculate MA
    df['Short_MA'] = df['Close'].rolling(window=short_MA).mean()
    df['Long_MA'] = df['Close'].rolling(window=long_MA).mean()

    # Get Today's MA
    current_short_MA = round(df['Short_MA'].iloc[short_MA - 1], 2)
    current_long_MA = round(df['Long_MA'].iloc[long_MA - 1], 2)
    print(f"{short_MA} MA : {current_short_MA}")
    print(f"{long_MA} MA : {current_long_MA}")

    # Get Yesterday's MA
    prev_short_MA = round(df['Short_MA'].iloc[short_MA], 2)
    prev_long_MA = round(df['Long_MA'].iloc[long_MA], 2)
    print(f"prev {short_MA} MA : {prev_short_MA}")
    print(f"prev {long_MA} MA : {prev_long_MA}")

    # Cross Check
    if current_short_MA > current_long_MA and prev_short_MA < prev_long_MA:
        return "✅Golden Cross✅"
    elif current_short_MA < current_long_MA and prev_short_MA > prev_long_MA:
        return "⛔Death Cross⛔"
    else:
        print("No Cross Detected")

if __name__ == "__main__":
    print(f"Signal : {check_signal()}")