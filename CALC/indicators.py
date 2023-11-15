import talib
import pandas_ta as ta
from finta import TA
import math
from API_BINANCE.utils_api import UTILSS_API
from API_BINANCE.get_api import GETT_API

class OTHERS_CALC(UTILSS_API):
    def __init__(self) -> None:
        super().__init__()

    def calculate_pandas_atr(self, data, period=14):        
        data.sort_index(ascending=True, inplace=True) 
        atr = ta.atr(data['High'], data['Low'], data['Close'], timeperiod=period)  
        # atr = atr.iloc[-1]      
        atr = atr.dropna()
        atr = atr.rolling(window=period).mean().iloc[-1]
        return atr

    def calculate_pivot(self, symbol, data, period=10):
        # finta
        dataa = data.copy()
        piv_repl = {}
        piv = None
   
        if self.PIVOT_GENERAL_TYPE == 'Classic':
            piv = TA.PIVOT(dataa)
        elif self.PIVOT_GENERAL_TYPE == 'Fibonacci':
            piv = TA.PIVOT_FIB(dataa)

        latest_pivot = piv.iloc[-period:]
        pivot_mean = latest_pivot.mean()
        latest_pivot_dict = {
            'pp': pivot_mean['pivot'],
            'S1': pivot_mean['s1'],
            'S2': pivot_mean['s2'],
            'S3': pivot_mean['s3'],
            'S4': pivot_mean['s4'],
         
            'R1': pivot_mean['r1'],
            'R2': pivot_mean['r2'],
            'R3': pivot_mean['r3'],
            'R4': pivot_mean['r4']            
        }
        self.pivot_levels_type = 4

        piv_repl[symbol] = {
            f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}': latest_pivot_dict[f'S{self.pivot_levels_type}'],
            f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}': latest_pivot_dict[f'R{self.pivot_levels_type}']
        }

        return piv_repl

    def calculate_heikin_ashi(self, data, ratio=1.2):
        heiken_close, heiken_open, heiken_signal = None, None, 0

        data['Heiken_Close'] = (data['Open'] + data['Close'] + data['High'] + data['Low']) / 4
        heiken_close = data['Heiken_Close'].iat[-1]

        data['Heiken_Open'] = data['Open']
        heiken_open = data['Heiken_Open'].iat[-1]

        for i in range(1, len(data)):
            data.loc[i, 'Heiken_Open'] = (data['Heiken_Open'].iat[i-1] + data['Heiken_Close'].iat[i-1]) / 2

        data['Heiken_High'] = data[['High', 'Heiken_Open', 'Heiken_Close']].max(axis=1)
        data['Heiken_Low'] = data[['Low', 'Heiken_Open', 'Heiken_Close']].min(axis=1)
        data.dropna(inplace=True)

        if len(data) < 2:
            return None, None, 0

        PreviousHeikenBody = abs(data['Heiken_Open'].iat[-2] - data['Heiken_Close'].iat[-2])

        condition_up = (
            (data['Heiken_High'].iat[-2] - max(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2])) /
            PreviousHeikenBody > ratio and
            (min(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2]) - data['Heiken_Low'].iat[-2]) /
            PreviousHeikenBody > ratio and
            (data['Heiken_Open'].iat[-1] < data['Heiken_Close'].iat[-1] and
            data['Heiken_Low'].iat[-1] >= data['Heiken_Open'].iat[-1])
        )

        condition_down = (
            (data['Heiken_High'].iat[-2] - max(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2])) /
            PreviousHeikenBody > ratio and
            (min(data['Heiken_Open'].iat[-2], data['Heiken_Close'].iat[-2]) - data['Heiken_Low'].iat[-2]) /
            PreviousHeikenBody > ratio and
            (data['Heiken_Open'].iat[-1] > data['Heiken_Close'].iat[-1] and
            data['Heiken_High'].iat[-1] <= data['Heiken_Open'].iat[-1])
        )

        if condition_up:
            heiken_signal = 1
        elif condition_down:
            heiken_signal = -1
        else:
            heiken_signal = 0

        return heiken_close, heiken_open, heiken_signal 
    
    def calculate_ma_s(self, data):
        data.dropna(inplace=True)
        # data.head(10) 
        data["MA7"] = ta.sma(data['Close'], length=7)
        ma_7 = data["MA7"].iloc[-1]
        data["MA25"] = ta.sma(data['Close'], length=25)
        ma_25 = data["MA25"].iloc[-1]
        data["MA99"] = ta.sma(data['Close'], length=99)
        ma_99 = data["MA99"].iloc[-1]
        # data.dropna(inplace=True)
        return ma_7, ma_25, ma_99
    
    def calculate_rsi(self, data):
        data['RSI'] = ta.rsi(data['Close'], length=self.rsi_period)
        rsi = data["RSI"].iloc[-1]
        return rsi
    
    def calculate_ema_s(self, data):
        data.dropna(inplace=True)
        # data.head(10) 
        data["EMA10"] = ta.ema(data['Close'], length=10)
        ema_10 = data["EMA10"].iloc[-1]
        data["EMA30"] = ta.ema(data['Close'], length=30)
        ema_30 = data["EMA30"].iloc[-1]
        data.dropna(inplace=True)
        # return data
        # print(ema_10, ema_30)
        return ema_10, ema_30

    def calculate_grid_number(self, resistance, support, atr):
        pivot_substract = abs(resistance - support)
        atr_decimal = atr/self.grid_decimal
        grid_number = int(pivot_substract/atr_decimal) + 1
        return grid_number    

class TALIB_INDSS():
    def __init__(self) -> None:
        pass

    def calculate_adx(self, data, period=14):

        try:
            adx = talib.ADX(data['High'], data['Low'], data['Close'], timeperiod=period)
        except Exception as ex:
            print(ex)

        last_adx = adx.iloc[-1]
        
        return last_adx

    def calculate_bollinger_bands(self, data, period=20, num_std=2):
        upper_band, _, lower_band = None, None, None
        try:
            upper_band, _, lower_band = talib.BBANDS(data['Close'], timeperiod=period, nbdevup=num_std, nbdevdn=num_std)
            upper_band = upper_band.to_numpy()[-1]
            lower_band = lower_band.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_bollinger_bands: {ex}")
        return upper_band, lower_band

    def calculate_macd(self, data, fast_period=12, slow_period=26, signal_period=9):
        macd, signal = None, None
        try:
            macd, signal, _ = talib.MACD(data['Close'], fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
            macd = macd.to_numpy()[-1]
            signal = signal.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_macd: {ex}")
        return macd, signal

    def calculate_talib_atr(self, data, period=14):
        atr = None
        try:
            atr = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)
            atr = atr.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_atr: {ex}")
        return atr

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

# symbol = 'BIGTIMEUSDT'
# symbol = 'BTCUSDT'
# # symbol = 'XRPUSDT'
# get_apii = GETT_API()
# data = get_apii.get_klines(symbol)
# other_calcc = OTHERS_CALC()
# talib_inds = TALIB_INDSS()

# atr2 = other_calcc.calculate_pandas_atr(data)
# print(atr2)
# # atr1 = other_calcc.calculate_finta_atr(data)
# # print(atr1)
# atr3 = talib_inds.calculate_talib_atr(data)
# print(atr3)
# atr = (atr2+atr3) / 2
# print(atr)




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





# python -m CALC.indicators