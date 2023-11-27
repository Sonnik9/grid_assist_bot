from CALC.indicators import OTHERS_CALC, PANDAS_TA_INDSS

class IND_STRATEGY_(OTHERS_CALC, PANDAS_TA_INDSS):
    def __init__(self) -> None:
        super().__init__()

    def bunch_handler_func(self, current_bunch, df, FT_flag):
        signals_sum = []
        buy_signals_counter = 0
        sell_signals_counter = 0
        total_signal = None   
        close_price = df.Close.iloc[-1]     

        try:
            if 'bb_fib_flag' in current_bunch:     
                buy_bband_signal, sell_bband_signal = False, False           
                df = self.calculate_bollinger_bands(df)
                buy_bband_signal = close_price > df['BBL_30_1.618'].iloc[-1] and close_price < df['BBM_30_1.382'].iloc[-1]
                sell_bband_signal = close_price < df['BBU_30_1.618'].iloc[-1] and close_price > df['BBM_30_1.382'].iloc[-1]
                signals_sum.append((buy_bband_signal, sell_bband_signal))

            if 'bb_fib2_doji_pattern_flag' in current_bunch:     
                buy_bband_signal, sell_bband_signal = False, False           
                df = self.calculate_bollinger_bands(df)
                # print(df)
                bb_l = df['BBL_30_1.618'].iloc[-1]
                bb_u = df['BBU_30_1.618'].iloc[-1]
                df = self.calculate_doji(df)
                doji = df["Doji"].iloc[-1]
                # print(close_price)
                # print(doji)
                # print(bb_l)
                # print(bb_u)
                buy_bband_signal = close_price < bb_l and doji == 100
                sell_bband_signal = close_price > bb_u and doji == 100
                signals_sum.append((buy_bband_signal, sell_bband_signal))

            if 'macd_cross_flag' in current_bunch: 
                buy_macd_cross_signal, sell_macd_cross_signal = False,False               
                df = self.calculate_macd(df)
                # print(df.MACD_12_26_9.iloc[-1])
                # print(df.MACDs_12_26_9.iloc[-1])
                # print(df.MACD_12_26_9.iloc[-2])
                # print(df.MACDs_12_26_9.iloc[-2])
                buy_macd_cross_signal = (df.MACD_12_26_9.iloc[-1] > df.MACDs_12_26_9.iloc[-1]) and ((df.MACD_12_26_9.iloc[-2] < df.MACDs_12_26_9.iloc[-2]) or (df.MACD_12_26_9.iloc[-3] < df.MACDs_12_26_9.iloc[-3]))           
                sell_macd_cross_signal = (df.MACD_12_26_9.iloc[-1] < df.MACDs_12_26_9.iloc[-1]) and ((df.MACD_12_26_9.iloc[-2] > df.MACDs_12_26_9.iloc[-2]) or (df.MACD_12_26_9.iloc[-3] > df.MACDs_12_26_9.iloc[-3]))
                signals_sum.append((buy_macd_cross_signal, sell_macd_cross_signal))

            if 'macd_flag' in current_bunch:                
                df = self.calculate_macd(df)
                buy_lite_macd_signal = df.MACD_12_26_9.iloc[-1] > df.MACDs_12_26_9.iloc[-1] and df.MACD_12_26_9.iloc[-1] > 0 and df.MACDs_12_26_9.iloc[-1] > 0
                sell_lite_macd_signal = df.MACD_12_26_9.iloc[-1] < df.MACDs_12_26_9.iloc[-1] and df.MACD_12_26_9.iloc[-1] < 0 and df.MACDs_12_26_9.iloc[-1] < 0
                signals_sum.append((buy_lite_macd_signal, sell_lite_macd_signal))


            if 'sma_lite_flag' in current_bunch: 
                buy_ma_lite_signal, sell_ma_lite_signal = False, False               
                df = self.calculate_ma_s(df)
                # print(df)
                # print(df["MA20"].iloc[-1])
                # print(df["MA50"].iloc[-1])
                buy_ma_lite_signal = (df["MA20"].iloc[-1] > df["MA50"].iloc[-1]) and (close_price > df["MA20"].iloc[-1]) and (close_price > df["MA50"].iloc[-1])
                sell_ma_lite_signal = (df["MA20"].iloc[-1] < df["MA50"].iloc[-1]) and (close_price < df["MA20"].iloc[-1]) and (close_price < df["MA50"].iloc[-1])
                signals_sum.append((buy_ma_lite_signal, sell_ma_lite_signal)) 

            if 'sma_strong_flag' in current_bunch: 
                buy_ma_strong_signal, sell_ma_strong_signal = False, False              
                df = self.calculate_ma_s(df)
                buy_ma_strong_signal = (df["MA7"].iloc[-1] > df["MA25"].iloc[-1]) and (df["MA25"].iloc[-1] > df["MA99"].iloc[-1]) and (close_price > df["MA7"].iloc[-1] and close_price > df["MA25"].iloc[-1] and close_price > df["MA99"].iloc[-1])
                sell_ma_strong_signal = (df["MA7"].iloc[-1] < df["MA25"].iloc[-1]) and (df["MA25"].iloc[-1] < df["MA99"].iloc[-1]) and (close_price < df["MA7"].iloc[-1] and close_price < df["MA25"].iloc[-1] and close_price < df["MA99"].iloc[-1])
                signals_sum.append((buy_ma_strong_signal, sell_ma_strong_signal))  

            if 'sma_crossover_flag' in current_bunch:  
                buy_ma_crossover_signal, sell_ma_crossover_signal = False, False              
                df = self.calculate_ma_s(df)
                buy_ma_crossover_signal = (df["MA20"].iloc[-1] > df["MA50"].iloc[-1]) and ((df["MA20"].iloc[-2] < df["MA50"].iloc[-2]) or (df["MA20"].iloc[-3] < df["MA50"].iloc[-3]))
                sell_ma_crossover_signal = (df["MA20"].iloc[-1] < df["MA50"].iloc[-1]) and ((df["MA20"].iloc[-2] > df["MA50"].iloc[-2]) or (df["MA20"].iloc[-3] > df["MA50"].iloc[-3]))
                signals_sum.append((buy_ma_crossover_signal, sell_ma_crossover_signal))               

            if 'rsi_pattern_flag' in current_bunch:               
                buy_rsi_diver_signal, sell_rsi_diver_signal = False, False 
                df = self.calculate_rsi(df)    
                data_rsi = df["RSI12"].iloc[-4:].to_list()     
                # print(data_rsi)       
                last_rsi = data_rsi[-1]    
                # print(last_rsi)            
                data_close_price = df['Close'].iloc[-4:].to_list()
                # print(data_close_price)
                detect_rsi = self.detect_rsi_divergence(data_close_price, data_rsi)
                buy_rsi_diver_signal = (detect_rsi == 2) or (last_rsi <= self.b_rsi_lev)
                sell_rsi_diver_signal = (detect_rsi == 1) or (last_rsi >= self.s_rsi_lev)
                signals_sum.append((buy_rsi_diver_signal, sell_rsi_diver_signal))
                
            if 'rsi_overtrading_flag' in current_bunch:
                df = self.calculate_rsi(df)
                rsi = df["RSI12"].iloc[-1]
                buy_rsi_signal = rsi <= self.b_rsi_lev
                sell_rsi_signal = rsi >= self.s_rsi_lev
                signals_sum.append((buy_rsi_signal, sell_rsi_signal))

            if 'heikin_ashi_strategy_flag' in current_bunch:
                buy_heikin_ashi_signal, sell_heikin_ashi_signal = False, False
                df = self.calculate_ema_s(df)
                ema_10, ema_30 = df["EMA10"].iloc[-1], df["EMA30"].iloc[-1]
                # print(ema_10, ema_30)
                df = self.calculate_doji(df)
                doji = df["Doji"].iloc[-1]
                # print(doji)
                heiken_close, heiken_open, heiken_signal = self.calculate_heikin_ashi(df)
                # print(heiken_close, heiken_open, heiken_signal)
                buy_heikin_ashi_signal = (ema_10 > ema_30) and (heiken_open < ema_10) and (heiken_close > ema_10) and (heiken_signal == 2) and (doji == 0)
                sell_heikin_ashi_signal = (ema_10 < ema_30) and (heiken_open > ema_10) and (heiken_close < ema_10) and (heiken_signal == 1) and (doji == 0)
                signals_sum.append((buy_heikin_ashi_signal, sell_heikin_ashi_signal))

           
            buy_signals_counter += sum(buy_signal for buy_signal, _ in signals_sum)
            sell_signals_counter += sum(sell_signal for _, sell_signal in signals_sum)

            total_signal = f'{FT_flag}_BUY' if buy_signals_counter == len(signals_sum) else \
                           f'{FT_flag}_SELL' if sell_signals_counter == len(signals_sum) else \
                           f'{FT_flag}_N'

        except Exception as ex:
            print(f"str120: {ex}")
        
        return total_signal

    def trends_defender(self, adx):
        try:
            if adx > 25:
                return "T"
            elif adx < 25:
                return "F"            
        except Exception as ex:
            print(f"Error in trends_defender: {ex}")
        return None

    def sigmals_handler_two(self, symbol, df):
        direction = {}

        total_signal = ''           
        try:            
            df = self.calculate_adx(df)   
            adx = df["ADX"].iloc[-1]            
        except Exception as ex:
            print(f"Error processing {symbol} in sigmals_handler_two: {ex}")
            
        try:
            trend_sign = self.trends_defender(adx)
            # print(trend_sign)
        except:
            pass
        if trend_sign == "T":
            FT_flag = 'T'
            current_bunch = self.BUNCH_DICT["T"][self.T_BUNCH_VARIANT]
        elif trend_sign == 'F':
            FT_flag = 'F'
            current_bunch = self.BUNCH_DICT["F"][self.F_BUNCH_VARIANT]
        else:
            pass
        try:
            total_signal = self.bunch_handler_func(current_bunch, df, FT_flag)
        except:
            pass
        if total_signal:
            return total_signal
        else:
            return ''

