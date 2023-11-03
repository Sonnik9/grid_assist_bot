
    # def cancel_order_by_id(self, symbol, last_sl_order_id):

    #     cancel_order = None
    #     all_orders = None
    #     success_flag = False
    #     all_orders = get_apii.get_all_orders()

    #     for item in all_orders:
    #         if item["symbol"] == symbol:
    #             params = {}
    #             params["symbol"] = item["symbol"]
    #             params["orderId"] = last_sl_order_id
    #             params = self.get_signature(params)
    #             url = my_params.URL_PATTERN_DICT['create_order_url']                
    #             cancel_order = self.HTTP_request(url, method=self.method, headers=self.header, params=params)                
    #             break

    #     if cancel_order and 'status' in cancel_order and cancel_order['status'] == 'CANCELED':
    #         success_flag = True 
            
    #     return cancel_order, success_flag


# Plot the Price Chart with Support and Resistance Levels
# plt.figure(figsize=(12, 6))
# plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
# plt.plot(df['Date'], df['Support1'], label='Support1', linestyle='--', color='green')
# plt.plot(df['Date'], df['Support2'], label='Support2', linestyle='--', color='orange')
# plt.plot(df['Date'], df['Support3'], label='Support3', linestyle='--', color='red')
# plt.plot(df['Date'], df['Resistance1'], label='Resistance1', linestyle='--', color='purple')
# plt.plot(df['Date'], df['Resistance2'], label='Resistance2', linestyle='--', color='brown')
# plt.plot(df['Date'], df['Resistance3'], label='Resistance3', linestyle='--', color='black')

# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.title('Price Chart with Support and Resistance Levels')
# plt.legend()
# plt.grid()

# plt.show()



# , Interval, Exchange

# def get_tv_signals(character, top_coins):

#     rec_list = []
#     signals_list = []
    
#     for symbol in top_coins:
#         if not symbol:
#             continue
        
#         handler = TA_Handler(
#             symbol=symbol,
#             exchange='BINANCE',
#             screener='crypto',
#             interval=my_params.INTERVAL  
#         )

#         analysis = handler.get_analysis()
#         if character == 'REC':
#             rec_list.append(analysis.summary['RECOMMENDATION'])
#         elif character == 'INDS':
#             # BB.lower
#             signals_list.append({
#                 symbol: {
#                 'BB.lower': analysis.indicators['BB.lower'],
#                 'BB.upper': analysis.indicators['BB.upper'],
#                 'Pivot.M.Classic.S1': analysis.indicators['Pivot.M.Classic.S1'],
#                 'Pivot.M.Classic.R1': analysis.indicators['Pivot.M.Classic.R1'],
#                 'Pivot.M.Fibonacci.S1': analysis.indicators['Pivot.M.Fibonacci.S1'],
#                 'Pivot.M.Fibonacci.R1': analysis.indicators['Pivot.M.Fibonacci.R1'],

#                 }
#             })

#     return signals_list

# # Example usage:
# character = 'INDS'  # 'B' for bullish, 'S' for bearish
# top_coins = ['BTCUSDT'] #['BTCUSDT', 'ETHUSDT', 'XRPUSDT']  # Replace with your list of symbols
# signals = get_tv_signals(character, top_coins)
# print(signals)


