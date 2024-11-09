import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time




# Alpha Vantage API configuration
API_KEY = 'PO7KFKT2JF0RGG9V'  # Replace with your Alpha Vantage API key
SYMBOL = 'AAPL'  # Replace with desired stock symbol

# Initialize Alpha Vantage API client
ts = TimeSeries(key=API_KEY, output_format='pandas')

try:
    # Get daily stock data
    data, meta_data = ts.get_daily(symbol=SYMBOL, outputsize='full')
    
    # Rename columns for clarity
    data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    
    # Reset index to make date a column
    data.reset_index(inplace=True)
    data.rename(columns={'index': 'Date'}, inplace=True)
    
    # Save to CSV
    csv_filename = f'Datasets/{SYMBOL}_daily_prices.csv'
    data.to_csv(csv_filename, index=False)
    print(f"Data successfully saved to {csv_filename}")
    
    # API has rate limits, so wait before making another request
    time.sleep(12)  # Alpha Vantage free tier has a rate limit of 5 calls per minute

except Exception as e:
    print(f"Error occurred: {str(e)}")
