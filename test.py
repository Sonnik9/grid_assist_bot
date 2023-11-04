# from API_BINANCE.get_api import get_apii
# from pparamss import my_params

# def calc_pivot_lev_func(data, n=my_params.pivot_levels_type, window=my_params.KLINES_PERIOD):
#     df = data 

#     df['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3
#     df['Support1'] = (2 * df['Pivot']) - df['High']
#     df['Support2'] = df['Pivot'] - (df['High'] - df['Low'])
#     df['Support3'] = df['Low'] - 2 * (df['High'] - df['Pivot'])
#     df['Resistance1'] = (2 * df['Pivot']) - df['Low']
#     df['Resistance2'] = df['Pivot'] + (df['High'] - df['Low'])
#     df['Resistance3'] = df['High'] + 2 * (df['Pivot'] - df['Low'])

#     support_ma = df[f'Support{n}'].rolling(window=window).mean().iloc[-1]
#     resistance_ma = df[f'Resistance{n}'].rolling(window=window).mean().iloc[-1]

#     return support_ma, resistance_ma

# symbol = 'BTCUSDT'
# support_ma, resistance_ma = None, None

# data = get_apii.get_klines(symbol)
# support_ma, resistance_ma = calc_pivot_lev_func(data, 1)
# print(support_ma, resistance_ma)
# support_ma, resistance_ma = calc_pivot_lev_func(data, 2)
# print(support_ma, resistance_ma)
# support_ma, resistance_ma = calc_pivot_lev_func(data, 3)
# print(support_ma, resistance_ma)

# python test.py

# Получение данных о стакане
# import requests, json

# symbol = "BTCUSDT"
# level = 5
# response = requests.get(f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit={level}")
# data = response.json()

# # Извлечение цен и объемов спроса и предложения
# bids = data['bids']  # Уровни спроса
# asks = data['asks']  # Уровни предложения

# # Определение уровней поддержки и сопротивления
# support_level = bids[0][0]  # Цена уровня поддержки
# resistance_level = asks[0][0]  # Цена уровня сопротивления

# print(support_level, resistance_level)
