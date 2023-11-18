
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



# def calculate_pivot_points2(data):
#     pivot_points = {}
#     try:
#         high = data['High']
#         low = data['Low']
#         close = data['Close']
        
#         # Рассчитываем уровни Pivot Points
#         pivot_points['pivot'] = (high + low + close) / 3
#         pivot_points['support1'] = (2 * pivot_points['pivot']) - high
#         pivot_points['support2'] = pivot_points['pivot'] - (high - low)
#         pivot_points['support3'] = pivot_points['pivot'] - 2 * (high - low)
#         pivot_points['resistance1'] = (2 * pivot_points['pivot']) - low
#         pivot_points['resistance2'] = pivot_points['pivot'] + (high - low)
#         pivot_points['resistance3'] = pivot_points['pivot'] + 2 * (high - low)
#     except Exception as ex:
#         print(ex)

#     return pivot_points

# # Пример использования
# data = {
#     'High': [140, 145, 150, 135, 132],
#     'Low': [130, 135, 140, 125, 122],
#     'Close': [138, 142, 148, 133, 128]
# }

# pivot_points = calculate_pivot_points(data)
# print(pivot_points)
                #     'BB.lower': analysis.indicators['BB.lower'],
                #     'BB.upper': analysis.indicators['BB.upper'],

        # @self.bot.message_handler(func=lambda message: message.text == "CALC")
        # def auto_calc(message):            
        #     symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = None, None, None, None, None, None, None
        #     try:
        #         symbol, directioperiod
        #         pass
        #     try:
        #         self.bot.send_message(message.chat.id, f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nStop Loss: {sl}\nTake Profit: {tp}\nGrid numder : {grid_number}")
        #     except:
        #         pass

    # def calculate_manual_atr(self, data, period=20):
    #     data_slice = data[-period:]  # Создаем срез данных для последних 'period' значений

    #     true_ranges = []

    #     for i in range(1, len(data_slice)):
    #         high = data_slice['High'].iloc[i]
    #         low = data_slice['Low'].iloc[i]
    #         close = data_slice['Close'].iloc[i]
    #         true_range = max(abs(high - low), abs(high - close), abs(low - close))
    #         true_ranges.append(true_range)

    #     atr = sum(true_ranges) / len(true_ranges)  # Рассчитываем средний ATR для среза данных

    #     return atr

    # def calculate_manual_atr(self, data, period=20):
    #     true_ranges = []
    #     for i in range(1, len(data)):
    #         high = data['High'].iloc[i]
    #         low = data['Low'].iloc[i]
    #         close = data['Close'].iloc[i]
    #         true_range = max(abs(high - low), abs(high - close), abs(low - close))        
    #         true_ranges.append(true_range)
    #     atr = sum(true_ranges[-period:]) / period
    #     return atr



    # def finta_pivot(self, data):
    #     dataa = data.copy()
    #     piv_repl = {}
    #     piv = None
    #     piv = TA.PIVOT(dataa)

    #     latest_pivot = piv.iloc[-1]

    #     # Оформить их в словарь
    #     latest_pivot_dict = {
    #         'pp': latest_pivot['pivot'],
    #         'S1': latest_pivot['s1'],
    #         'S2': latest_pivot['s2'],
    #         'S3': latest_pivot['s3'],
    #         'S4': latest_pivot['s4'],
    #         'R1': latest_pivot['r1'],
    #         'R2': latest_pivot['r2'],
    #         'R3': latest_pivot['r3'],
    #         'R4': latest_pivot['r4']
    #     }
    #     my_params.pivot_levels_type = 3
    #     piv_repl[symbol] = {
    #         f'Pivot.M.Classic.S{my_params.pivot_levels_type}': latest_pivot_dict[f'S{my_params.pivot_levels_type}'],
    #         f'Pivot.M.Classic.R{my_params.pivot_levels_type}': latest_pivot_dict[f'R{my_params.pivot_levels_type}']
    #     }
    #     return piv_repl



    # def calculate_fibonacci_pivot_points(self, symbol, data):
    #     piv = {}
    #     try:
    #         high = data['High']
    #         low = data['Low']
    #         close = data['Close']
            
    #         # Рассчитываем уровни Pivot Points Фибоначчи
    #         pivot = (high + low + close) / 3
    #         support1 = pivot - 0.382 * (high - low)
    #         support2 = pivot - 0.618 * (high - low)
    #         support3 = pivot - (high - low)
    #         resistance1 = pivot + 0.382 * (high - low)
    #         resistance2 = pivot + 0.618 * (high - low)
    #         resistance3 = pivot + (high - low)

    #         piv = {
    #             'pp': pivot.iloc[-1],
    #             'S1': support1.iloc[-1],
    #             'S2': support2.iloc[-1],
    #             'S3': support3.iloc[-1],
    #             'R1': resistance1.iloc[-1],
    #             'R2': resistance2.iloc[-1],
    #             'R3': resistance3.iloc[-1]
    #         }
    #         piv[symbol] = {
    #             f'Pivot.M.Fibonacci.S{my_params.pivot_levels_type}': piv[f'S{my_params.pivot_levels_type}'],
    #             f'Pivot.M.Fibonacci.R{my_params.pivot_levels_type}': piv[f'R{my_params.pivot_levels_type}']
    #         }
    #     except Exception as ex:
    #         print(ex)

    #     return piv

    # def calculate_classsic_pivot_points(self, symbol, data):
    #     piv = {}
    #     piv_repl = {} 
    #     try:
    #         high = data['High']
    #         # print(high
    #         # )
    #         low = data['Low']
    #         # print(low)
    #         close = data['Close']
    #         # print(close)

    #         pivot = (high + low + close) / 3
    #         support1 = (2 * pivot) - high
    #         support2 = pivot - (high - low)
    #         support3 = pivot - 2 * (high - low)
    #         resistance1 = (2 * pivot) - low
    #         resistance2 = pivot + (high - low)
    #         resistance3 = pivot + 2 * (high - low)
            
    #         piv = {
    #             'pp': pivot.iloc[-1],
    #             'S1': support1.iloc[-1],
    #             'S2': support2.iloc[-1],
    #             'S3': support3.iloc[-1],
    #             'R1': resistance1.iloc[-1],
    #             'R2': resistance2.iloc[-1],
    #             'R3': resistance3.iloc[-1]
    #         }
    #         my_params.pivot_levels_type = 3
    #         piv_repl[symbol] = {
    #             f'Pivot.M.Classic.S{my_params.pivot_levels_type}': piv[f'S{my_params.pivot_levels_type}'],
    #             f'Pivot.M.Classic.R{my_params.pivot_levels_type}': piv[f'R{my_params.pivot_levels_type}']
    #         }
    #     except Exception as ex:
    #         print(f"str31: {ex}")

    #     return piv_repl

    # def piv_controller(self, symbol, data):
    #     piv = None
    #     if my_params.PIVOT_GENERAL_TYPE == 'Classic':
    #         piv = self.calculate_classsic_pivot_points(symbol, data)
    #     elif my_params.PIVOT_GENERAL_TYPE == 'Fibonacci':
    #         piv = self.calculate_fibonacci_pivot_points(symbol, data)

    #     return piv




        # print(trende_sign)

        # if not my_params.NEUTRAL_FLAG:                            
        #     if trende_sign == 'U':
        #         if my_params.BUNCH_VARIANT == 1:
        #             current_bunch = ['bband_flag', 'macd_strong_flag', 'U']
        #         elif my_params.BUNCH_VARIANT == 2:
        #             current_bunch = ['bband_flag', 'macd_lite_flag', 'rsi_flag', 'U']
        #         # current_bunch = ['bband_flag', 'macd_lite_flag', 'U']            
                
        #     if trende_sign == 'D':
        #         if my_params.BUNCH_VARIANT == 1:
        #             current_bunch = ['bband_flag', 'macd_strong_flag', 'D']
        #         elif my_params.BUNCH_VARIANT == 2:
        #             current_bunch = ['bband_flag', 'macd_lite_flag', 'rsi_flag', 'D']
        #         # current_bunch = ['bband_flag', 'macd_lite_flag', 'D']            
            
        # if trende_sign == 'F':
        #     if my_params.BUNCH_VARIANT == 1:               
        #         current_bunch = ['macd_strong_flag', 'stoch_flag', 'F']
        #     elif my_params.BUNCH_VARIANT == 2:
        #         current_bunch = ['macd_lite_flag', 'stoch_flag', 'F']

        # buy_signal, sell_signal = bunch_handler_func(close_price, upper, lower, macd, signal, rsi, fastk, slowk, current_bunch)
    

