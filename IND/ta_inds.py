import talib
# import pandas as pd
# import pandas_ta as ta
# import numpy as np
# from pparamss import my_params
# from API_BINANCE.get_api import get_apii
# from CALC.calc_controller import calc_controllerr

class TA_INDSS():
    def __init__(self) -> None:
        pass

    def calculate_adx(self, data, period=14):

        try:
            adx = talib.ADX(data['High'], data['Low'], data['Close'], timeperiod=period)
        except Exception as ex:
            print(ex)

        last_adx = adx.iloc[-1]
        
        return last_adx

    def calculate_sma(self, data, period=20):
        sma = None
        num_std = 2
        try:
            _, sma, _ = talib.BBANDS(data['Close'], timeperiod=period, nbdevup=num_std, nbdevdn=num_std)
            sma = sma.to_numpy()[-1]
        except Exception as ex:
            print(ex)
        return sma

    def calculate_bollinger_bands(self, data, period=20, num_std=2):
        upper_band, _, lower_band = None, None, None
        try:
            upper_band, _, lower_band = talib.BBANDS(data['Close'], timeperiod=period, nbdevup=num_std, nbdevdn=num_std)
            upper_band = upper_band.to_numpy()[-1]
            lower_band = lower_band.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_bollinger_bands: {ex}")
        return upper_band, lower_band

    def calculate_rsi(self, data, period=14):
        rsi = None
        try:
            rsi = talib.RSI(data['Close'], timeperiod=period)
            rsi.interpolate(method='linear', inplace=True)
            rsi = rsi.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_rsi: {ex}")
        return rsi

    def calculate_macd(self, data, fast_period=12, slow_period=26, signal_period=9):
        macd, signal = None, None
        try:
            macd, signal, _ = talib.MACD(data['Close'], fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
            macd = macd.to_numpy()[-1]
            signal = signal.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_macd: {ex}")
        return macd, signal

    # def calculate_atr(self, data, period=14):
    #     atr = None
    #     try:
    #         atr = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)
    #         atr = atr.to_numpy()[-1]
    #     except Exception as ex:
    #         print(f"Error in calculate_atr: {ex}")
    #     return atr

    def calculate_engulfing_patterns(self, data):
        engulfing = None
        try:
            engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
            engulfing = engulfing.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_engulfing_patterns: {ex}")
        return engulfing

    def calculate_doji(self, data):
        doji = None
        try:
            doji = talib.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
            doji = doji.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_doji: {ex}")
        return doji

    def calculate_stochastic_oscillator(self, data, k_period=14, d_period=3):
        slow_k, slow_d = None, None
        try:
            slow_k, slow_d = talib.STOCH(data['High'], data['Low'], data['Close'], fastk_period=k_period, slowk_period=k_period, slowd_period=d_period)
            slow_k = slow_k.to_numpy()[-1]
            slow_d = slow_d.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_stochastic_oscillator: {ex}")
        return slow_k, slow_d
    
# ta_iindss = TA_INDSS()

# symbol = 'BTCUSDT'
# data = get_apii.get_klines(symbol)
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



# # atr1 = calc_controllerr.calculate_atr(data)
# # print(atr1)
# atr2 = ta_iindss.calculate_atr(data)
# print(atr2)

# python -m IND.ta_inds