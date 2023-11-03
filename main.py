from pparamss import my_params
from TG.tg_main import main_tg_func
from API_BINANCE.get_api import get_apii
from API_BINANCE.utils_api import utils_for_orderss
from CALC.atr_calc import calculate_atr
from CALC.grid_number_calc import grid_calc_func
from CALC.tv_ind import tv_infoo
# from config import Configg

def main():
    top_coins = []
    top_coins = utils_for_orderss.assets_filters()
    tv_info_repl = None
    upper_piv, resistance_piv = None, None
    symbol = top_coins[0]
    data = get_apii.get_klines(symbol) 
    print(symbol)   
    character = 'INDS'
    assets = []
    assets.append(symbol)
    tv_info_repl = tv_infoo.get_tv_info(character, assets)
    upper_piv, resistance_piv = tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}'], tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}']
    atr = calculate_atr(data)
    print(upper_piv, resistance_piv)
    grid_number = grid_calc_func(upper_piv, resistance_piv, atr)
    print(grid_number)

    # main_tg_func() 

if __name__=="__main__":
    main()