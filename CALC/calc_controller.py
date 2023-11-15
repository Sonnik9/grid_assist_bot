from CALC.inds_strategy import IND_STRATEGY_

class CALC_MANAGER(IND_STRATEGY_):

    def __init__(self) -> None:
        super().__init__()     

    def find_the_best_coin(self, symbol, target):
        piv_info_repl = None
        direction = None
        resistance_piv, support_piv = None, None
        tp, sl = None, None
        assets = []
        if target == 'default_calc':
            top_coins = []
            top_coins = self.assets_filters()
            symbol = top_coins[0]        
        assets.append(symbol)    
        try: 
            data = self.get_klines(symbol)  
            print(data)
        except:
            return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl
        
        direction = self.sigmals_handler_two(assets)        
        direction = direction[0]['side'] 
        piv_info_repl = self.calculate_pivot(symbol, data)        
        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}']
        atr2 = self.calculate_pandas_atr(data)
        atr3 = self.calculate_talib_atr(data)
        atr = (atr2+atr3) / 2

        if direction == 'BUY':
            tp, sl = resistance_piv + atr*0.03, support_piv - atr*0.1
        elif direction == 'SELL':
            sl, tp = resistance_piv + atr*0.1, support_piv - atr*0.03
        
        grid_number = self.calculate_grid_number(resistance_piv, support_piv, atr)

        return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

    def find_the_top_coin(self):
        top_coins = []       
        top_coins_updated = []
        top_coins = self.assets_filters()                       
        top_coins_updated = self.sigmals_handler_two(top_coins)

        return top_coins_updated

# python -m CALC.calc_controller