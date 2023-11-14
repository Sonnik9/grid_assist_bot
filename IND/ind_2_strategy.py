
from API_BINANCE.utils_api import UTILS_FOR_ORDERS
from IND.ta_inds import TA_INDSS

class IND_STRATEGY_2(UTILS_FOR_ORDERS, TA_INDSS):
    def __init__(self) -> None:
        super().__init__()

    def bunch_handler_func(self, close_price, upper, lower, macd, signal, rsi, fastk, slowk, engulfing, doji, current_bunch, kline_data):
        signals_sum = []
        buy_signals_counter = 0
        sell_signals_counter = 0    
        total_signal = None
        # print(f"str14: {current_bunch}")

        if 'bband_flag' in current_bunch:            
            # buy_bband_signal, sell_bband_signal = False, False
            if self.inds_source == 'ta': 
                upper, lower = None, None
                upper, lower = self.calculate_bollinger_bands(kline_data)
            # print(upper, lower)
            try:                     
                buy_bband_signal = close_price >= lower * self.b_bband_q
                sell_bband_signal = close_price <= upper * self.s_bband_q
                signals_sum.append((buy_bband_signal, sell_bband_signal))
            except Exception as ex:
                print(ex)

        if 'macd_lite_flag' in current_bunch:            
            # buy_lite_macd_signal, sell_lite_macd_signal = False, False
            # print(self.inds_source)
            if self.inds_source == 'ta': 
                macd, signal = None, None
                macd, signal = self.calculate_macd(kline_data)
            # print(macd, signal)
            try:                      
                buy_lite_macd_signal = macd > signal * self.b_macd__q
                sell_lite_macd_signal = macd < signal * self.s_macd_q
                signals_sum.append((buy_lite_macd_signal, sell_lite_macd_signal))
            except Exception as ex:
                print(ex)

        if 'macd_strong_flag' in current_bunch:
            if self.inds_source == 'ta': 
                macd, signal = self.calculate_macd(kline_data)
            try:                        
                buy_strong_macd_signal = (macd > signal * self.b_macd__q) & (macd < 0)
                sell_strong_macd_signal = (macd < signal * self.s_macd_q) & (macd > 0)
                signals_sum.append((buy_strong_macd_signal, sell_strong_macd_signal))
            except Exception as ex:
                print(ex)

        if 'rsi_strong_flag' in current_bunch:   
            if self.inds_source == 'ta':                
                rsi = self.calculate_rsi(kline_data)                
            try:           
                buy_rsi_signal = rsi <= self.b_rsi_lev                
                sell_rsi_signal = rsi >= self.s_rsi_lev                
                signals_sum.append((buy_rsi_signal, sell_rsi_signal))
            except Exception as ex:
                print(ex)

        if 'rsi_lite_flag' in current_bunch:            
            buy_rsi_signal, sell_rsi_signal = False, False
            if self.inds_source == 'ta': 
                rsi = None                
                rsi = self.calculate_rsi(kline_data)               
            try:   
                if 'U' in current_bunch or 'F' in current_bunch:       
                    buy_rsi_signal = rsi < self.s_rsi_lite_lev
                elif 'D' in current_bunch or 'F' in current_bunch:
                    sell_rsi_signal = rsi > self.b_rsi_lite_lev
                signals_sum.append((buy_rsi_signal, sell_rsi_signal))
            except Exception as ex:
                print(ex)

        if 'stoch_flag' in current_bunch:            
            # buy_stoch_signal, sell_stoch_signal = False, False
            if self.inds_source == 'ta':
                fastk, slowk = None, None
                fastk, slowk = self.calculate_stochastic_oscillator(kline_data)
            try:
                buy_stoch_signal = (fastk > slowk) & (fastk < self.b_stoch_q)
                sell_stoch_signal = (fastk < slowk) & (fastk > self.s_stoch_q)
                signals_sum.append((buy_stoch_signal, sell_stoch_signal))
            except Exception as ex:
                print(ex)

        if 'engulfing_flag' in current_bunch:
            if self.inds_source == 'ta':
                engulfing = self.calculate_engulfing_patterns(kline_data)
            try:
                buy_engulfing_signal = engulfing > 0
                sell_engulfing_signal = engulfing < 0
                signals_sum.append((buy_engulfing_signal, sell_engulfing_signal))
            except Exception as ex:
                print(ex)

        if 'doji_flag' in current_bunch:
            if self.inds_source == 'ta':
                doji = self.calculate_doji(kline_data)  
            try:
                buy_doji_signal = doji != 0
                sell_doji_signal = doji != 0
                signals_sum.append((buy_doji_signal, sell_doji_signal))
            except Exception as ex:
                print(ex)

        for buy_signal, sell_signal in signals_sum:
            if buy_signal:
                buy_signals_counter += 1
            if sell_signal:
                sell_signals_counter += 1

        if 'U' in current_bunch:
            if buy_signals_counter == len(signals_sum):
                total_signal = 'BUY'
            else:
                total_signal = 'NEUTRAL'

        if 'D'in current_bunch:
            if sell_signals_counter == len(signals_sum):
                total_signal = 'SELL'
            else:
                total_signal = 'NEUTRAL'
        if 'F' in current_bunch:
            if buy_signals_counter == len(signals_sum):
                total_signal = 'F_BUY'
            elif sell_signals_counter == len(signals_sum):
                total_signal = 'F_SELL'
            else:
                total_signal = 'F_NEUTRAL'

        return total_signal

    def trends_defender(self, close_price, adx, sma20):
        try:
            if close_price > sma20 and adx > 25:
                return "U"
            elif close_price < sma20 and adx > 25:
                return "D"
            else:
                return "F"
        except:
            return None

    def sigmals_handler_two(self, coins_list, data_analysis): 
        # print('ksfbvkfbvfk')
        orders_stek = []

        for i in range(len(coins_list)):
            close_price, upper, lower, macd, signal, rsi, fastk, slowk, engulfing, doji = None, None, None, None, None, None, None, None, None, None
            total_signal = None
            current_bunch = []
            if self.inds_source == 'tv':
                kline_data = None
                try:
                    symboll, close_price, adx, sma20, upper, lower, macd, signal, rsi, fastk, slowk = data_analysis[i][0], data_analysis[i][1], data_analysis[i][2], data_analysis[i][3], data_analysis[i][4], data_analysis[i][5], data_analysis[i][6], data_analysis[i][7], data_analysis[i][8], data_analysis[i][9], data_analysis[i][10]
                except:
                    continue

            if self.inds_source == 'ta':           
                symboll = coins_list[i]
                kline_data = []
                try:
                    kline_data = self.get_klines(symboll)
                    close_price = kline_data['Close'].iloc[-1]
                    adx = self.calculate_adx(kline_data)
                    sma20 = self.calculate_sma(kline_data)
                except:
                    continue

            trende_sign = self.trends_defender(close_price, adx, sma20)
            # print(trende_sign)
            # print(self.current_bunch)
            if trende_sign == 'U':
                current_bunch = self.current_bunch + ['U']            
            elif trende_sign == 'D':
                current_bunch = self.current_bunch + ['D']
            elif trende_sign == 'F':         
                # current_bunch = ['bband_flag', 'macd_lite_flag', 'F']  
                current_bunch = ['stoch_flag', 'macd_lite_flag', 'F']         
                # current_bunch = ['stoch_flag', 'macd_lite_flag', 'doji_flag', 'F']
            else:
                continue
                
            total_signal = self.bunch_handler_func(close_price, upper, lower, macd, signal, rsi, fastk, slowk, engulfing, doji, current_bunch, kline_data)
            # print(total_signal)
            if total_signal:
                orders_stek.append({'symbol': symboll, 'side': total_signal})

        return orders_stek