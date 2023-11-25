# # # from API_BINANCE.get_api import get_apii
# # # from pparamss import my_params

# # # def calc_pivot_lev_func(data, n=my_params.pivot_levels_type, window=my_params.KLINES_PERIOD):
# # #     df = data 

# # #     df['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3
# # #     df['Support1'] = (2 * df['Pivot']) - df['High']
# # #     df['Support2'] = df['Pivot'] - (df['High'] - df['Low'])
# # #     df['Support3'] = df['Low'] - 2 * (df['High'] - df['Pivot'])
# # #     df['Resistance1'] = (2 * df['Pivot']) - df['Low']
# # #     df['Resistance2'] = df['Pivot'] + (df['High'] - df['Low'])
# # #     df['Resistance3'] = df['High'] + 2 * (df['Pivot'] - df['Low'])

# # #     support_ma = df[f'Support{n}'].rolling(window=window).mean().iloc[-1]
# # #     resistance_ma = df[f'Resistance{n}'].rolling(window=window).mean().iloc[-1]

# # #     return support_ma, resistance_ma

# # # symbol = 'BTCUSDT'
# # # support_ma, resistance_ma = None, None

# # # data = get_apii.get_klines(symbol)
# # # support_ma, resistance_ma = calc_pivot_lev_func(data, 1)
# # # print(support_ma, resistance_ma)
# # # support_ma, resistance_ma = calc_pivot_lev_func(data, 2)
# # # print(support_ma, resistance_ma)
# # # support_ma, resistance_ma = calc_pivot_lev_func(data, 3)
# # # print(support_ma, resistance_ma)

# # # python test.py

# # # Получение данных о стакане
# # # import requests, json

# # # symbol = "BTCUSDT"
# # # level = 5
# # # response = requests.get(f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit={level}")
# # # data = response.json()

# # # # Извлечение цен и объемов спроса и предложения
# # # bids = data['bids']  # Уровни спроса
# # # asks = data['asks']  # Уровни предложения

# # # # Определение уровней поддержки и сопротивления
# # # support_level = bids[0][0]  # Цена уровня поддержки
# # # resistance_level = asks[0][0]  # Цена уровня сопротивления

# # # print(support_level, resistance_level)
# # from pparamss import my_params 
# # from config import Configg
# # import pandas as pd
# # from datetime import datetime


# # class GETT_API(Configg):

# #     def __init__(self) -> None:
# #         super().__init__()   
# #         self.method = 'GET'

# #     def get_klines(self, symbol, end_date):
# #         klines = None
# #         url = my_params.URL_PATTERN_DICT["klines_url"]

# #         params = {}
# #         params["symbol"] = symbol
# #         params["interval"] = my_params.INTERVAL

# #         if end_date:            
# #            params["endTime"] = int(end_date.timestamp() * 1000)
# #         params["limit"] = my_params.KLINES_PERIOD + 1
# #         params = self.get_signature(params)
# #         klines = self.HTTP_request(url, method=self.method, headers=self.header, params=params)
        
# #         if klines:
# #             data = pd.DataFrame(klines).iloc[:, :6]
# #             data.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
# #             data = data.set_index('Time')
# #             data.index = pd.to_datetime(data.index, unit='ms')
# #             data = data.astype(float)
        
# #         return data

# # your_instance = GETT_API()
# # end_date = datetime(2023, 8, 12)
# # klines_data = your_instance.get_klines("BTCUSDT", end_date=end_date)
# # print(klines_data)

# # # python test.py


# # a = [1,2,3,4,5]
# # b = a[:-3]
# # c = a[-3:]
# # print(b)
# # print(c)

# # import requests

# # spot_klines_url = 'https://api.binance.com/api/v3/klines'
# # symbol = 'BTCUSDT'
# # interval = '1m'

# # params = {
# #     'symbol': symbol,
# #     'interval': interval
# # }

# # response = requests.get(spot_klines_url, params=params)
# # klines_data = response.json()
# # print(klines_data)
# # text = f"Please change the options:\nmarket = spot\ntest_flag = False"  
# # new_market = text.split('=')[1].split('\n')[0].strip()
# # new_test_flag = text.split('=')[2].strip().lower() == 'true'
# # new_test_flag = bool(new_test_flag_str)
# # print(new_market)
# # print(new_test_flag)

