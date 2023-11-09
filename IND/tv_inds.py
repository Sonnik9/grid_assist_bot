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
    
    def extract_tv_signals(self, all_coins_indicators):
        close_price, adx, sma, upper, lower, macd, signal, rsi, fastk, slowk = None, None, None, None, None, None, None, None, None, None

        data_previous_stek = []
        for _, item in all_coins_indicators.items():
            try: 
                symboll = item.symbol  
                close_price = item.indicators['close']        
                adx = item.indicators["ADX"] 
                sma = item.indicators["SMA20"] 
                upper, lower = item.indicators["BB.upper"], item.indicators["BB.lower"] 
                macd, signal = item.indicators["MACD.macd"], item.indicators["MACD.signal"]     
                rsi = item.indicators["RSI"]
                fastk, slowk = item.indicators["Stoch.K"], item.indicators["Stoch.D"]
                
                data_previous_stek.append((symboll, close_price, adx, sma, upper, lower, macd, signal, rsi, fastk, slowk))
            except Exception as ex:
                pass

        return data_previous_stek
    
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
        # print(coin_indicators)
        piv[the_best_coin] = {
            f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}': coin_indicators.indicators[f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}'],
            f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}': coin_indicators.indicators[f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}']      
        }

        return piv
    
tv_infoo = TV_INFO()

# python -m IND.tv_inds