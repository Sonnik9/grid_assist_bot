from pparamss import my_params
from API_BINANCE.get_api import get_apii
from API_BINANCE.utils_api import utils_for_orderss
from CALC.atr_calc import calculate_atr
from CALC.piv_calc import piv_controller
from CALC.grid_number_calc import grid_calc_func
from IND.ind_1_strategy import sigmals_handler_one 
from IND.ind_2_strategy import sigmals_handler_two
from IND.ta_inds import *
from IND.tv_inds import tv_infoo

class UTILS_CALC():

    def __init__(self) -> None:
        pass

    def find_the_best_coin(self, symbol, target='custom_calc'):
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
                piv_info_repl = piv_controller(symbol, data)
            
        elif my_params.inds_source == 'ta':
            all_coins_indicators = self.get_ta_signals(assets)
            direction = sigmals_handler_two(all_coins_indicators)
            direction = direction[0]['side'] 
            piv_info_repl = piv_controller(symbol, data)

        resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}']
        atr = calculate_atr(data)
        # print(atr)

        if direction == 'BUY' or 'NEUTRAL':
            tp, sl = resistance_piv + atr*0.03, support_piv - atr*0.015
        elif direction == 'SELL' or 'NEUTRAL':
            sl, tp = resistance_piv + atr*0.015, support_piv - atr*0.03
        
        grid_number = grid_calc_func(resistance_piv, support_piv, atr)

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
            # print(top_coins)
            all_coins_indicators = self.get_ta_signals(top_coins)
            # print(all_coins_indicators)
            top_coins_updated = sigmals_handler_two(all_coins_indicators)

        return top_coins_updated
    
    def get_ta_signals(self, top_coins):
        klines_data = []
        for symbol in top_coins:
            # print(symbol)
            try:
                kline_data = get_apii.get_klines(symbol)
                # print(kline_data)
                close_price = kline_data['Close'].iloc[-1]
                adx = calculate_adx(kline_data)
                sma26 = calculate_sma(kline_data)
                upper, lower = calculate_bollinger_bands(kline_data)                 
                macd, signal = calculate_macd(kline_data)
                rsi = calculate_rsi(kline_data)
                fastk, slowk = calculate_stochastic_oscillator(kline_data)   
                klines_data.append({
                    'symbol': symbol,
                    'close_price': close_price,
                    'ADX': adx, 
                    'SMA20': sma26, 
                    "BB.upper": upper,
                    "BB.lower": lower,
                    "MACD.macd": macd,
                    "MACD.signal": signal,
                    "RSI": rsi,
                    "Stoch.K": fastk,
                    "Stoch.D": slowk,
                    })
            except Exception as ex:
                # print(ex) 
                pass
   
        return klines_data
    
calc_controller = UTILS_CALC()
# top_coins = None
# symbol = "BTCUSDT"
# top_coins = calc_controller.find_the_top_coin()
# print(top_coins)

# python -m CALC.calc_controller