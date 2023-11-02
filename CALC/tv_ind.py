from tradingview_ta import *
from pparamss import my_params
from tradingview_ta import TA_Handler

class TV_INFO():

    def __init__(self)-> None:
        pass

    def get_tv_steak_signals(self, top_coins):

        all_coins_indicators = None        
        symbols = [f"BINANCE:{x}" for x in top_coins if x]

        all_coins_indicators = get_multiple_analysis(symbols=symbols,
                            screener='crypto',                    
                            interval=my_params.INTERVAL)
        
        return all_coins_indicators
    
    def get_tv_info(self, character, top_coins):

        repl_dict = {}
            
        for symbol in top_coins:
            if not symbol:
                continue
            
            handler = TA_Handler(
                symbol=symbol,
                exchange='BINANCE',
                screener='crypto',
                interval=my_params.INTERVAL  
            )

            analysis = handler.get_analysis()
            if character == 'REC':
                repl_dict.append(analysis.summary['RECOMMENDATION'])
            elif character == 'INDS':            
                repl_dict[symbol] = {                    
                    'BB.lower': analysis.indicators['BB.lower'],
                    'BB.upper': analysis.indicators['BB.upper'],
                    'Pivot.M.Classic.S1': analysis.indicators['Pivot.M.Classic.S1'],
                    'Pivot.M.Classic.R1': analysis.indicators['Pivot.M.Classic.R1'],
                    'Pivot.M.Fibonacci.S1': analysis.indicators['Pivot.M.Fibonacci.S1'],
                    'Pivot.M.Fibonacci.R1': analysis.indicators['Pivot.M.Fibonacci.R1']
                }
                

        return repl_dict
    
tv_infoo = TV_INFO()

# python -m CALC.tv_ind