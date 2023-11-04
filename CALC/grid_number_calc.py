from pparamss import my_params

def grid_calc_func(resistance, support, atr):
    pivot_substract = abs(resistance - support)
    # print(pivot_substract)
    # print(atr)
    atr_decimal = atr/my_params.grid_decimal
    # print(atr_decimal)
    grid_number = int(pivot_substract/atr_decimal) + 1
    return grid_number


