from CALC.indicators import OTHERS_CALC, TALIB_INDSS

class IND_STRATEGY_(OTHERS_CALC, TALIB_INDSS):
    def __init__(self) -> None:
        super().__init__()

    def bunch_handler_func(self, close_price, current_bunch, kline_data, FT_flag):
        signals_sum = []
        buy_signals_counter = 0
        sell_signals_counter = 0
        total_signal = None        

        try:
            if 'bband_flag' in current_bunch:
                # print('ekrjbgv')
                upper, lower = self.calculate_bollinger_bands(kline_data)
                buy_bband_signal = close_price >= lower * self.b_bband_q
                sell_bband_signal = close_price <= upper * self.s_bband_q
                signals_sum.append((buy_bband_signal, sell_bband_signal))

            if 'macd_lite_flag' in current_bunch:
                # print('mkrjbgv')
                macd, signal = self.calculate_macd(kline_data)
                buy_lite_macd_signal = macd > signal * self.b_macd_q
                sell_lite_macd_signal = macd < signal * self.s_macd_q
                signals_sum.append((buy_lite_macd_signal, sell_lite_macd_signal))

            if 'ma_crossover_lite_flag' in current_bunch:
                # print('maccrjbgv')
                _, ma_20, _, ma_50, _ = self.calculate_ma_s(kline_data)
                buy_ma_crossover_signal = (ma_20 > ma_50) and (close_price > ma_20 and close_price > ma_50)
                sell_ma_crossover_signal = (ma_20 < ma_50) and (close_price < ma_20 and close_price < ma_50)
                signals_sum.append((buy_ma_crossover_signal, sell_ma_crossover_signal)) 

            if 'ma_crossover_strong_flag' in current_bunch:
                # print('kfjgnekrjbgv')
                ma_7, _, ma_25, _, ma_99 = self.calculate_ma_s(kline_data)
                buy_ma_crossover_signal = (ma_7 > ma_25 and ma_25 > ma_99) and (close_price > ma_7 and close_price > ma_25 and close_price > ma_99)
                sell_ma_crossover_signal = (ma_7 < ma_25 and ma_25 < ma_99) and (close_price < ma_7 and close_price < ma_25 and close_price < ma_99)
                signals_sum.append((buy_ma_crossover_signal, sell_ma_crossover_signal))                

            if 'rsi_diver_pattern_flag' in current_bunch:
                # print(signals_sum)
                buy_rsi_diver_signal, sell_rsi_diver_signal = False, False 
                data_rsi = self.calculate_rsi(kline_data)
                data_rsi = data_rsi.iloc[-4:].to_list()
                data_close_price = kline_data['Close'].iloc[-4:].to_list()
                detect_rsi = self.detect_rsi_divergence(data_close_price, data_rsi)
                buy_rsi_diver_signal = detect_rsi == 1
                sell_rsi_diver_signal = detect_rsi == -1
                signals_sum.append((buy_rsi_diver_signal, sell_rsi_diver_signal))
                # print(signals_sum)

            if 'rsi_overtrading_flag' in current_bunch:
                data_rsi = self.calculate_rsi(kline_data)
                rsi = data_rsi.iloc[-1]
                buy_rsi_signal = rsi <= self.b_rsi_lev
                sell_rsi_signal = rsi >= self.s_rsi_lev
                signals_sum.append((buy_rsi_signal, sell_rsi_signal))

            if 'heikin_ashi_strategy_flag' in current_bunch:
                ema_10, ema_30 = self.calculate_ema_s(kline_data)
                heiken_close, heiken_open, heiken_signal = self.calculate_heikin_ashi(kline_data)
                buy_heikin_ashi_signal = (ema_10 > ema_30) and (heiken_open < ema_10) and (heiken_close > ema_10) and (heiken_signal == 1)
                sell_heikin_ashi_signal = (ema_10 < ema_30) and (heiken_open > ema_10) and (heiken_close < ema_10) and (heiken_signal == -1)
                signals_sum.append((buy_heikin_ashi_signal, sell_heikin_ashi_signal))
           
            for buy_signal, sell_signal in signals_sum:
                if buy_signal:
                    buy_signals_counter += 1
                if sell_signal:
                    sell_signals_counter += 1

            total_signal = f'{FT_flag}_BUY' if buy_signals_counter == len(signals_sum) else \
                           f'{FT_flag}_SELL' if sell_signals_counter == len(signals_sum) else \
                           f'{FT_flag}_NEUTRAL'

        except Exception as ex:
            print(ex)
        
        return total_signal

    def trends_defender(self, adx, doji):
        try:
            if adx > 25 and doji == 0:
                return "T"
            elif adx < 25 and doji != 0:
                return "F"            
        except Exception as ex:
            print(f"Error in trends_defender: {ex}")
        return None

    def sigmals_handler_two(self, coins_list):
        orders_stek = []        
        for symbol in coins_list:
            total_signal = None
            kline_data = None
            try:                
                kline_data = self.get_klines(symbol, custom_period=None)  
                close_price = kline_data['Close'].iloc[-1]
                adx = self.calculate_adx(kline_data)                
                doji = self.calculate_doji(kline_data)
            except Exception as ex:
                print(f"Error processing {symbol} in sigmals_handler_two: {ex}")
                continue
            try:
                trend_sign = self.trends_defender(adx, doji)
                # print(trend_sign)
            except:
                continue
            if trend_sign == "T":
                FT_flag = 'T'
                current_bunch = self.BUNCH_DICT["T"][self.T_BUNCH_VARIANT]
            elif trend_sign == 'F':
                FT_flag = 'F'
                current_bunch = self.BUNCH_DICT["F"][self.F_BUNCH_VARIANT]
            else:
                continue
            try:
                total_signal = self.bunch_handler_func(close_price, current_bunch, kline_data, FT_flag)
            except:
                continue
            if total_signal:
                orders_stek.append({'symbol': symbol, 'side': total_signal})

        return orders_stek