# self.SLIPPAGE_COEFFICIENT = 0.005  # Коэффициент погрешности 0.5%   
# self.interval_shedjule_step = 30


# def get_ta_signals(top_coins):
#     klines_data = []
#     for symbol in top_coins:
#         # print(symbol)
#         try:
#             kline_data = get_apii.get_klines(symbol)
#             # print(kline_data)
#             close_price = kline_data['Close'].iloc[-1]
#             adx = ta_iindss.calculate_adx(kline_data)
#             sma20 = ta_iindss.calculate_sma(kline_data)
#             upper, lower = ta_iindss.calculate_bollinger_bands(kline_data)                 
#             macd, signal = ta_iindss.calculate_macd(kline_data)
#             rsi = ta_iindss.calculate_rsi(kline_data)
#             print(f"rsi:  {rsi}")
#             fastk, slowk = ta_iindss.calculate_stochastic_oscillator(kline_data) 
#             engulfing = ta_iindss.calculate_engulfing_patterns(kline_data)
#             doji = ta_iindss.calculate_doji(kline_data)        
              
#             klines_data.append({
#                 'symbol': symbol,
#                 'close_price': close_price,
#                 'ADX': adx, 
#                 'SMA20': sma20, 
#                 "BB.upper": upper,
#                 "BB.lower": lower,
#                 "MACD.macd": macd,
#                 "MACD.signal": signal,
#                 "RSI": rsi,
#                 "Stoch.K": fastk,
#                 "Stoch.D": slowk,
#                 "Engulfing": engulfing, 
#                 "Doji": doji
#                 })
#         except Exception as ex:
#             # print(ex) 
#             pass

