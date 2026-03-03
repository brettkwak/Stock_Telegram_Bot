from api_dailyprice.get_price_data import get_price_data
from data_io import *

def update_data(csv_path):

    old_df = csv_to_df(csv_path)
    json_data = get_price_data()
    new_df = json_to_df(json_data)


    max_date = old_df['Date'].max()
    target_date = max_date
    filtered_new_df = new_df[new_df['Date'] >= target_date]

    # Concatenate
    concat_df = pd.concat([old_df, filtered_new_df], ignore_index=True)
    # Remove duplication of "Date"
    dup_removed_df = concat_df.drop_duplicates(subset=['Date'], keep='last')
    # Reset Index
    final_df = dup_removed_df.sort_values(by='Date', ascending=False).reset_index(drop=True)

    # Overwrite
    save_df_to_csv(final_df, csv_path)

    return


if __name__ == '__main__':
    update_data("api_dailyprice/stock_data_QQQ.csv")