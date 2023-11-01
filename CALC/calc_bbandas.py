import pandas as pd
from API_BINANCE.get_api import get_apii
from pparamss import my_params

def calc_bbandas(data, window=my_params.KLINES_PERIOD, num_std_dev=2):
    df = data.copy()  # Make a copy of the input DataFrame to avoid modifying it

    # Calculate the rolling mean
    df['Rolling Mean'] = df['Close'].rolling(window=window).mean()
    
    # Calculate the rolling standard deviation
    df['Rolling Std'] = df['Close'].rolling(window=window).std()
    
    # Calculate the upper and lower Bollinger Bands
    df['Upper Bollinger Band'] = df['Rolling Mean'] + (df['Rolling Std'] * num_std_dev)
    df['Lower Bollinger Band'] = df['Rolling Mean'] - (df['Rolling Std'] * num_std_dev)

    # Filter out rows with NaN values
    df = df.dropna()

    # Get the last values of lower and upper Bollinger Bands
    lower_bollinger_band = df['Lower Bollinger Band'].iloc[-1]
    upper_bollinger_band = df['Upper Bollinger Band'].iloc[-1]

    return lower_bollinger_band, upper_bollinger_band

# Example usage:
symbol = 'BTCUSDT'
data = get_apii.get_klines(symbol)
# print(data)
lower_Bollinger_Band, upper_Bollinger_Band = calc_bbandas(data)
print(lower_Bollinger_Band, upper_Bollinger_Band)

# python -m CALC.calc_bbandas
