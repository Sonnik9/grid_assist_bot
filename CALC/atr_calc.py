from pparamss import my_params

def calculate_atr(data, period=my_params.KLINES_PERIOD):

    true_ranges = []

    for i in range(1, len(data)):
        high = data['High'].iloc[i]
        low = data['Low'].iloc[i]
        close = data['Close'].iloc[i]
        true_range = max(abs(high - low), abs(high - close), abs(low - close))        
        true_ranges.append(true_range)
    atr = sum(true_ranges[-period:]) / period

    return atr