# [{'Recommend.Other': -0.27272727, 'Recommend.All': 0.26363636, 'Recommend.MA': 0.8, 'RSI': 74.71864723, 'RSI[1]': 84.54829153, 'Stoch.K': 90.25871643, 'Stoch.D': 91.03491729, 'Stoch.K[1]': 92.6042009, 'Stoch.D[1]': 90.44268972, 'CCI20': 78.23861547, 'CCI20[1]': 86.93579511, 'ADX': 59.18583998, 'ADX+DI': 37.7030806, 'ADX-DI': 4.22127139, 'ADX+DI[1]': 39.33726188, 'ADX-DI[1]': 4.72163505, 'AO': 4693.92655882, 'AO[1]': 4741.5685, 'Mom': 1566.67, 'Mom[1]': 5428.98, 'MACD.macd': 1939.89634701, 'MACD.signal': 1734.4610898, 'Rec.Stoch.RSI': 0, 'Stoch.RSI.K': 58.59599865, 'Rec.WR': -1, 'W.R': -18.2041935, 'Rec.BBPower': 0, 'BBPower': 3459.90509988, 'Rec.UO': 0, 'UO': 56.97683349, 'close': 34636.66, 'EMA5': 34655.48085195, 'SMA5': 34740.332, 'EMA10': 33922.11304986, 'SMA10': 34424.512, 'EMA20': 32354.63131119, 'SMA20': 31741.172, 'EMA30': 31251.94542412, 'SMA30': 30309.82, 'EMA50': 30006.13953792, 'SMA50': 28905.5752, 'EMA100': 28900.28055781, 'SMA100': 28211.113, 'EMA200': 27900.21114606, 'SMA200': 28313.8375, 'Rec.Ichimoku': 0, 'Ichimoku.BLine': 31261.825, 'Rec.VWMA': 1, 'VWMA': 32152.32412682, 'Rec.HullMA9': -1, 'HullMA9': 35080.86774074, 'Pivot.M.Classic.S3': 14671.18666667, 'Pivot.M.Classic.S2': 23412.52666667, 'Pivot.M.Classic.S1': 29027.73333333, 'Pivot.M.Classic.Middle': 32153.86666667, 'Pivot.M.Classic.R1': 37769.07333333, 'Pivot.M.Classic.R2': 40895.20666667, 'Pivot.M.Classic.R3': 49636.54666667, 'Pivot.M.Fibonacci.S3': 23412.52666667, 'Pivot.M.Fibonacci.S2': 26751.71854667, 'Pivot.M.Fibonacci.S1': 28814.67478667, 'Pivot.M.Fibonacci.Middle': 32153.86666667, 'Pivot.M.Fibonacci.R1': 35493.05854667, 'Pivot.M.Fibonacci.R2': 37556.01478667, 'Pivot.M.Fibonacci.R3': 40895.20666667, 'Pivot.M.Camarilla.S3': 32239.0715, 'Pivot.M.Camarilla.S2': 33040.361, 'Pivot.M.Camarilla.S1': 33841.6505, 'Pivot.M.Camarilla.Middle': 32153.86666667, 'Pivot.M.Camarilla.R1': 35444.2295, 'Pivot.M.Camarilla.R2': 36245.519, 'Pivot.M.Camarilla.R3': 37046.8085, 'Pivot.M.Woodie.S3': 21527.77, 'Pivot.M.Woodie.S2': 24033.215, 'Pivot.M.Woodie.S1': 30269.11, 'Pivot.M.Woodie.Middle': 32774.555, 'Pivot.M.Woodie.R1': 39010.45, 'Pivot.M.Woodie.R2': 41515.895, 'Pivot.M.Woodie.R3': 47751.79, 'Pivot.M.Demark.S1': 30590.8, 'Pivot.M.Demark.Middle': 32935.4, 'Pivot.M.Demark.R1': 39332.14, 'open': 35421.43, 'P.SAR': 32533.97819576, 'BB.lower': 25845.27910673, 'BB.upper': 37637.06489327, 'AO[2]': 4772.93788235, 'volume': 39106.46254, 'change': -2.21555081, 'low': 34300, 'high': 35984.99}] 



# from pparamss import my_params
# from API_BINANCE.get_api import get_apii
# # from API_BINANCE.post_api import post_apii

# class UTILS_FOR_ORDERS():

#     def __init__(self) -> None:
#         pass

#     def assets_filters(self, sentiment_data_30d_min=1, volatility_7d_min=3, market_cap_ranc_max=50):
#         top_pairs = []
#         all_tickers = []
#         exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
#         all_tickers = get_apii.get_all_tickers()

#         if all_tickers:
#             usdt_filtered = [ticker for ticker in all_tickers if
#                             ticker['symbol'].upper().endswith('USDT') and
#                             not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
#                             float(ticker['lastPrice']) >= my_params.FILTER_PRICE]
            
#             print(usdt_filtered[0])

#             sorted_by_volume_data = sorted(usdt_filtered, key=lambda x: float(x['quoteVolume']), reverse=True)
#             sorted_by_volume_data = sorted_by_volume_data[:my_params.SLICE_VOLUME_PAIRS]

#             # Filter and sort by priceChangePercent
#             sorted_by_price_change_data = sorted(sorted_by_volume_data, key=lambda x: float(x['priceChangePercent']), reverse=True)
#             sorted_by_price_change_data = sorted_by_price_change_data[:my_params.SLICE_CHANGINGPRICES_PAIRS]

#             top_pairs = [x['symbol'] for x in sorted_by_price_change_data if x not in my_params.problem_pairs]

#             # return

#             # Filter and sort by marketCapRank (from strong to weak)
#             # sorted_by_market_cap_rank_data = sorted(sorted_by_price_change_data, key=lambda x: int(x['marketCapRank']))
#             # sorted_by_market_cap_rank_data = sorted_by_market_cap_rank_data[:my_params.SLICE_MARKET_CAP_RANK]

#             # # Filter and sort by sentimentData30D
#             # sorted_by_sentiment_data_30d = sorted(sorted_by_market_cap_rank_data, key=lambda x: float(x['sentimentData30D']), reverse=True)
#             # sorted_by_sentiment_data_30d = sorted_by_sentiment_data_30d[:my_params.SLICE_SENTIMENTE_DATA_30D]

#             # top_pairs = [x['symbol'] for x in sorted_by_sentiment_data_30d if x not in my_params.problem_pairs]
            
#             # Apply additional filters
#             # filtered_pairs = [ticker for ticker in sorted_by_sentiment_data_30d if
#             #                   float(ticker['sentimentData30D']) >= sentiment_data_30d_min and
#             #                   float(ticker['volatility7D']) >= volatility_7d_min]

#             # top_pairs = [coins['symbol'] for coins in filtered_pairs]

#         return top_pairs

