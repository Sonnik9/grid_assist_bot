from API_BINANCE.get_api import get_apii
from pparamss import my_params

def calc_pivot_lev_func(dataa, n=my_params.pivot_levels_type, window=my_params.KLINES_PERIOD):
    
    data = dataa.copy()
    
    data['Pivot'] = (data['High'] + data['Low'] + data['Close']) / 3
    data['Support1'] = (2 * data['Pivot']) - data['High']
    data['Support2'] = data['Pivot'] - (data['High'] - data['Low'])
    data['Support3'] = data['Low'] - 2 * (data['High'] - data['Pivot'])
    data['Resistance1'] = (2 * data['Pivot']) - data['Low']
    data['Resistance2'] = data['Pivot'] + (data['High'] - data['Low'])
    data['Resistance3'] = data['High'] + 2 * (data['Pivot'] - data['Low'])

    support_ma = data[f'Support{n}'].rolling(window=window).mean().iloc[-1]
    resistance_ma = data[f'Resistance{n}'].rolling(window=window).mean().iloc[-1]

    return support_ma, resistance_ma