#     return klines_data

        # atr = None
        # try:
        #     atr = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)
        #     atr = atr.dropna()            
        #     atr = atr.rolling(window=period).mean().iloc[-1]            
        # except Exception as ex:
        #     print(f"Error in calculate_atr: {ex}")
        # return atr


    # def calculate_pandas_atr(self, data, period=20):
    #     # data = data.copy() 
    #     data.sort_index(ascending=True, inplace=True) 
    #     atr = ta.atr(data['High'], data['Low'], data['Close'], timeperiod=period)        
    #     atr = atr.dropna()
    #     atr = atr.rolling(window=period).mean().iloc[-1]
    #     return atr

    # def calculate_finta_atr(self, data, period=20):
    #     # data = data.copy() 
    #     data.sort_index(ascending=True, inplace=True)  
    #     atr = TA.ATR(data, period=period)
    #     atr = atr.dropna()
    #     atr = atr.rolling(window=period).mean().iloc[-1]
    #     return atr  


    # def calculate_heikin_ashi(self, data):
    #     data['Heiken_Close'] = (data['Open'] + data['Close'] + data['High'] + data['Low']) / 4
    #     data['Heiken_Open'] = data['Open']
    #     for i in range(1, len(data)):
    #         data['Heiken_Open'].iloc[i] = (data['Heiken_Open'].iloc[i-1] + data['Heiken_Close'].iloc[i-1]) / 2

    #     data['Heiken_High'] = data[['High', 'Heiken_Open', 'Heiken_Close']].max(axis=1)
    #     data['Heiken_Low'] = data[['Low', 'Heiken_Open', 'Heiken_Close']].min(axis=1)
    #     data.dropna(inplace=True)
    #     data.head(10)
    #     PreviousHeikenBody = math.fabs(data['Heiken_Open'].iloc[-2] - data['Heiken_Close'].iloc[-2])
    #     ratio = 1.5
    #     if (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]))
    #         / PreviousHeikenBody > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2])
    #         / PreviousHeikenBody > ratio and
    #         (data['Heiken_Open'].iloc[-1] < data['Heiken_Close'].iloc[-1] and data['Heiken_Low'].iloc[-1] >= data['Heiken_Open'].iloc[-1])
    #     ):
    #         return 1            

    #     elif (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]))
    #         / PreviousHeikenBody > ratio > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2])
    #         / PreviousHeikenBody > ratio > ratio and
    #         (data['Heiken_Open'].iloc[-1] > data['Heiken_Close'].iloc[-1] and data['Heiken_High'].iloc[-1] <= data['Heiken_Open'].iloc[-1])
    #     ):
    #         return -1

    #     else:
    #         return 0        
    

        # if 'heikin_ashi_flag' in current_bunch:
        #     try:
        #         buy_heikin_ashi_signal, sell_heikin_ashi_signal = False, False
        #         heiken_close, heiken_open, heiken_signal = None, None, 0
        #         ema_10, ema_30 = None, None
        #         rsi_12 = None
            
        #         ema_10, ema_30 = self.calculate_ema_s(kline_data)
        #         # print(ema_10, ema_30)
        #         rsi_12 = self.calculate_rsi_12(kline_data)
        #         # print(rsi_12)
        #         heiken_close, heiken_open, heiken_signal = self.calculate_heikin_ashi(kline_data)
        #         # print(heiken_close, heiken_open, heiken_signal)
        #         buy_heikin_ashi_signal = (ema_10 > ema_30) and (heiken_open < ema_10) and (heiken_close > ema_10) and (heiken_signal == 1) and (rsi_12 > 50)           
        #         sell_heikin_ashi_signal = (ema_10 < ema_30) and (heiken_open > ema_10) and (heiken_close < ema_10) and (heiken_signal == -1) and (rsi_12 < 50)
        #         if buy_heikin_ashi_signal:
        #             return 'BUY'
        #         if sell_heikin_ashi_signal: 
        #             return 'SELL'
        #     except Exception as ex:
        #         print(ex)            

        #     return total_signal


    # def calculate_heikin_ashi(self, data, ratio=1.5):
    #     heiken_close, heiken_open, heiken_signal = None, None, 0

    #     data['Heiken_Close'] = (data['Open'] + data['Close'] + data['High'] + data['Low']) / 4
    #     heiken_close = data['Heiken_Close'].iloc[-1]

    #     data['Heiken_Open'] = data['Open']
    #     heiken_open = data['Heiken_Open'].iloc[-1]

    #     for i in range(1, len(data)):
    #         data.loc[i, 'Heiken_Open'] = (data['Heiken_Open'].iloc[i-1] + data['Heiken_Close'].iloc[i-1]) / 2

    #     data['Heiken_High'] = data[['High', 'Heiken_Open', 'Heiken_Close']].max(axis=1)
    #     data['Heiken_Low'] = data[['Low', 'Heiken_Open', 'Heiken_Close']].min(axis=1)
    #     data.dropna(inplace=True)

    #     PreviousHeikenBody = abs(data['Heiken_Open'].iloc[-2] - data['Heiken_Close'].iloc[-2])

    #     if (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2])) /
    #         PreviousHeikenBody > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2]) /
    #         PreviousHeikenBody > ratio and
    #         (data['Heiken_Close'].iloc[-1] > data['Heiken_Open'].iloc[-1])
    #     ):
    #         heiken_signal = 1
    #     elif (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2])) /
    #         PreviousHeikenBody > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2]) /
    #         PreviousHeikenBody > ratio and
    #         (data['Heiken_Close'].iloc[-1] < data['Heiken_Open'].iloc[-1])
    #     ):
    #         heiken_signal = -1
    #     else:
    #         heiken_signal = 0

    #     return heiken_close, heiken_open, heiken_signal

