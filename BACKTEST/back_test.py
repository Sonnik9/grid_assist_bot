from CALC.calc_controller import CALC_MANAGER
import pandas as pd

class BACKTESTT(CALC_MANAGER):
    def __init__(self) -> None:
        super().__init__()

    def backtest_main(self, symbol, last_data='2023-10-31'):

        bt_repl = {}
        calc_data = {}
        bt_repl["strategy_result"] = 'Undefended'
        bt_repl["position"] = 'open'
        calc_data["symbol"] = symbol
        custom_period = 1499
        self.INTERVAL = '1h'
        try:
            direction, resistance_piv, support_piv, grid_number, tp, sl = None, None, None, None, None, None
            data = self.get_klines(symbol, custom_period)
            data.index = pd.to_datetime(data.index)
            last_data = pd.to_datetime(last_data)
            kline_data_before = data[data.index <= last_data]
            kline_data_after = data[data.index > last_data]
            close_price = float(kline_data_before['Close'].iloc[-1])
              
            
            self.bt_data = kline_data_before  
            # print(self.bt_data)        
            _, direction, resistance_piv, support_piv, grid_number, tp, sl = self.find_the_best_coin(symbol, self.bt_data)
            calc_data["direction"] = direction  
            calc_data["resistance_piv"] = resistance_piv   
            calc_data["support_piv"] = support_piv 
            calc_data["grid_number"] = grid_number  
            calc_data["tp"] = tp  
            calc_data["sl"] = sl     
           
            max_high = kline_data_after['High'].max()
            min_low = kline_data_after['Low'].min()            
            max_high_flag = kline_data_after['High'].idxmax() < kline_data_after['Low'].idxmin()
            min_low_flag = not max_high_flag

            if direction == 'BUY':
                if max_high_flag:
                    if tp <= max_high:
                        bt_repl["strategy_result"] = 'Win'
                        bt_repl["position"] = 'close'
                        return bt_repl
                    elif sl >= min_low:
                        bt_repl["strategy_result"] = 'Lose'
                        bt_repl["position"] = 'close'
                        return bt_repl
                if min_low_flag:
                    if sl >= min_low:
                        bt_repl["strategy_result"] = 'Lose'
                        bt_repl["position"] = 'close'
                        return bt_repl
                    elif tp <= max_high:
                        bt_repl["strategy_result"] = 'Win'
                        bt_repl["position"] = 'close'
                        return bt_repl
            elif direction == 'SELL':
                if max_high_flag:
                    if tp >= max_high:
                        bt_repl["strategy_result"] = 'Win'
                        bt_repl["position"] = 'close'
                        return bt_repl
                    elif sl <= min_low:
                        bt_repl["strategy_result"] = 'Lose'
                        bt_repl["position"] = 'close'
                        return bt_repl
                if min_low_flag:
                    if sl <= min_low:
                        bt_repl["strategy_result"] = 'Lose'
                        bt_repl["position"] = 'close'
                        return bt_repl
                    elif tp >= max_high:
                        bt_repl["strategy_result"] = 'Win'
                        bt_repl["position"] = 'close'
                        return bt_repl
        except KeyError as key_error:
            print(f"KeyError: {key_error}")
        except Exception as ex:
            print(f"Exception: {ex}")

        return grid_number, bt_repl





        



bt = BACKTESTT()
symbol = 'LINKUSDT'
repl = None
repl = bt.backtest_main(symbol)
print(repl)

# python -m BACKTEST.back_test

        