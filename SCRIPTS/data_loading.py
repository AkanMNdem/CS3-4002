# necessary imports to handle data
import requests
import json
import pandas as pd

api_key = 'BGC08TPHNNTLV25Z'

# Function to get monthly ticker data from Alpha Vantage and save it to a CSV file
def get_monthly_ticker_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    # Check if the response contains the expected data
    if "Monthly Time Series" not in data:
        print("Error: Unexpected response format.")
        return None

    #  create a DataFrame from the JSON data and save it to a CSV file
    df = pd.DataFrame.from_dict(data["Monthly Time Series"], orient="index").astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df.to_csv(f"DATA/{symbol}_monthly.csv")
    return df

# script to run the function and save the data
if __name__ == '__main__':
    symbol = input("Please enter ticker symbol: ").strip().upper()
    df = get_monthly_ticker_data(symbol)
    print(df.head())