# def calculate_heikin_ashi(self, data, ratio=1.2):
#     heiken_close, heiken_open, heiken_signal = None, None, 0

#     data['Heiken_Close'] = (data['Open'] + data['Close'] + data['High'] + data['Low']) / 4
#     heiken_close = data['Heiken_Close'].iloc[-1]

#     data['Heiken_Open'] = data['Open']
#     heiken_open = data['Heiken_Open'].iloc[-1]

#     for i in range(1, len(data)):
#         data.loc[i, 'Heiken_Open'] = (data['Heiken_Open'].iloc[i-1] + data['Heiken_Close'].iloc[i-1]) / 2

#     data['Heiken_High'] = data[['High', 'Heiken_Open', 'Heiken_Close']].max(axis=1)
#     data['Heiken_Low'] = data[['Low', 'Heiken_Open', 'Heiken_Close']].min(axis=1)
#     data.dropna(inplace=True)

#     PreviousHeikenBody = abs(data['Heiken_Open'].iloc[-2] - data['Heiken_Close'].iloc[-2])

#     if (
#         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2])) /
#         PreviousHeikenBody > ratio and
#         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2]) /
#         PreviousHeikenBody > ratio and
#         (data['Heiken_Open'].iloc[-1] < data['Heiken_Close'].iloc[-1] and
#          data['Heiken_Low'].iloc[-1] >= data['Heiken_Open'].iloc[-1])
#     ):
#         heiken_signal = 1
#     elif (
#         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2])) /
#         PreviousHeikenBody > ratio and
#         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2]) /
#         PreviousHeikenBody > ratio and
#         (data['Heiken_Open'].iloc[-1] > data['Heiken_Close'].iloc[-1] and
#          data['Heiken_High'].iloc[-1] <= data['Heiken_Open'].iloc[-1])
#     ):
#         heiken_signal = -1
#     else:
#         heiken_signal = 0

