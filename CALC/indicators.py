import talib
import pandas_ta as ta
from finta import TA
import math
import numpy as np
from API_BINANCE.utils_api import UTILSS_API
from API_BINANCE.get_api import GETT_API

class OTHERS_CALC(UTILSS_API):
    def __init__(self) -> None:
        super().__init__()

    def calculate_pandas_steck_atr(self, data):        
        data.sort_index(ascending=True, inplace=True) 
        atr_data_data = []
        for i in range(40, len(data)):
            atr_data = ta.atr(data['High'].iloc[:i], data['Low'].iloc[:i], data['Close'].iloc[:i], timeperiod=i)                          
            atr_data = atr_data.dropna()
            last_atr = float(atr_data.iloc[-1])
            atr_data_data.append(last_atr)
        return atr_data_data
    
    def determine_pivot_type(self, atr_list, last_atr):
        pivot_type = None
        sorted_atr = sorted(atr_list)
        len_sorted_atr = len(sorted_atr)
        sort_grade = len_sorted_atr/4
        atr_index = [i for i, item in enumerate(sorted_atr) if float(item) == float(last_atr)][0]
        pivot_type = atr_index / sort_grade    
        pivot_type = math.ceil((pivot_type * 10) / 10) + 1
        if pivot_type > 5: pivot_type = 5
        return pivot_type
    
    def calculate_fibonacci_pivot_points(self, symbol, data):
        data = data.iloc[-100:] 
        latest_pivot_dict = {}
        piv_repl = {}
        try:
            high = data['High']
            low = data['Low']
            close = data['Close']
            
            pivot = (high + low + close) / 3
            # support1 = pivot - 0.382 * (high - low)
            # support2 = pivot - 0.618 * (high - low)
            # support3 = pivot - (high - low)
            # support3 = pivot - 1.382 * (high - low) 
            support1 = pivot - 1.618 * (high - low)
            support2 = pivot - 2.618 * (high - low)  
            support3 = pivot - 4.236 * (high - low)
            support4 = pivot - 6.854 * (high - low)
            support5 = pivot - 11.090 * (high - low)  
            # resistance1 = pivot + 0.382 * (high - low)
            # resistance2 = pivot + 0.618 * (high - low)
            # resistance3 = pivot + (high - low)
            # resistance4 = pivot + 1.382 * (high - low) 
            resistance1 = pivot + 1.618 * (high - low) 
            resistance2 = pivot + 2.618 * (high - low)
            resistance3 = pivot + 4.236 * (high - low)  
            resistance4 = pivot + 6.854 * (high - low)
            resistance5 = pivot + 11.090 * (high - low)          
            
            latest_pivot_dict = {
                'pp': pivot.iloc[-1],
                'S1': support1.iloc[-1],
                'S2': support2.iloc[-1],
                'S3': support3.iloc[-1],
                'S4': support4.iloc[-1], 
                'S5': support5.iloc[-1],  
                # 'S6': support6.iloc[-1],
                # 'S7': support7.iloc[-1],
                'R1': resistance1.iloc[-1],
                'R2': resistance2.iloc[-1],
                'R3': resistance3.iloc[-1],
                'R4': resistance4.iloc[-1], 
                'R5': resistance5.iloc[-1],
                # 'R6': resistance6.iloc[-1],
                # 'R7': resistance7.iloc[-1]   
            }
            # self.pivot_levels_type = 6  # Update the number of pivot levels
            piv_repl[symbol] = {
                f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}': latest_pivot_dict[f'S{self.pivot_levels_type}'],
                f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}': latest_pivot_dict[f'R{self.pivot_levels_type}']
            }
        except Exception as ex:
            print(ex)

        return piv_repl

    def calculate_classic_pivot_points(self, symbol, data):
        data = data.iloc[-100:]
        latest_pivot_dict = {}
        piv_repl = {} 
        try:
            high = data['High']
            low = data['Low']
            close = data['Close']

            pivot = (high + low + close) / 3
            # support1 = (2 * pivot) - high
            # support2 = pivot - (high - low)
            # support2 = pivot - 2 * (high - low)
            support1 = pivot - 3 * (high - low)
            support2 = pivot - 4 * (high - low)  
            support3 = pivot - 5 * (high - low)
            support4 = pivot - 6 * (high - low)
            support5 = pivot - 7 * (high - low)  
            # resistance1 = (2 * pivot) - low
            # resistance2 = pivot + (high - low)
            # resistance3 = pivot + 2 * (high - low)
            # resistance4 = pivot + 3 * (high - low)  
            resistance1 = pivot + 3 * (high - low)
            resistance2 = pivot + 4 * (high - low)
            resistance3 = pivot + 5 * (high - low)
            resistance4 = pivot + 6 * (high - low)
            resistance5 = pivot + 7 * (high - low)  
            
            latest_pivot_dict = {
                'pp': pivot.iloc[-1],
                'S1': support1.iloc[-1],
                'S2': support2.iloc[-1],
                'S3': support3.iloc[-1],
                'S4': support4.iloc[-1], 
                'S5': support5.iloc[-1],  
                # 'S6': support6.iloc[-1],
                # 'S7': support7.iloc[-1],
                'R1': resistance1.iloc[-1],
                'R2': resistance2.iloc[-1],
                'R3': resistance3.iloc[-1],
                'R4': resistance4.iloc[-1], 
                'R5': resistance5.iloc[-1],
                # 'R6': resistance6.iloc[-1],
                # 'R7': resistance7.iloc[-1]   
            }
            # self.pivot_levels_type = 4  # Update the number of pivot levels
            piv_repl[symbol] = {
                f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}': latest_pivot_dict[f'S{self.pivot_levels_type}'],
                f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}': latest_pivot_dict[f'R{self.pivot_levels_type}']
            }
        except Exception as ex:
            print(f"str31: {ex}")

        return piv_repl


    def calculate_manualy_pivot(self, symbol, data):
        piv = None
        if self.PIVOT_GENERAL_TYPE == 'Classic':
            piv = self.calculate_classic_pivot_points(symbol, data)
        elif self.PIVOT_GENERAL_TYPE == 'Fibonacci':
            piv = self.calculate_fibonacci_pivot_points(symbol, data)

        return piv

    def calculate_finta_pivot(self, symbol, data, period=50):
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

    def calculate_heikin_ashi(self, data, ratio=0.9):
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
            heiken_signal = 2
        elif condition_down:
            heiken_signal = 1
        else:
            heiken_signal = 0

        return heiken_close, heiken_open, heiken_signal   

    
    def detect_rsi_divergence(self, close_price_list, rsi_values):  
        # print(closes, rsi_values)  
        if np.mean(rsi_values[-4:-2]) < 50 and  np.mean(rsi_values[-2:] > 50 and rsi_values[-1] < 60) and np.mean(close_price_list[-4:-2]) < np.mean(close_price_list[-2:]):        
            return 2 
        elif np.mean(rsi_values[-4:-2]) > 50 and  np.mean(rsi_values[-2:] < 50 and rsi_values[-1] > 40) and np.mean(close_price_list[-4:-2]) > np.mean(close_price_list[-2:]):
            return 1
        else:       
            return 0   

    def calculate_grid_number(self, resistance, support, atr):
        pivot_substract = abs(resistance - support)
        atr_decimal = atr/self.grid_decimal
        grid_number = int(pivot_substract/atr_decimal) + 1
        return grid_number    

