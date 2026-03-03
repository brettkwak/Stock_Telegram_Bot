import pandas as pd
import json
from datetime import datetime


# CSV into dataframe
def csv_to_df(file_path):

    print(f"Reading CSV from: {file_path}")

    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        print("CSV not found")
        return pd.DataFrame()


# JSON into dataframe
def json_to_df(json_data: dict):

    data = json_data['output2']

    processed_data = []

    for record in data:
        formatted_date = datetime.strptime(record['xymd'], '%Y%m%d').strftime('%Y-%m-%d')

        processed_record = {
            'Date': formatted_date,
            'Close': round(float(record['clos']), 2)
        }
        processed_data.append(processed_record)

    df = pd.DataFrame(processed_data)
    df['Date'] = pd.to_datetime(df['Date'])

    return df


# Save dataframe to CSV
def save_df_to_csv(df, file_path):
    print(f"Saving DataFrame to: {file_path}")
    df.to_csv(file_path, index=False)
    print("Save complete.")

