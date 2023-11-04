from API_BINANCE.get_api import get_apii
from API_BINANCE.utils_api import utils_for_orderss
from CALC.atr_calc import calculate_atr
from CALC.grid_number_calc import grid_calc_func
from CALC.tv_ind import tv_infoo
from CALC.custom_ind import sigmals_handler_two

from pparamss import my_params

def find_the_best_coin():
    top_coins = []
    top_coins = utils_for_orderss.assets_filters()
    tv_info_repl = None
    direction = None
    resistance_piv, support_piv = None, None
    symbol = top_coins[0]
    data = get_apii.get_klines(symbol) 
    # print(symbol)   
    character = 'INDS'
    assets = []
    assets.append(symbol)
    all_coins_indicators = tv_infoo.get_tv_steak_signals(assets)
    direction = sigmals_handler_two(all_coins_indicators)
    direction = direction[0]['side']    
    tv_info_repl = tv_infoo.get_tv_info(character, assets)
    resistance_piv, support_piv = tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}'], tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}']
    atr = calculate_atr(data)

    if direction == 'BUY' or 'NEUTRAL':
        tp, sl = resistance_piv + atr*0.1, support_piv + atr*0.05
    elif direction == 'SELL' or 'NEUTRAL':
        sl, tp = resistance_piv + atr*0.1, support_piv + atr*0.05
    
    grid_number = grid_calc_func(resistance_piv, support_piv, atr)
    return symbol, direction, resistance_piv, support_piv, grid_number, sl, tp

def find_the_top_coin():
    top_coins = []
    all_coins_indicators = []
    top_coins_updated = []
    top_coins = utils_for_orderss.assets_filters()
    all_coins_indicators = tv_infoo.get_tv_steak_signals(top_coins)
    top_coins_updated = sigmals_handler_two(all_coins_indicators)

    return top_coins_updated

def find_the_coin_by_custom_way(symbol):
    tv_info_repl = None
    direction = None
    resistance_piv, support_piv = None, None
    data = get_apii.get_klines(symbol) 
    # print(symbol)   
    character = 'INDS'
    assets = []
    assets.append(symbol)
    all_coins_indicators = tv_infoo.get_tv_steak_signals(assets)
    direction = sigmals_handler_two(all_coins_indicators)
    direction = direction[0]['side']    
    tv_info_repl = tv_infoo.get_tv_info(character, assets)
    resistance_piv, support_piv = tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}'], tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}']
    atr = calculate_atr(data)
    
    if direction == 'BUY' or 'NEUTRAL':
        tp, sl = resistance_piv + atr*0.1, support_piv - atr*0.05
    elif direction == 'SELL' or 'NEUTRAL':
        sl, tp = resistance_piv + atr*0.05, support_piv - atr*0.1
    
    grid_number = grid_calc_func(resistance_piv, support_piv, atr)
    return symbol, direction, resistance_piv, support_piv, grid_number, sl, tp

