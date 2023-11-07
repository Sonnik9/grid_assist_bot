from pparamss import my_params
from API_BINANCE.get_api import get_apii
from API_BINANCE.utils_api import utils_for_orderss
from IND.ind_1_strategy import sigmals_handler_one 
from IND.ind_2_strategy import sigmals_handler_two, get_ta_signals
from IND.ta_inds import ta_iindss
from IND.tv_inds import tv_infoo
import pandas_ta as ta
from finta import TA
import pandas as pd

class CALC_UTILS():
    def __init__(self) -> None:
         pass
    
    def calculate_atr(self, data, period=14):

        true_ranges = []

        for i in range(1, len(data)):
            high = data['High'].iloc[i]
            low = data['Low'].iloc[i]
            close = data['Close'].iloc[i]
            true_range = max(abs(high - low), abs(high - close), abs(low - close))        
            true_ranges.append(true_range)
        atr = sum(true_ranges[-period:]) / period

        return atr

    def finta_pivot(self, data):
        dataa = data.copy()
        piv_repl = {}
        piv = None
        piv = TA.PIVOT(dataa)

        latest_pivot = piv.iloc[-1]

        # Оформить их в словарь
        latest_pivot_dict = {
            'pp': latest_pivot['pivot'],
            'S1': latest_pivot['s1'],
            'S2': latest_pivot['s2'],
            'S3': latest_pivot['s3'],
            'S4': latest_pivot['s4'],
            'R1': latest_pivot['r1'],
            'R2': latest_pivot['r2'],
            'R3': latest_pivot['r3'],
            'R4': latest_pivot['r4']
        }
        my_params.pivot_levels_type = 3
        piv_repl[symbol] = {
            f'Pivot.M.Classic.S{my_params.pivot_levels_type}': latest_pivot_dict[f'S{my_params.pivot_levels_type}'],
            f'Pivot.M.Classic.R{my_params.pivot_levels_type}': latest_pivot_dict[f'R{my_params.pivot_levels_type}']
        }
        return piv_repl

    
    def grid_calc_func(self, resistance, support, atr):
        pivot_substract = abs(resistance - support)
        atr_decimal = atr/my_params.grid_decimal
        grid_number = int(pivot_substract/atr_decimal) + 1
        return grid_number
    
    def calculate_fibonacci_pivot_points(self, symbol, data):
        piv = {}
        try:
            high = data['High']
            low = data['Low']
            close = data['Close']
            
            # Рассчитываем уровни Pivot Points Фибоначчи
            pivot = (high + low + close) / 3
            support1 = pivot - 0.382 * (high - low)
            support2 = pivot - 0.618 * (high - low)
            support3 = pivot - (high - low)
            resistance1 = pivot + 0.382 * (high - low)
            resistance2 = pivot + 0.618 * (high - low)
            resistance3 = pivot + (high - low)

            piv = {
                'pp': pivot.iloc[-1],
                'S1': support1.iloc[-1],
                'S2': support2.iloc[-1],
                'S3': support3.iloc[-1],
                'R1': resistance1.iloc[-1],
                'R2': resistance2.iloc[-1],
                'R3': resistance3.iloc[-1]
            }
            piv[symbol] = {
                f'Pivot.M.Fibonacci.S{my_params.pivot_levels_type}': piv[f'S{my_params.pivot_levels_type}'],
                f'Pivot.M.Fibonacci.R{my_params.pivot_levels_type}': piv[f'R{my_params.pivot_levels_type}']
            }
        except Exception as ex:
            print(ex)

        return piv

    def calculate_classsic_pivot_points(self, symbol, data):
        piv = {}
        piv_repl = {} 
        try:
            high = data['High']
            # print(high
            # )
            low = data['Low']
            # print(low)
            close = data['Close']
            # print(close)

            pivot = (high + low + close) / 3
            support1 = (2 * pivot) - high
            support2 = pivot - (high - low)
            support3 = pivot - 2 * (high - low)
            resistance1 = (2 * pivot) - low
            resistance2 = pivot + (high - low)
            resistance3 = pivot + 2 * (high - low)
            
            piv = {
                'pp': pivot.iloc[-1],
                'S1': support1.iloc[-1],
                'S2': support2.iloc[-1],
                'S3': support3.iloc[-1],
                'R1': resistance1.iloc[-1],
                'R2': resistance2.iloc[-1],
                'R3': resistance3.iloc[-1]
            }
            piv_repl[symbol] = {
                f'Pivot.M.Classic.S{my_params.pivot_levels_type}': piv[f'S{my_params.pivot_levels_type}'],
                f'Pivot.M.Classic.R{my_params.pivot_levels_type}': piv[f'R{my_params.pivot_levels_type}']
            }
        except Exception as ex:
            print(f"str31: {ex}")

        return piv_repl

    def piv_controller(self, symbol, data):
        piv = None
        if my_params.PIVOT_GENERAL_TYPE == 'Classic':
            piv = self.calculate_classsic_pivot_points(symbol, data)
        elif my_params.PIVOT_GENERAL_TYPE == 'Fibonacci':
            piv = self.calculate_fibonacci_pivot_points(symbol, data)

        return piv


class CALC_MANAGER(CALC_UTILS):

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
                piv_info_repl = self.piv_controller(symbol, data)
            
        elif my_params.inds_source == 'ta':
            all_coins_indicators = get_ta_signals(assets)
            direction = sigmals_handler_two(all_coins_indicators)
            direction = direction[0]['side'] 
            piv_info_repl = self.piv_controller(symbol, data)

        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}']
        atr = self.calculate_atr(data)
        # print(atr)

        if direction == 'BUY' or 'NEUTRAL':
            tp, sl = resistance_piv + atr*0.03, support_piv - atr*0.015
        elif direction == 'SELL' or 'NEUTRAL':
            sl, tp = resistance_piv + atr*0.015, support_piv - atr*0.03
        
        grid_number = self.grid_calc_func(resistance_piv, support_piv, atr)

        return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

    def find_the_top_coin(self):
        top_coins = []
        # klines_data = []
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

symbol = 'BTCUSDT'
data = get_apii.get_klines(symbol)
# atr = calc_controllerr.calculate_atr(data)
# print(atr)

# tv_piv = tv_infoo.get_piv(symbol)
# print(tv_piv)
manual_piv = calc_controllerr.piv_controller(symbol, data)
finta_piv = calc_controllerr.pandas_pivot(data)
print(manual_piv)
print(finta_piv)


# top_coins = None
# symbol = "BTCUSDT"
# target = 'default_calc'
# top_coins = calc_controllerr.find_the_best_coin(symbol, target)
# print(top_coins)

# python -m CALC.calc_controller