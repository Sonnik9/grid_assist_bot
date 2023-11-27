from CALC.inds_strategy import IND_STRATEGY_
import pandas as pd

class CALC_MANAGER(IND_STRATEGY_):

    def __init__(self) -> None:
        super().__init__()     

    def find_the_best_coin(self, symbol):
        time_frame_list = ['1h', '4h', '1d']
        direction_acum = ''
        price_acum = ''
        answer = {}
        piv_info_repl = ''
        direction = ''
        resistance_piv, support_piv = '', ''
        resistance_piv_acum, support_piv_acum = '', ''
        tp, sl = '', '' 
        tp_acum, sl_acum = '', ''
        grid_number_acum = ''

        for tm in time_frame_list:
            self.INTERVAL = tm           
            df = None         
            df = self.get_klines(symbol, custom_period=1000)                     
            direction = self.sigmals_handler_two(symbol, df)
            direction_acum += direction + ',' + '  '            
            # /////////////////////////////////////////////////////////////        
            atr_data = self.calculate_pandas_steck_atr(df)
            last_atr = atr_data[-1]
            # print(f"atr:  {last_atr}")
            self.pivot_levels_type = self.determine_pivot_type(atr_data, last_atr)
            print(f"pivot_tipe: {self.pivot_levels_type}")
            piv_info_repl = self.calculate_manualy_pivot(symbol, df)
            # piv_info_repl = self.calculate_finta_pivot(symbol, data)        
            resistance_piv, support_piv = piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.R{self.pivot_levels_type}'], piv_info_repl[symbol][f'Pivot.M.{self.PIVOT_GENERAL_TYPE}.S{self.pivot_levels_type}']
            resistance_piv_acum += str(resistance_piv) + ',' + '  '
            support_piv_acum += str(support_piv) + ',' + '  '
            # ////////////////////////////////////////////////////////////  
            slatr = 1.2*last_atr  
            print(last_atr)
            # /////////////////////////////////////////////
            last_close_price = df.Close.iloc[-1] 
            price_acum += str(last_close_price) + ',' + '  ' 
    
            if direction == 'T_BUY' or direction == 'F_BUY':
                tp, sl = last_close_price + slatr*self.TPSLRatio, last_close_price - slatr
            elif direction == 'T_SELL' or direction == 'F_SELL':
                sl, tp = last_close_price + slatr, last_close_price - slatr*self.TPSLRatio
            tp_acum += str(tp) + ',' + '  '
            sl_acum += str(sl) + ',' + '  '

            
            grid_number = self.calculate_grid_number(resistance_piv, support_piv, last_atr)
            grid_number_acum += str(grid_number) + ',' + '  '
        answer['symbol'] = symbol
        answer['direction'] = direction_acum
        answer['last_close_price'] = price_acum
        answer['resistance_piv'] = resistance_piv_acum
        answer['support_piv'] = support_piv_acum
        answer['grid_number'] = grid_number_acum
        answer['tp'] = tp_acum
        answer['sl'] = sl_acum

        return answer

    def find_the_top_coin(self):
        top_coins = []       
        top_coins_updated = []
        
        top_coins = self.assets_filters()  
        time_frame_list = ['1h', '4h', '1d']
        for symbol in top_coins:
            direction_acum = ''
            for tm in time_frame_list:
                self.INTERVAL = tm           
                df = None            
                df = self.get_klines(symbol, custom_period=1000)                     
                direction_acum += self.sigmals_handler_two(symbol, df) + ',' + '  '
            top_coins_updated.append({'symbol': symbol, 'side': direction_acum})

        return top_coins_updated

# python -m CALC.calc_controller