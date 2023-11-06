from pparamss import my_params

def calculate_fibonacci_pivot_points(symbol, data):
    piv = {}
    try:
        high = data['High']
        low = data['Low']
        close = data['Close']
        
        # Рассчитываем уровни Pivot Points Фибоначчи
        pivot = (high + low + close) / 3
        support1 = pivot - 0.382 * (high - low)
        support2 = pivot - 0.618 * (high - low)
        support3 = pivot - (high - low)
        resistance1 = pivot + 0.382 * (high - low)
        resistance2 = pivot + 0.618 * (high - low)
        resistance3 = pivot + (high - low)

        piv = {
            'pp': pivot.iloc[-1],
            'S1': support1.iloc[-1],
            'S2': support2.iloc[-1],
            'S3': support3.iloc[-1],
            'R1': resistance1.iloc[-1],
            'R2': resistance2.iloc[-1],
            'R3': resistance3.iloc[-1]
        }
        piv[symbol] = {
            f'Pivot.M.Fibonacci.S{my_params.pivot_levels_type}': piv[f'S{my_params.pivot_levels_type}'],
            f'Pivot.M.Fibonacci.R{my_params.pivot_levels_type}': piv[f'R{my_params.pivot_levels_type}']
        }
    except Exception as ex:
        print(ex)

    return piv

def calculate_classsic_pivot_points(symbol, data):
    piv = {}
    try:
        high = data['High']
        # print(high)
        low = data['Low']
        # print(low)
        close = data['Close']
        # print(close)

        pivot = (high + low + close) / 3
        support1 = (2 * pivot) - high
        support2 = pivot - (high - low)
        support3 = pivot - 2 * (high - low)
        resistance1 = (2 * pivot) - low
        resistance2 = pivot + (high - low)
        resistance3 = pivot + 2 * (high - low)
        
        piv = {
            'pp': pivot.iloc[-1],
            'S1': support1.iloc[-1],
            'S2': support2.iloc[-1],
            'S3': support3.iloc[-1],
            'R1': resistance1.iloc[-1],
            'R2': resistance2.iloc[-1],
            'R3': resistance3.iloc[-1]
        }
        piv[symbol] = {
            f'Pivot.M.Classic.S{my_params.pivot_levels_type}': piv[f'S{my_params.pivot_levels_type}'],
            f'Pivot.M.Classic.R{my_params.pivot_levels_type}': piv[f'R{my_params.pivot_levels_type}']
        }
    except Exception as ex:
        print(f"str31: {ex}")

    return piv

def piv_controller(symbol, data):
    piv = None
    if my_params.PIVOT_GENERAL_TYPE == 'Classic':
        piv = calculate_classsic_pivot_points(symbol, data)
    elif my_params.PIVOT_GENERAL_TYPE == 'Fibonacci':
        piv = calculate_fibonacci_pivot_points(symbol, data)

    return piv

# data = get_apii.get_klines(symbol='BTCUSDT')
# piv = None
# piv = piv_controller(data)
# print(piv)