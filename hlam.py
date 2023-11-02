
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

