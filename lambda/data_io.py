import pandas as pd
from datetime import datetime

# Convert JSON into dataframe
def json_to_df(json_data: dict) -> pd.DataFrame:

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