from pparamss import my_params

def grid_calc_func(resistance, support, atr):
    pivot_substract = abs(resistance - support)
    atr_decimal = atr/my_params.grid_decimal
    grid_number = int(pivot_substract/atr_decimal) + 1
    return grid_number


