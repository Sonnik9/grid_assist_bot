from tradingview_ta import *
from pparamss import my_params
from tradingview_ta import TA_Handler

class TV_INFO():

    def __init__(self)-> None:
        pass

    def get_tv_steak_signals(self, top_coins_list):

        all_coins_indicators = None        
        symbols = [f"BINANCE:{x}" for x in top_coins_list if x]

        all_coins_indicators = get_multiple_analysis(symbols=symbols,
                            screener='crypto',                    
                            interval=my_params.INTERVAL)
        
        return all_coins_indicators
    
    def get_piv(self, the_best_coin):

        coin_indicators = {}
        piv = {}

        handler = TA_Handler(
            symbol=the_best_coin,
            exchange='BINANCE',
            screener='crypto',
            interval=my_params.INTERVAL  
        )

        coin_indicators = handler.get_analysis()
        piv[the_best_coin] = {
            f'Pivot.M.Classic.S{my_params.pivot_levels_type}': coin_indicators.indicators[f'Pivot.M.Classic.S{my_params.pivot_levels_type}'],
            f'Pivot.M.Classic.R{my_params.pivot_levels_type}': coin_indicators.indicators[f'Pivot.M.Classic.R{my_params.pivot_levels_type}'],
            f'Pivot.M.Fibonacci.S{my_params.pivot_levels_type}': coin_indicators.indicators[f'Pivot.M.Fibonacci.S{my_params.pivot_levels_type}'],
            f'Pivot.M.Fibonacci.R{my_params.pivot_levels_type}': coin_indicators.indicators[f'Pivot.M.Fibonacci.R{my_params.pivot_levels_type}']

        }

        return piv
    
tv_infoo = TV_INFO()
# top_coins_list = 'BTCUSDT'
# coin_indicators = tv_infoo.get_tv_symbol_signals(top_coins_list)
# print(coin_indicators.indicators['BB.lower'])


                # repl_dict[symbol] = {                    
                #     'BB.lower': analysis.indicators['BB.lower'],
                #     'BB.upper': analysis.indicators['BB.upper'],
                #     f'Pivot.M.Classic.S{my_params.pivot_levels_type}': analysis.indicators[f'Pivot.M.Classic.S{my_params.pivot_levels_type}'],
                #     f'Pivot.M.Classic.R{my_params.pivot_levels_type}': analysis.indicators[f'Pivot.M.Classic.R{my_params.pivot_levels_type}'],
                #     f'Pivot.M.Fibonacci.S{my_params.pivot_levels_type}': analysis.indicators[f'Pivot.M.Fibonacci.S{my_params.pivot_levels_type}'],
                #     f'Pivot.M.Fibonacci.R{my_params.pivot_levels_type}': analysis.indicators[f'Pivot.M.Fibonacci.R{my_params.pivot_levels_type}']
                # }

# python -m IND.tv_inds