#     return heiken_close, heiken_open, heiken_signal

    # def calculate_heikin_ashi(self, data):
    #     data['Heiken_Close'] = (data['Open'] + data['Close'] + data['High'] + data['Low']) / 4
    #     data['Heiken_Open'] = data['Open']
    #     for i in range(1, len(data)):
    #         data['Heiken_Open'].iloc[i] = (data['Heiken_Open'].iloc[i-1] + data['Heiken_Close'].iloc[i-1]) / 2

    #     data['Heiken_High'] = data[['High', 'Heiken_Open', 'Heiken_Close']].max(axis=1)
    #     data['Heiken_Low'] = data[['Low', 'Heiken_Open', 'Heiken_Close']].min(axis=1)
    #     data.dropna(inplace=True)
    #     data.head(10)
    #     PreviousHeikenBody = math.fabs(data['Heiken_Open'].iloc[-2] - data['Heiken_Close'].iloc[-2])
    #     ratio = 1.5
    #     if (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]))
    #         / PreviousHeikenBody > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2])
    #         / PreviousHeikenBody > ratio and
    #         (data['Heiken_Open'].iloc[-1] < data['Heiken_Close'].iloc[-1] and data['Heiken_Low'].iloc[-1] >= data['Heiken_Open'].iloc[-1])
    #     ):
    #         return 1            

    #     elif (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]))
    #         / PreviousHeikenBody > ratio > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2])
    #         / PreviousHeikenBody > ratio > ratio and
    #         (data['Heiken_Open'].iloc[-1] > data['Heiken_Close'].iloc[-1] and data['Heiken_High'].iloc[-1] <= data['Heiken_Open'].iloc[-1])
    #     ):
    #         return -1

    #     else:
    #         return 0   


        # if 'heikin_ashi_flag' in current_bunch:
        #     print('heikin_ashi_flag')
        #     try:
        #         buy_heikin_ashi_signal, sell_heikin_ashi_signal = False, False
        #         heiken_signal = 0
        #         _, _, heiken_signal = self.calculate_heikin_ashi(kline_data)   
        #         print(heiken_signal)             
        #         buy_heikin_ashi_signal = heiken_signal == 1
        #         sell_heikin_ashi_signal = heiken_signal == -1
        #         signals_sum.append((buy_heikin_ashi_signal, sell_heikin_ashi_signal))
        #     except Exception as ex:
        #         print(ex) 


    # def calculate_rsi(self, data, period=14):
    #     rsi = None
    #     try:
    #         rsi = talib.RSI(data['Close'], timeperiod=period)
    #         rsi.interpolate(method='linear', inplace=True)
    #         rsi = rsi.to_numpy()[-1]
    #     except Exception as ex:
    #         print(f"Error in calculate_rsi: {ex}")
    #     return rsi


        # if self.BUNCH_VARIANT == 7:
        #     if len(signals_sum) != 0:
        #         if buy_signals_counter == len(signals_sum):
        #             total_signal = 'BUY'
        #         elif sell_signals_counter == len(signals_sum):
        #             total_signal = 'SELL'


    # def calculate_engulfing_patterns(self, data):
    #     engulfing = None
    #     try:
    #         engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
    #         engulfing = engulfing.to_numpy()[-1]
    #     except Exception as ex:
    #         print(f"Error in calculate_engulfing_patterns: {ex}")
    #     return engulfing

                # if close_price > sma25 and close_price > sma7 and doji == 0:
                #     if self.strong_trande_sign:
                #         close_price > sma99
                #         return "U"
                #     else:
                #         return "U"
                # elif close_price < sma25 and close_price < sma7 and doji == 0:
                #     return "D"
                # else:
                #     return "F"


    # def calculate_sma(self, data, period=20):
    #     sma = None
    #     num_std = 2
    #     try:
    #         _, sma, _ = talib.BBANDS(data['Close'], timeperiod=period, nbdevup=num_std, nbdevdn=num_std)
    #         sma = sma.to_numpy()[-1]
    #     except Exception as ex:
    #         print(ex)
    #     return sma

# def calculate_heikin_ashi(self, data, ratio=1.2):
#     heiken_close, heiken_open, heiken_signal = None, None, 0

#     data['Heiken_Close'] = (data['Open'] + data['Close'] + data['High'] + data['Low']) / 4
#     heiken_close = data['Heiken_Close'].iat[-1]

#     data['Heiken_Open'] = data['Open']
#     heiken_open = data['Heiken_Open'].iat[-1]

#     for i in range(1, len(data)):
#         data.loc[i, 'Heiken_Open'] = (data['Heiken_Open'].iat[i-1] + data['Heiken_Close'].iat[i-1]) / 2

