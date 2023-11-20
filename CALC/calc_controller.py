from CALC.inds_strategy import IND_STRATEGY_
import pandas as pd

class CALC_MANAGER(IND_STRATEGY_):

    def __init__(self) -> None:
        super().__init__()     

    def find_the_best_coin(self, symbol):
        data = None
        piv_info_repl = None
        direction = None
        resistance_piv, support_piv = None, None
        tp, sl = None, None        
        custom_period = None
        assets = []         
        assets.append(symbol)

        
        direction = self.sigmals_handler_two(assets)        
        direction = direction[0]['side']
        print(direction)
        # ///////////////////////////////////////////////////////////// 
        spec_kline_data = self.get_klines(symbol, custom_period=1000)
        atr_data = self.calculate_pandas_atr_for_pivot_type(spec_kline_data)
        last_atr = atr_data[-1]
        print(f"atr:  {last_atr}")
        self.pivot_levels_type = self.determine_pivot_type(atr_data, last_atr)
        print(f"pivot_tipe: {self.pivot_levels_type}")
        try:
            data = self.get_klines(symbol, custom_period)  
            # print(f"klines_data: {data}")
        except Exception as ex:
            print(f"25control: {ex}")
            return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl        
        
        piv_info_repl = self.calculate_manualy_pivot(symbol, data)
        # piv_info_repl = self.calculate_finta_pivot(symbol, data)        
        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}']
        # ////////////////////////////////////////////////////////////
        atr1 = self.calculate_pandas_atr(data)
        atr2 = self.calculate_talib_atr(data)
        atr = (atr1+atr2) / 2
        print(f"atr: {atr}")
        # ////////////////////////////////////////////////////////////
        if direction == 'T_BUY' or direction == 'F_BUY':
            tp, sl = resistance_piv + atr*0.03, support_piv - atr*0.015
        elif direction == 'T_SELL' or direction == 'F_SELL':
            sl, tp = resistance_piv + atr*0.015, support_piv - atr*0.03
        
        grid_number = self.calculate_grid_number(resistance_piv, support_piv, atr)

        return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

    def find_the_top_coin(self):
        top_coins = []       
        top_coins_updated = []
        top_coins = self.assets_filters()                       
        top_coins_updated = self.sigmals_handler_two(top_coins)

        return top_coins_updated

# python -m CALC.calc_controller