class PANDAS_TA_INDSS():
    def __init__(self) -> None:
        pass

    def calculate_bollinger_bands(self, data):
        dataBB_382 = ta.bbands(data.Close, length=30, std=1.382) 
        dataBB_382.dropna(inplace=True)
        dataBB_618 = ta.bbands(data.Close, length=30, std=1.618) 
        dataBB_618.dropna(inplace=True)
        data = data.join(dataBB_382)
        data = data.join(dataBB_618)
        # data.columns
        data.dropna(inplace=True)
        return data

    def calculate_rsi(self, data):
        data['RSI12'] = ta.rsi(data.Close, length=12)
        data.dropna(inplace=True)        
        return data
    
    def calculate_ema_s(self, data):
        data["EMA10"] = ta.ema(data['Close'], length=10)
        data.dropna(inplace=True)
        data["EMA30"] = ta.ema(data['Close'], length=30)        
        data.dropna(inplace=True)
        return data
    
    def calculate_pandas_atr(self, data, period=14):        
        data.sort_index(ascending=True, inplace=True)       
        data["ATR_PANDAS"] = ta.atr(data['High'], data['Low'], data['Close'], timeperiod=period)                          
        data = data.dropna()
        # last_atr = atr_data.iloc[-1]        
        return data
    
    def calculate_talib_atr(self, data, period=14):        
        try:
            data["ATR_TALIB"] = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)
            # atr = atr.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_atr: {ex}")
        return data

    def calculate_adx(self, data, period=14):
        data['ADX'] = talib.ADX(data['High'], data['Low'], data['Close'], timeperiod=period)       
        return data

    def calculate_ma_s(self, data):
        # data.head(10) 
        data["MA7"] = ta.sma(data['Close'], length=7)
        data.dropna(inplace=True)     

        data["MA20"] = ta.sma(data['Close'], length=25)
        data.dropna(inplace=True)

        data["MA25"] = ta.sma(data['Close'], length=25)
        data.dropna(inplace=True)

        data["MA50"] = ta.sma(data['Close'], length=99)
        data.dropna(inplace=True)

        data["MA99"] = ta.sma(data['Close'], length=99)
        data.dropna(inplace=True)
        
        return data

    def calculate_macd(self, data):
        data_macd = ta.macd(data.Close, fastperiod=12, slowperiod=26, signalperiod=9)
        data_macd.dropna(inplace=True)
        data = data.join(data_macd)
        return data
    
    def calculate_doji(self, data):
        try:
            data['Doji'] = talib.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
            # doji = doji.to_numpy()[-1]
        except Exception as ex:
            print(f"Error in calculate_doji: {ex}")
        return data


    
# iinds = OTHERS_CALC()
# iinds = TALIB_INDSS()
# get_apii = GETT_API()
# symbol = 'BTCUSDT'
# data = get_apii.get_klines(symbol, custom_period=None)
# # rsi6, rsi5, rsi4, rsi3, rsi2, rsi1 = iinds.calculate_rsi(data)
# # print(rsi6, rsi5, rsi4, rsi3, rsi2, rsi1)
# boll = iinds.calculate_bollinger_bands(data)
# print(boll)

# symbol = 'BIGTIMEUSDT'
# import pandas as pd
# import numpy as np
# symbol = 'BTCUSDT'
# # # symbol = 'XRPUSDT'
# get_apii = GETT_API()
# data = get_apii.get_klines(symbol, custom_period=1000)
# other_calcc = OTHERS_CALC()
# talib_inds = TALIB_INDSS()
# piv_finta = other_calcc.calculate_finta_pivot(symbol, data)
# piv_manualy = other_calcc.calculate_manualy_pivot(symbol, data)
# print(piv_finta)
# print(piv_manualy)



# python -m CALC.indicators