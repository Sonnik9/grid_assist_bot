from TG.tg_main import main_tg_func
from API_BINANCE.get_api import get_apii
from CALC.atr_calc import calculate_atr
from CALC.pivot_lev import calc_pivot_lev_func
from CALC.grid_number_calc import grid_calc_func
from CALC.tv_ind import tv_infoo

def main():
    tv_info_repl = None
    uppor_piv, resistance_piv = None, None
    symbol = 'BTCUSDT'
    data = get_apii.get_klines(symbol)    
    character = 'INDS'
    top_coins = []
    top_coins.append(symbol)
    tv_info_repl = tv_infoo.get_tv_info(character, top_coins)
    uppor_piv, resistance_piv = tv_info_repl[symbol]['Pivot.M.Classic.R1'], tv_info_repl[symbol]['Pivot.M.Classic.S1']
    atr = calculate_atr(data)
    grid_number = grid_calc_func(uppor_piv, resistance_piv, atr)
    print(grid_number)

    # main_tg_func() 

if __name__=="__main__":
    main()