#     data['Heiken_High'] = data[['High', 'Heiken_Open', 'Heiken_Close']].max(axis=1)
#     data['Heiken_Low'] = data[['Low', 'Heiken_Open', 'Heiken_Close']].min(axis=1)
#     data.dropna(inplace=True)

#     if len(data) < 2:
#         return None, None, 0

#     PreviousHeikenBody = abs(data['Heiken_Open'].iat[-2] - data['Heiken_Close'].iat[-2])

#     condition_up = (
#         (data['Heiken_High'].iat[-2] - max(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2])) /
#         PreviousHeikenBody > ratio and
#         (min(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2]) - data['Heiken_Low'].iat[-2]) /
#         PreviousHeikenBody > ratio and
#         (data['Heiken_Open'].iat[-1] < data['Heiken_Close'].iat[-1] and
#         data['Heiken_Low'].iat[-1] >= data['Heiken_Open'].iat[-1])
#     )

#     condition_down = (
#         (data['Heiken_High'].iat[-2] - max(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2])) /
#         PreviousHeikenBody > ratio and
#         (min(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2]) - data['Heiken_Low'].iat[-2]) /
#         PreviousHeikenBody > ratio and
#         (data['Heiken_Open'].iat[-1] > data['Heiken_Close'].iat[-1] and
#         data['Heiken_High'].iat[-1] <= data['Heiken_Open'].iat[-1])
#     )

#     if condition_up:
#         heiken_signal = 1
#     elif condition_down:
#         heiken_signal = -1
#     else:
#         heiken_signal = 0

#     return heiken_close, heiken_open, heiken_signal

     
    # def calculate_heikin_ashi(self, data, ratio=1.2):
    #     heiken_close, heiken_open, heiken_signal = None, None, 0

    #     data['Heiken_Close'] = (data['Open'] + data['Close'] + data['High'] + data['Low']) / 4
    #     heiken_close = data['Heiken_Close'].iloc[-1]

    #     data['Heiken_Open'] = data['Open']
    #     heiken_open = data['Heiken_Open'].iloc[-1]

    #     for i in range(1, len(data)):
    #         data.loc[i, 'Heiken_Open'] = (data['Heiken_Open'].iloc[i-1] + data['Heiken_Close'].iloc[i-1]) / 2

    #     data['Heiken_High'] = data[['High', 'Heiken_Open', 'Heiken_Close']].max(axis=1)
    #     data['Heiken_Low'] = data[['Low', 'Heiken_Open', 'Heiken_Close']].min(axis=1)
    #     data.dropna(inplace=True)

    #     PreviousHeikenBody = abs(data['Heiken_Open'].iloc[-2] - data['Heiken_Close'].iloc[-2])

    #     if (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2])) /
    #         PreviousHeikenBody > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2]) /
    #         PreviousHeikenBody > ratio and
    #         (data['Heiken_Open'].iloc[-1] < data['Heiken_Close'].iloc[-1] and
    #         data['Heiken_Low'].iloc[-1] >= data['Heiken_Open'].iloc[-1])
    #     ):
    #         heiken_signal = 1
    #     elif (
    #         (data['Heiken_High'].iloc[-2] - max(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2])) /
    #         PreviousHeikenBody > ratio and
    #         (min(data['Heiken_Open'].iloc[-2], data['Heiken_Close'].iloc[-2]) - data['Heiken_Low'].iloc[-2]) /
    #         PreviousHeikenBody > ratio and
    #         (data['Heiken_Open'].iloc[-1] > data['Heiken_Close'].iloc[-1] and
    #         data['Heiken_High'].iloc[-1] <= data['Heiken_Open'].iloc[-1])
    #     ):
    #         heiken_signal = -1
    #     else:
    #         heiken_signal = 0

    #     return heiken_close, heiken_open, heiken_signal


    # def __init__(self) -> None:
    #     super().__init__()
    #     self.tg_api_token = os.getenv("TG_API_TOKEN", "")

    #     # if not self.test_flag:
    #     self.api_key  = os.getenv("BINANCE_API_PUBLIC_KEY_REAL", "")
    #     self.api_secret = os.getenv("BINANCE_API_PRIVATE_KEY_REAL", "")
    #         # print(self.api_key, self.api_secret)

    #     # else:
    #     #     if self.market == 'spot':
    #     #         self.api_key  = os.getenv(f"BINANCE_API_PUBLIC_KEY_{self.market.upper()}_TEST", "")
    #     #         self.api_secret = os.getenv(f"BINANCE_API_PRIVATE_KEY_{self.market.upper()}_TEST", "")

    #     #     if self.market == 'futures':
    #     #         self.api_key  = os.getenv(f"BINANCE_API_PUBLIC_KEY_{self.market.upper()}_TEST", "")
    #     #         self.api_secret = os.getenv(f"BINANCE_API_PRIVATE_KEY_{self.market.upper()}_TEST", "")    
        
    #     # print(self.api_key)
    #     # print(self.api_secret)
    #     # print(self.tg_api_token)
    #     self.header = {
    #         'X-MBX-APIKEY': self.api_key
    #     }



    # def calculate_finta_atr(self, data, period=20):
    #     # data = data.copy() 
    #     data.sort_index(ascending=True, inplace=True)  
    #     atr = TA.ATR(data, period=period)
    #     atr = atr.iloc[-1]
    #     # atr = atr.dropna()
    #     # atr = atr.rolling(window=period).mean().iloc[-1]
    #     return atr 


