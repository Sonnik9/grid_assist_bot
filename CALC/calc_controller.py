from pparamss import my_params
from API_BINANCE.get_api import get_apii
from API_BINANCE.utils_api import utils_for_orderss
from IND.ind_1_strategy import sigmals_handler_one 
from IND.ind_2_strategy import sigmals_handler_two, get_ta_signals
from IND.ta_inds import ta_iindss
from IND.tv_inds import tv_infoo
import pandas_ta as ta
from finta import TA
import talib
import pandas as pd

class CALC_ATR():
    def __init__(self) -> None:
         pass
        
    def calculate_talib_atr(self, data, period=20):
        atr = None
        try:
            atr = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)
            atr = atr.dropna()            
            atr = atr.rolling(window=period).mean().iloc[-1]            
        except Exception as ex:
            print(f"Error in calculate_atr: {ex}")
        return atr
        
    def calculate_pandas_atr(self, data, period=20):
        data = data.copy() 
        data.sort_index(ascending=True, inplace=True) 
        atr = ta.atr(data['High'], data['Low'], data['Close'], timeperiod=period)        
        atr = atr.dropna()
        atr = atr.rolling(window=period).mean().iloc[-1]
        return atr

    def calculate_finta_atr(self, data, period=20):
        data = data.copy() 
        data.sort_index(ascending=True, inplace=True)  
        atr = TA.ATR(data, period=period)
        atr = atr.dropna()
        atr = atr.rolling(window=period).mean().iloc[-1]
        return atr    
    
    def grid_calc_func(self, resistance, support, atr):
        pivot_substract = abs(resistance - support)
        atr_decimal = atr/my_params.grid_decimal
        grid_number = int(pivot_substract/atr_decimal) + 1
        return grid_number
# //////////////////////////////////////////////////////////////////

class CALC_PIV(CALC_ATR):
    def __init__(self) -> None:
         super().__init__()
    
    def finta_pivot_with_period(self, symbol, data, period=20):
        dataa = data.copy()
        piv_repl = {}
        piv = None
   
        if my_params.PIVOT_GENERAL_TYPE == 'Classic':
            piv = TA.PIVOT(dataa)
        elif my_params.PIVOT_GENERAL_TYPE == 'Fibonacci':
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

        my_params.pivot_levels_type = 4

        piv_repl[symbol] = {
            f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}': latest_pivot_dict[f'S{my_params.pivot_levels_type}'],
            f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}': latest_pivot_dict[f'R{my_params.pivot_levels_type}']
        }

        return piv_repl

class CALC_MANAGER(CALC_PIV):

    def __init__(self) -> None:
        super().__init__()

    def find_the_best_coin(self, symbol, target):
        piv_info_repl = None
        direction = None
        resistance_piv, support_piv = None, None
        if target == 'default_calc':
            top_coins = []
            top_coins = utils_for_orderss.assets_filters()
            symbol = top_coins[0]
        elif target == 'custom_calc':
            # symbol = 'BTCUSDT' 
            pass
        data = get_apii.get_klines(symbol) 
        assets = []
        assets.append(symbol)
        all_coins_indicators = tv_infoo.get_tv_steak_signals(assets)  

        if my_params.inds_source == 'tv':            
            if my_params.ind_strategy == 1:                
                direction = sigmals_handler_one(all_coins_indicators)
                direction = direction[0]['side'] 
                piv_info_repl = tv_infoo.get_piv(symbol)
            elif my_params.ind_strategy == 2:
                all_coins_indicators = tv_infoo.get_tv_steak_signals(assets)
                direction = sigmals_handler_two(all_coins_indicators)
                direction = direction[0]['side']
                piv_info_repl = self.finta_pivot_with_period(symbol, data)
                my_params.pivot_levels_type = 4
            
        elif my_params.inds_source == 'ta':
            all_coins_indicators = get_ta_signals(assets)
            direction = sigmals_handler_two(all_coins_indicators)
            direction = direction[0]['side'] 
            piv_info_repl = self.finta_pivot_with_period(symbol, data)
            my_params.pivot_levels_type = 4

        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}']
        atr2 = self.calculate_talib_atr(data)
        atr3 = self.calculate_pandas_atr(data)
        atr4 = self.calculate_finta_atr(data)
        atr = (atr2 + atr3 + atr4) / 3

        if direction == 'BUY' or 'NEUTRAL':
            tp, sl = resistance_piv + atr*0.03, support_piv - atr*0.015
        elif direction == 'SELL' or 'NEUTRAL':
            sl, tp = resistance_piv + atr*0.015, support_piv - atr*0.03
        
        grid_number = self.grid_calc_func(resistance_piv, support_piv, atr)

        return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

    def find_the_top_coin(self):
        top_coins = []        
        all_coins_indicators = []
        top_coins_updated = []
        top_coins = utils_for_orderss.assets_filters()        
        if my_params.inds_source == 'tv' and my_params.ind_strategy == 1:
            all_coins_indicators = tv_infoo.get_tv_steak_signals(top_coins)
            top_coins_updated = sigmals_handler_one(all_coins_indicators)

        elif my_params.inds_source == 'tv' and my_params.ind_strategy == 2:
            all_coins_indicators = tv_infoo.get_tv_steak_signals(top_coins)
            top_coins_updated = sigmals_handler_two(all_coins_indicators)
            
        elif my_params.inds_source == 'ta':            
            all_coins_indicators = get_ta_signals(top_coins)            
            top_coins_updated = sigmals_handler_two(all_coins_indicators)

        return top_coins_updated
        
calc_controllerr = CALC_MANAGER()

# symbol = 'BTCUSDT'
# data = get_apii.get_klines(symbol)


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