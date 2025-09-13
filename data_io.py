import pandas as pd


# CSV into dataframe
def csv_to_df(file_path):

    print(f"Reading CSV from: {file_path}")

    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("CSV not found")
        return pd.DataFrame()


# JSON into dataframe
def json_to_df(json_data):
    return pd.DataFrame(json_data)


# Save dataframe to CSV
def save_df_to_csv(df, file_path):
    print(f"Saving DataFrame to: {file_path}")
    df.to_csv(file_path, index=False)
    print("Save complete.")