# atr2 = other_calcc.calculate_pandas_atr(data)
# print(atr2)
# # atr1 = other_calcc.calculate_finta_atr(data)
# # print(atr1)
# atr3 = talib_inds.calculate_talib_atr(data)
# print(atr3)
# atr = (atr2+atr3) / 2
# print(atr)


# Применяем функции

# pivot_levels = calculate_pivot_levels(atr_values)
# last_atr = atr_values.iloc[-1]

# pivot_type = determine_pivot_type(last_atr, pivot_levels)

# print(f"ATR Values:\n{atr_values}\n")
# print(f"Pivot Levels:\n{pivot_levels}\n")
# print(f"Last ATR: {last_atr}\n")
# print(f"Determined Pivot Type: {pivot_type}")







# a = other_calcc.calculate_heikin_ashi(data)
# print(a)
# a, b = other_calcc.calculate_ema_s(data)
# print(a,b)
# a, b, c = other_calcc.calculate_ma_s(data)
# rsi_12 = other_calcc.calculate_rsi_12(data)
# print(rsi_12)
# print(a,b,c)



# f, s = ta_iindss.calculate_stochastic_oscillator(data)
# print(f, s)
# rsi = None
# rsi = ta_iindss.calculate_rsi(data)
# macd = ta_iindss.calculate_macd(data)
# engulfing = ta_iindss.calculate_engulfing_patterns(data)
# doji = ta_iindss.calculate_doji(data)
# print(rsi)
# print(macd)
# print(engulfing)
# print(doji)



        # # Print or use the values and flags as needed
        # print("Max High:", max_high)
        # print("Min Low:", min_low)
        # print("Max High Flag:", max_high_flag)
        # print("Min Low Flag:", min_low_flag)

        # # Continue with your code...

        # @bot.message_handler(func=lambda message: message.text == "CALC")
        # def calc_input(message):
        #     response_message = "Please choice a way of calculation:\nDefault: 1;\nCustom: 2;" 
        #     message.text = self.connector_func(bot, message, response_message)
        #     self.calc_flag = True

        # @bot.message_handler(func=lambda message: message.text.strip() == "1" and self.calc_flag)
        # def default_calc(message):
        #     symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = None, None, None, None, None, None, None
        #     try:
        #         symbol = None
        #         target = 'default_calc'
        #         self.calc_flag = False  
        #         symbol, direction, resistance_piv, support_piv, grid_number, tp, sl = self.find_the_best_coin(symbol, target)                
        #     except:
        #         pass
        #     try:
        #         response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
        #         message.text = self.connector_func(bot, message, response_message)  
                        
        #     except Exception as ex:
        #         print(ex)  


    # # ///////////////////////////////////////////////
    # def update_time_temps(self, new_kline_time, new_time_frame, new_end_date, new_klines_period): 
    #     self.KLINE_TIME, self.TIME_FRAME = int(new_kline_time), new_time_frame.strip().lower()
    #     self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
    #     new_end_date = tuple(new_end_date)
    #     self.end_date = datetime(new_end_date[0], new_end_date[1], new_end_date[2])        
    #     self.KLINES_PERIOD = int(new_klines_period)    
    #     # ///////////////////////////////////////////////////////////////////////////

        
    # def update_ind_params(self, new_b_bband_q, new_s_bband_q, new_b_rsi_lev, new_s_rsi_lev, new_b_macd__q, new_s_macd_q, new_b_stoch_q, new_s_stoch_q):
    #     self.b_bband_q, self.s_bband_q = new_b_bband_q, new_s_bband_q
    #     self.b_rsi_lev, self.s_rsi_lev = new_b_rsi_lev, new_s_rsi_lev
    #     self.b_macd_q, self.s_macd_q = new_b_macd__q, new_s_macd_q
    #     self.b_stoch_q, self.s_stoch_q = new_b_stoch_q, new_s_stoch_q


    # def update_filter_set(self, new_slice_volun_pairs, new_slice_volatility, new_min_filter_price, new_max_filter_price, new_problem_pairs):       
    #     self.SLICE_VOLUME_PAIRS = new_slice_volun_pairs
    #     self.SLICE_VOLATILITY = new_slice_volatility
    #     self.MIN_FILTER_PRICE = new_min_filter_price 
    #     self.MAX_FILTER_PRICE = new_max_filter_price 
    #     self.problem_pairs = new_problem_pairs 

    # def trends_defender(self, close_price, adx, sma7, sma25, sma99, doji):
    #     try:
    #         u_conditions = [close_price > sma7, close_price > sma25, doji == 0]
    #         d_conditions = [close_price < sma7, close_price < sma25, doji == 0]
    #         if self.strong_trande_sign:
    #             u_conditions.append(close_price > sma99)
    #             d_conditions.append(close_price < sma99)

    #         if adx > 25:
    #             u_condition_met = all(u_conditions)
    #             d_condition_met = all(d_conditions)

    #             if u_condition_met:
    #                 return "U"
    #             elif d_condition_met:
    #                 return "D"
    #             else:
    #                 return "F"
    #         else:
    #             return "F"
    #     except Exception as ex:
    #         print(f"Error in trends_defender: {ex}")
    #         return None

    # def update_strategy_set(self, new_ind_strategy, new_inds_source, new_BUNCH_VARIANT, new_pivot_gen_type, new_pivot_levels_type, new_grid_decimal):
    #     self.ind_strategy = new_ind_strategy       
    #     self.inds_source = new_inds_source         
    #     self.BUNCH_VARIANT = new_BUNCH_VARIANT
    #     self.PIVOT_GENERAL_TYPE = new_pivot_gen_type
    #     self.pivot_levels_type = new_pivot_levels_type
    #     self.grid_decimal = new_grid_decimal



    # def update_main_params(self, new_market, new_test_flag=False):
    #     self.market = new_market
    #     self.test_flag = new_test_flag

        # super().update_main_params(new_market)
        # self.init_urls()


