# # from API_BINANCE.get_api import get_apii
# # from pparamss import my_params

# # def calc_pivot_lev_func(data, n=my_params.pivot_levels_type, window=my_params.KLINES_PERIOD):
# #     df = data 

# #     df['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3
# #     df['Support1'] = (2 * df['Pivot']) - df['High']
# #     df['Support2'] = df['Pivot'] - (df['High'] - df['Low'])
# #     df['Support3'] = df['Low'] - 2 * (df['High'] - df['Pivot'])
# #     df['Resistance1'] = (2 * df['Pivot']) - df['Low']
# #     df['Resistance2'] = df['Pivot'] + (df['High'] - df['Low'])
# #     df['Resistance3'] = df['High'] + 2 * (df['Pivot'] - df['Low'])

# #     support_ma = df[f'Support{n}'].rolling(window=window).mean().iloc[-1]
# #     resistance_ma = df[f'Resistance{n}'].rolling(window=window).mean().iloc[-1]

# #     return support_ma, resistance_ma

# # symbol = 'BTCUSDT'
# # support_ma, resistance_ma = None, None

# # data = get_apii.get_klines(symbol)
# # support_ma, resistance_ma = calc_pivot_lev_func(data, 1)
# # print(support_ma, resistance_ma)
# # support_ma, resistance_ma = calc_pivot_lev_func(data, 2)
# # print(support_ma, resistance_ma)
# # support_ma, resistance_ma = calc_pivot_lev_func(data, 3)
# # print(support_ma, resistance_ma)

# # python test.py

# # Получение данных о стакане
# # import requests, json

# # symbol = "BTCUSDT"
# # level = 5
# # response = requests.get(f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit={level}")
# # data = response.json()

# # # Извлечение цен и объемов спроса и предложения
# # bids = data['bids']  # Уровни спроса
# # asks = data['asks']  # Уровни предложения

# # # Определение уровней поддержки и сопротивления
# # support_level = bids[0][0]  # Цена уровня поддержки
# # resistance_level = asks[0][0]  # Цена уровня сопротивления

# # print(support_level, resistance_level)
# from pparamss import my_params 
# from config import Configg
# import pandas as pd
# from datetime import datetime


# class GETT_API(Configg):

#     def __init__(self) -> None:
#         super().__init__()   
#         self.method = 'GET'

#     def get_klines(self, symbol, end_date):
#         klines = None
#         url = my_params.URL_PATTERN_DICT["klines_url"]

#         params = {}
#         params["symbol"] = symbol
#         params["interval"] = my_params.INTERVAL

#         if end_date:            
#            params["endTime"] = int(end_date.timestamp() * 1000)
#         params["limit"] = my_params.KLINES_PERIOD + 1
#         params = self.get_signature(params)
#         klines = self.HTTP_request(url, method=self.method, headers=self.header, params=params)
        
#         if klines:
#             data = pd.DataFrame(klines).iloc[:, :6]
#             data.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
#             data = data.set_index('Time')
#             data.index = pd.to_datetime(data.index, unit='ms')
#             data = data.astype(float)
        
#         return data

# your_instance = GETT_API()
# end_date = datetime(2023, 8, 12)
# klines_data = your_instance.get_klines("BTCUSDT", end_date=end_date)
# print(klines_data)

# # python test.py


# a = [1,2,3,4,5]
# b = a[:-3]
# c = a[-3:]
# print(b)
# print(c)

import requests

spot_klines_url = 'https://api.binance.com/api/v3/klines'
symbol = 'BTCUSDT'
interval = '1m'

params = {
    'symbol': symbol,
    'interval': interval
}

response = requests.get(spot_klines_url, params=params)
klines_data = response.json()
print(klines_data)