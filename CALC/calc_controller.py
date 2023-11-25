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
        mono_flag = True    
        assets = []         
        assets.append(symbol)  
        data = self.get_klines(symbol, custom_period=1000)      
        direction = self.sigmals_handler_two(assets, data, mono_flag)        
        direction = direction[0]['side']
        print(direction)
        # /////////////////////////////////////////////////////////////        
        atr_data = self.calculate_pandas_steck_atr(data)
        last_atr = atr_data[-1]
        # print(f"atr:  {last_atr}")
        self.pivot_levels_type = self.determine_pivot_type(atr_data, last_atr)
        print(f"pivot_tipe: {self.pivot_levels_type}")
        piv_info_repl = self.calculate_manualy_pivot(symbol, data)
        # piv_info_repl = self.calculate_finta_pivot(symbol, data)        
        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}']
        # ////////////////////////////////////////////////////////////        
        if direction == 'T_BUY' or direction == 'F_BUY':
            tp, sl = resistance_piv + last_atr*0.03, support_piv - last_atr*0.015
        elif direction == 'T_SELL' or direction == 'F_SELL':
            sl, tp = resistance_piv + last_atr*0.015, support_piv - last_atr*0.03
        
        grid_number = self.calculate_grid_number(resistance_piv, support_piv, last_atr)

        return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

    def find_the_top_coin(self):
        top_coins = []       
        top_coins_updated = []
        data = None 
        mono_flag = False
        top_coins = self.assets_filters()                       
        top_coins_updated = self.sigmals_handler_two(top_coins, data, mono_flag)

        return top_coins_updated

# python -m CALC.calc_controller