# Индикаторы для Бокового Рынка (Флета):
# Bollinger Bands (Полосы Боллинджера): В боковом рынке цена часто колеблется между верхней и нижней полосами, что может предоставить сигналы о возможных точках разворота.

# RSI (Индекс относительной силы): RSI может помочь идентифицировать перекупленные или перепроданные условия. В боковом рынке цены могут часто возвращаться к среднему значению RSI.

# Moving Averages (Скользящие средние): Когда рынок находится в флете, цена может пересекать скользящие средние, что может служить сигналом о возможном развороте или продолжении флета.

# MACD (Схождение/Расхождение скользящих средних): В боковом рынке, когда цена не имеет явного тренда, сигналы MACD о схождении и расхождении могут быть особенно важными.

# Индикаторы для Трендового Рынка:
# Трендовые линии и каналы: В трендовом рынке важно отмечать и рисовать уровни поддержки и сопротивления, которые могут помочь определить тренд.

# Parabolic SAR (Параболическая SAR): Этот индикатор может предоставить сигналы о направлении тренда и моментах его изменения.

# ADX (Средний индикатор направленности): Индикатор ADX может использоваться для измерения силы тренда.

# Ichimoku Cloud (Облако Ишимоку): Помогает определить направление тренда и области поддержки/сопротивления.

# Осцилляторы Momentum (например, ROC): Могут предоставить сигналы о силе текущего тренда.





            # if 'macd_strong_flag' in current_bunch:
            #     # print('mskrjbgv')
            #     macd, signal = self.calculate_macd(kline_data)
            #     buy_strong_macd_signal = (macd > signal * self.b_macd_q) and (macd < 0)
            #     sell_strong_macd_signal = (macd < signal * self.s_macd_q) and (macd > 0)
            #     signals_sum.append((buy_strong_macd_signal, sell_strong_macd_signal))


            # if 'stoch_flag' in current_bunch:
            #     fastk, slowk = self.calculate_stochastic_oscillator(kline_data)
            #     buy_stoch_signal = (fastk > slowk) and (fastk < self.b_stoch_q)
            #     sell_stoch_signal = (fastk < slowk) and (fastk > self.s_stoch_q)
            #     signals_sum.append((buy_stoch_signal, sell_stoch_signal))

