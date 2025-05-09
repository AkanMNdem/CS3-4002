#  This script loads and prepares stock data from CSV files.
import os
import pandas as pd

# Function to load and prepare all stock data from CSV files
def load_and_prepare_all(start='2015-01-01', folder='DATA'):
    data = {}
    for file in os.listdir(folder):
        if file.endswith('_monthly.csv'):
            symbol = file.split('_')[0]  # Extract ticker from filename
            path = os.path.join(folder, file) # Construct full path
            df = pd.read_csv(path, index_col=0, parse_dates=True)  # Ensure dates are parsed
            df.index = pd.to_datetime(df.index, errors='coerce')  # Convert index to datetime
            df = df[df.index >= pd.to_datetime(start)]  # Ensure start is a valid date
            df['month'] = range(len(df)) # Create month index
            df = df.rename(columns={"4. close": "close"}) # Rename column to 'close'
            data[symbol] = df[['month', 'close']] # Select relevant columns
    return data

# verify the function
if __name__ == '__main__':
    all_data = load_and_prepare_all()
    for symbol, df in all_data.items():
        print(f"{symbol}:\n", df.head(), "\n")