# asset_filtr = UTILS_FOR_ORDERS()
# top_coins = asset_filtr.assets_filters()
# print(top_coins)
    

# python -m API_BINANCE.utils_api


# from API_BINANCE.get_api import get_apii
# from pparamss import my_params

# def calc_pivot_lev_func(dataa, n=my_params.pivot_levels_type, window=my_params.KLINES_PERIOD):
    
#     data = dataa.copy()
    
#     data['Pivot'] = (data['High'] + data['Low'] + data['Close']) / 3
#     data['Support1'] = (2 * data['Pivot']) - data['High']
#     data['Support2'] = data['Pivot'] - (data['High'] - data['Low'])
#     data['Support3'] = data['Low'] - 2 * (data['High'] - data['Pivot'])
#     data['Resistance1'] = (2 * data['Pivot']) - data['Low']
#     data['Resistance2'] = data['Pivot'] + (data['High'] - data['Low'])
#     data['Resistance3'] = data['High'] + 2 * (data['Pivot'] - data['Low'])

#     support_ma = data[f'Support{n}'].rolling(window=window).mean().iloc[-1]
#     resistance_ma = data[f'Resistance{n}'].rolling(window=window).mean().iloc[-1]

#     return support_ma, resistance_ma

# import pandas as pd
# from API_BINANCE.get_api import get_apii
# from pparamss import my_params

# def calc_bbandas(data, window=my_params.KLINES_PERIOD, num_std_dev=2):
#     df = data.copy()  # Make a copy of the input DataFrame to avoid modifying it

#     # Calculate the rolling mean
#     df['Rolling Mean'] = df['Close'].rolling(window=window).mean()
    
#     # Calculate the rolling standard deviation
#     df['Rolling Std'] = df['Close'].rolling(window=window).std()
    
#     # Calculate the upper and lower Bollinger Bands
#     df['Upper Bollinger Band'] = df['Rolling Mean'] + (df['Rolling Std'] * num_std_dev)
#     df['Lower Bollinger Band'] = df['Rolling Mean'] - (df['Rolling Std'] * num_std_dev)

#     # Filter out rows with NaN values
#     df = df.dropna()

#     # Get the last values of lower and upper Bollinger Bands
#     lower_bollinger_band = df['Lower Bollinger Band'].iloc[-1]
#     upper_bollinger_band = df['Upper Bollinger Band'].iloc[-1]

#     return lower_bollinger_band, upper_bollinger_band

# # Example usage:
# symbol = 'BTCUSDT'
# data = get_apii.get_klines(symbol)
# # print(data)
# lower_Bollinger_Band, upper_Bollinger_Band = calc_bbandas(data)
# print(lower_Bollinger_Band, upper_Bollinger_Band)

# # python -m CALC.calc_bbandas


# import telebot
# # import requests
# # from bs4 import BeautifulSoup
# import schedule
# import atexit
# import time
# import re
# import random 
# from random import choice 
# from UTILS.clean_cache import cleanup_cache
# from config import Configg
# from pparamss import my_params

# class Tg(Configg):

#     def __init__(self) -> None:
#         super().__init__()
#         tg_api_token = self.tg_api_token
#         self.bot = telebot.TeleBot(tg_api_token)
#         # atexit.register(cleanup_cache) 

#     def job(self):
#         print('hello job')


#     def start_command(self, message):
#         self.bot.reply_to(message, "Hello! I'm Grid Assistent Bot!") 
#         self.job()

#         schedule.every(my_params.interval_shedjule_step).seconds.do(self.job) 
#         while True:
#             schedule.run_pending()
#             time.sleep(5)

#     def start_bot(self):
#         @self.bot.message_handler(commands=['start'])
#         def handle_start(message):
#             # print('start comand')
#             self.start_command(message)
        
#         self.bot.infinity_polling()

# def main_tg_func():    
#     tg_api = Tg()
#     tg_api.start_bot()


# import os
# import time
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor

# class TgApi:
#     def __init__(self, api_token='6655474801:AAFCa1cf01z4zP-XQV6zMkBQkE2p_pY2ryA'):  
     
#         self.bot = Bot(token=api_token)
#         self.dp = Dispatcher(self.bot)
#         self.dp.register_message_handler(self.start_command, commands=['start'])
#         self.dp.register_message_handler(self.handler_text, content_types=types.ContentType.TEXT)
#         self.dp.register_message_handler(self.handler_voice, content_types=types.ContentType.VOICE)


#     async def start_command(self, message: types.Message):
  
#         try:
#             await message.reply("Привет!")
#         except:
#             pass


#     async def handler_text(self, message: types.Message) -> None:
#         # print('hello text')
#         response_text = 'sbkfbrkjh'
#         await message.answer(response_text)


#     async def handler_voice(self, message: types.Message) -> None:
#         pass


 

#     async def start_bot(self):
#         await self.dp.start_polling()

 
# def main():
  
#     tg_api = TgApi()
#     executor.start_polling(tg_api.dp, skip_updates=True)

# if __name__ == '__main__':
#     main()
