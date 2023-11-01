from TG.tg_main import main_tg_func
from API_BINANCE.get_api import get_apii
from CALC.atr_calc import calculate_atr
from CALC.pivot_lev import calc_pivot_lev_func
from CALC.grid_number_calc import grid_calc_func

def main():
    symbol = 'BTCUSDT'
    data = get_apii.get_klines(symbol)
    support_ma, resistance_ma = calc_pivot_lev_func(data)
    atr = calculate_atr(data)
    grid_number = grid_calc_func(support_ma, resistance_ma, atr)
    print(grid_number)

    # main_tg_func() 

if __name__=="__main__":
    main()