# # from datetime import datetime

# # date_string = '2023-10-31'
# # date_format = '%Y-%m-%d'

# # # Преобразование строки в объект datetime
# # date_object = datetime.strptime(date_string, date_format)

# # print(type(date_object))

# # def detect_rsi_divergence(closes, rsi_values):
# #     # Проверяем, является ли последнее значение RSI больше 50
# #     if rsi_values[-1] > 50:
# #         # Проверяем, была ли цена на новом высоком уровне
# #         if closes[-1] > max(closes[:-1]):
# #             print("Бычья дивергенция: RSI не подтверждает новый высокий в цене.")
# #             # В этом месте можно вставить код или логику для принятия решения о покупке
# #             return 1  # Сигнал на покупку
# #         else:
# #             print("Бычья дивергенция отсутствует.")
# #             return 0  # Отсутствие сигнала
# #     # Проверяем, является ли последнее значение RSI меньше 50
# #     elif rsi_values[-1] < 50:
# #         # Проверяем, была ли цена на новом низком уровне
# #         if closes[-1] < min(closes[:-1]):
# #             print("Медвежья дивергенция: RSI не подтверждает новый низкий в цене.")
# #             # В этом месте можно вставить код или логику для принятия решения о продаже
# #             return -1  # Сигнал на продажу
# #         else:
# #             print("Медвежья дивергенция отсутствует.")
# #             return 0  # Отсутствие сигнала
# #     else:
# #         print("RSI находится в нейтральной зоне.")
# #         return 0  # Отсутствие сигнала

# # # Пример использования
# # closes = [10, 12, 15, 14, 16, 18]
# # rsi_values = [38.509508614672285, 37.02042485106416, 52.988250909750924, 52.1602916222665, 48.154229288370445, 52.12705647174558]
# # signal = detect_rsi_divergence(closes, rsi_values)
# # print("Сигнал:", signal)

# # def detect_rsi_divergence(closes, rsi_values):
# #     # Проверяем, является ли последнее значение RSI выше 50
# #     if rsi_values[-1] > 50:
# #         # Проверяем, была ли цена на новом высоком уровне
# #         if closes[-1] > max(closes[:-1]):
# #             print("Бычья дивергенция: RSI не подтверждает новый высокий в цене.")
# #             # В этом месте можно вставить код или логику для принятия решения о покупке
# #             return 1  # Сигнал на покупку
# #         else:
# #             print("Бычья дивергенция отсутствует.")
# #             return 0  # Отсутствие сигнала
# #     # Проверяем, является ли последнее значение RSI ниже 50
# #     elif rsi_values[-1] < 50:
# #         # Проверяем, была ли цена на новом низком уровне
# #         if closes[-1] < min(closes[:-1]):
# #             print("Медвежья дивергенция: RSI не подтверждает новый низкий в цене.")
# #             # В этом месте можно вставить код или логику для принятия решения о продаже
# #             return -1  # Сигнал на продажу
# #         else:
# #             print("Медвежья дивергенция отсутствует.")
# #             return 0  # Отсутствие сигнала
# #     else:
# #         print("RSI находится в нейтральной зоне.")
# #         return 0  # Отсутствие сигнала

# # # Пример использования
# # closes = [10, 12, 15, 14, 16, 18]
# # rsi_values = [38.509508614672285, 37.02042485106416, 52.988250909750924, 52.1602916222665, 48.154229288370445, 52.12705647174558]
# # signal = detect_rsi_divergence(closes, rsi_values)
# # print("Сигнал:", signal)

# # import numpy as np

# # def detect_rsi_divergence(closes, rsi_values):    
# #     if np.mean(rsi_values[-4:]) > 50:       
# #         if closes[-1] > max(closes[:-1]):
# #             return 1
# #         else:
# #             return 0    
# #     elif np.mean(rsi_values[-4:]) < 50:        
# #         if closes[-1] < min(closes[:-1]):
# #             return -1  
# #         else:
            
# #             return 0  
# #     else:       
# #         return 0  

