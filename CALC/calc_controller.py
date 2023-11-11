from API_BINANCE.utils_api import UTILS_FOR_ORDERS
from IND.ind_1_strategy import IND_STRATEGY_1 
from IND.ind_2_strategy import IND_STRATEGY_2
# from IND.ta_inds import TA_INDSS
from IND.tv_inds import TV_INFO
import pandas_ta as ta
from finta import TA
import talib
from pparamss import STRATEGY_SET
# import pandas as pd

class CALC_ATR(STRATEGY_SET):
    def __init__(self) -> None:
         super().__init__()
                 
    def calculate_talib_atr(self, data, period=20):    
        # atr = None
        # try:
        #     atr = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)
        #     atr = atr.to_numpy()[-1]
        # except Exception as ex:
        #     print(f"Error in calculate_atr: {ex}")
        # return atr
        atr = None
        try:
            atr = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)
            atr = atr.dropna()            
            atr = atr.rolling(window=period).mean().iloc[-1]            
        except Exception as ex:
            print(f"Error in calculate_atr: {ex}")
        return atr
        
    def calculate_pandas_atr(self, data, period=20):
        # data = data.copy() 
        data.sort_index(ascending=True, inplace=True) 
        atr = ta.atr(data['High'], data['Low'], data['Close'], timeperiod=period)        
        atr = atr.dropna()
        atr = atr.rolling(window=period).mean().iloc[-1]
        return atr

    def calculate_finta_atr(self, data, period=20):
        # data = data.copy() 
        data.sort_index(ascending=True, inplace=True)  
        atr = TA.ATR(data, period=period)
        atr = atr.dropna()
        atr = atr.rolling(window=period).mean().iloc[-1]
        return atr    
    
    def grid_calc_func(self, resistance, support, atr):
        pivot_substract = abs(resistance - support)
        atr_decimal = atr/self.grid_decimal
        grid_number = int(pivot_substract/atr_decimal) + 1
        return grid_number
# //////////////////////////////////////////////////////////////////

class CALC_PIV(CALC_ATR):
    def __init__(self) -> None:
         super().__init__()
    
    def finta_pivot_with_period(self, symbol, data, period=10):
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

class CALC_MANAGER(UTILS_FOR_ORDERS, CALC_PIV, IND_STRATEGY_1, TV_INFO):

    def __init__(self) -> None:
        super().__init__()
        self.ind_strategy_2 = IND_STRATEGY_2()
        

    def find_the_best_coin(self, symbol, target):
        piv_info_repl = None
        direction = None
        resistance_piv, support_piv = None, None
        tp, sl = None, None
        if target == 'default_calc':
            top_coins = []
            top_coins = self.assets_filters()
            symbol = top_coins[0]
        else:
            pass          

        assets = []
        assets.append(symbol)    
        try: 
            data = self.get_klines(symbol)  
        except:
            return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

        # print(data)   

        if self.inds_source == 'tv':  
            all_coins_indicators = self.get_tv_steak_signals(assets)          
            if self.ind_strategy == 1:                
                direction = self.sigmals_handler_one(all_coins_indicators)
                direction = direction[0]['side'] 
                piv_info_repl = self.get_piv(symbol)
            elif self.ind_strategy == 2:               
                data_analysis = self.extract_tv_signals(all_coins_indicators)              
                direction = self.ind_strategy_2.sigmals_handler_two(assets, data_analysis)
                direction = direction[0]['side']                
                piv_info_repl = self.finta_pivot_with_period(symbol, data)
                self.pivot_levels_type = 4
            
        elif self.inds_source == 'ta':
            data_analysis = None            
            direction = self.ind_strategy_2.sigmals_handler_two(assets, data_analysis)
            direction = direction[0]['side'] 
            piv_info_repl = self.finta_pivot_with_period(symbol, data)
            self.pivot_levels_type = 4

        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}']
        atr2 = self.calculate_talib_atr(data)
        atr3 = self.calculate_pandas_atr(data)
        atr4 = self.calculate_finta_atr(data)
        atr = (atr2 + atr3 + atr4) / 3

        if direction == 'BUY' or 'F_BUY':
            tp, sl = resistance_piv + atr*0.03, support_piv - atr*0.015
        elif direction == 'SELL' or 'F_SELL':
            sl, tp = resistance_piv + atr*0.015, support_piv - atr*0.03
        
        grid_number = self.grid_calc_func(resistance_piv, support_piv, atr)

        return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

    def find_the_top_coin(self):
        top_coins = []        
        all_coins_indicators = []
        top_coins_updated = []
        top_coins = self.assets_filters()        
        if self.inds_source == 'tv' and self.ind_strategy == 1:
            all_coins_indicators = self.get_tv_steak_signals(top_coins)
            top_coins_updated = self.sigmals_handler_one(all_coins_indicators)

        elif self.inds_source == 'tv' and self.ind_strategy == 2:
            all_coins_indicators = self.get_tv_steak_signals(top_coins)
            data_analysis = self.extract_tv_signals(all_coins_indicators)              
            top_coins_updated = self.ind_strategy_2.sigmals_handler_two(top_coins, data_analysis)
            
        elif self.inds_source == 'ta':   
            data_analysis = None                  
            top_coins_updated = self.ind_strategy_2.sigmals_handler_two(top_coins, data_analysis)

        return top_coins_updated
        
# calc_controllerr = CALC_MANAGER()

# symbol = 'BTCUSDT'
# data = get_apii.get_klines(symbol)

# atr2 = calc_controllerr.calculate_talib_atr(data)
# atr3 = calc_controllerr.calculate_pandas_atr(data)
# atr4 = calc_controllerr.calculate_finta_atr(data)
# print(atr2)
# print(atr3)
# print(atr4)
# atr = (atr2 + atr3 + atr4) / 3
# print(atr)

# symbol = None
# target = 'default_calc'
# target = 'custom_calc'
# symbol = 'LINKUSDT'
# repl = calc_controllerr.find_the_best_coin(symbol, target)
# print(repl)

# top_coin = calc_controllerr.find_the_top_coin()
# print(top_coin)


# tv_piv = tv_infoo.get_piv(symbol)
# print(tv_piv)
# finta_piv = calc_controllerr.finta_pivot_with_period(symbol, data)
# print(finta_piv)


# top_coins = None
# symbol = "BTCUSDT"
# target = 'default_calc'
# top_coins = calc_controllerr.find_the_best_coin(symbol, target)
# print(top_coins)

# python -m CALC.calc_controller