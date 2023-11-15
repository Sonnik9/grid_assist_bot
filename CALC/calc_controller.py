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
        except:
            return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl
        
        direction = self.sigmals_handler_two(assets)        
        direction = direction[0]['side'] 
        piv_info_repl = self.calculate_pivot(symbol, data)
        self.pivot_levels_type = 4
        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}']
        atr = self.calculate_atr(data)

        if direction == 'BUY' or 'F_BUY':
            tp, sl = resistance_piv + atr*0.03, support_piv - atr*0.015
        elif direction == 'SELL' or 'F_SELL':
            sl, tp = resistance_piv + atr*0.015, support_piv - atr*0.03
        
        grid_number = self.calculate_grid_number(resistance_piv, support_piv, atr)

        return symbol, direction, resistance_piv, support_piv, grid_number, tp, sl

    def find_the_top_coin(self):
        top_coins = []       
        top_coins_updated = []
        top_coins = self.assets_filters()                       
        top_coins_updated = self.sigmals_handler_two(top_coins)

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