# # # Пример использования
# # closes = [10, 12, 15, 14, 16, 18]
# # rsi_values = [38.509508614672285, 37.02042485106416, 52.988250909750924, 52.1602916222665, 48.154229288370445, 52.12705647174558]
# # signal = detect_rsi_divergence(closes, rsi_values)
# # print("Сигнал:", signal)

# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample data (replace this with your own OHLC data)
# data = {
#     'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
#     'Open': [100, 102, 98, 104, 101],
#     'High': [105, 108, 100, 110, 103],
#     'Low': [98, 100, 95, 101, 99],
#     'Close': [102, 105, 97, 108, 100]
# }

# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])
# df.set_index('Date', inplace=True)

# # Calculate Heikin Ashi candles
# df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
# df['HA_Open'] = (df['Open'].shift(1) + df['Close'].shift(1)) / 2
# df['HA_High'] = df[['High', 'HA_Open', 'HA_Close']].max(axis=1)
# df['HA_Low'] = df[['Low', 'HA_Open', 'HA_Close']].min(axis=1)

# # Detect Doji patterns
# df['Body'] = abs(df['Open'] - df['Close'])
# df['UpperShadow'] = df['High'] - df[['Open', 'Close']].max(axis=1)
# df['LowerShadow'] = df[['Open', 'Close']].min(axis=1) - df['Low']

# # Define a function to identify Doji candles
# def is_doji(row):
#     return (row['Body'] < 0.1 * (row['High'] - row['Low'])) and (row['UpperShadow'] > 2 * row['Body']) and (row['LowerShadow'] > 2 * row['Body'])

# df['IsDoji'] = df.apply(is_doji, axis=1)

# # Generate signals based on Heikin Ashi and Doji
# df['Buy_Signal'] = (df['HA_Open'] < df['HA_Close']) & df['IsDoji']
# df['Sell_Signal'] = (df['HA_Open'] > df['HA_Close']) & df['IsDoji']

# # Plotting
# plt.figure(figsize=(10, 5))
# plt.plot(df.index, df['HA_Close'], label='Heikin Ashi Close', color='blue')
# plt.scatter(df[df['Buy_Signal']].index, df[df['Buy_Signal']]['HA_Close'], label='Buy Signal', marker='^', color='green')
# plt.scatter(df[df['Sell_Signal']].index, df[df['Sell_Signal']]['HA_Close'], label='Sell Signal', marker='v', color='red')
# plt.title('Heikin Ashi with Doji Signals')
# plt.legend()
# plt.show()

# doji = 0

# buy_doji_signal = sell_doji_signal = doji == 0
# print(buy_doji_signal, sell_doji_signal)


# import pandas as pd
# import yfinance as yf
# import pandas_ta as ta
# import talib

# # Fetch historical data for the S&P 500 index
# symbol = '^GSPC'
# start_date = '2022-01-01'
# end_date = '2022-12-31'
# data = yf.download(symbol, start=start_date, end=end_date)

# # Function to detect doji candlestick patterns
# def detect_doji(data):
#     data['is_doji'] = ta.cdl_doji(data['Open'], data['High'], data['Low'], data['Close'])
#     return data

# # Apply the doji detection function
# sp500_data = detect_doji(data)

# # Analyze the doji patterns
# doji_signals = sp500_data[sp500_data['is_doji'] != 0]

# # Print the DataFrame with doji signals
# print(doji_signals)

import talib 
import pandas as pd
import yfinance as yf

def calculate_doji(data):
    try:
        data['Doji'] = talib.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])        
    except Exception as ex:
        print(f"Error in calculate_doji: {ex}")
    return data

def get_historical_data(symbol='BTC-USD'):
    start= "2022-01-1"
    end="2023-11-19"
    # start = "2020-1-1"
    # end = "2023-11-19"
    data = yf.download(symbol, start=start, end=end, interval='1h')
    try:
        data.drop(['Dividends'], axis=1, inplace=True)
        data.drop(['Stock Splits'], axis=1, inplace=True)     
    except:
        pass   
    data.reset_index(inplace=True)   
    try:
        data['Date'] = data['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')   
    except:
        pass  
    try:
        data['Date'] = data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        pass
    return data


data = get_historical_data()
data = calculate_doji(data)
print(data['Doji'].to_list())