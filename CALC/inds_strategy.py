from CALC.indicators import OTHERS_CALC, TALIB_INDSS

class IND_STRATEGY_(OTHERS_CALC, TALIB_INDSS):
    def __init__(self) -> None:
        super().__init__()

    def bunch_handler_func(self, close_price, current_bunch, kline_data):
        signals_sum = []
        buy_signals_counter = 0
        sell_signals_counter = 0
        total_signal = 'NEUTRAL'

        try:
            if 'bband_flag' in current_bunch:
                upper, lower = self.calculate_bollinger_bands(kline_data)
                buy_bband_signal = close_price >= lower * self.b_bband_q
                sell_bband_signal = close_price <= upper * self.s_bband_q
                signals_sum.append((buy_bband_signal, sell_bband_signal))

            if 'macd_lite_flag' in current_bunch:
                macd, signal = self.calculate_macd(kline_data)
                buy_lite_macd_signal = macd > signal * self.b_macd_q
                sell_lite_macd_signal = macd < signal * self.s_macd_q
                signals_sum.append((buy_lite_macd_signal, sell_lite_macd_signal))

            if 'macd_strong_flag' in current_bunch:
                macd, signal = self.calculate_macd(kline_data)
                buy_strong_macd_signal = (macd > signal * self.b_macd_q) and (macd < 0)
                sell_strong_macd_signal = (macd < signal * self.s_macd_q) and (macd > 0)
                signals_sum.append((buy_strong_macd_signal, sell_strong_macd_signal))

            if 'ma_crossover_flag' in current_bunch:
                ma_7, ma_25, ma_99 = self.calculate_ma_s(kline_data)
                buy_ma_crossover_signal = ma_7 > ma_25 and ma_25 > ma_99
                sell_ma_crossover_signal = ma_7 < ma_25 and ma_25 < ma_99
                signals_sum.append((buy_ma_crossover_signal, sell_ma_crossover_signal))                

            if 'rsi_diver_flag' in current_bunch:
                rsi = self.calculate_rsi(kline_data)
                buy_rsi_signal = (rsi > self.b_rsi_diver_lev) and (rsi < self.s_rsi_lev) if 'U' in current_bunch or 'F' in current_bunch else False
                sell_rsi_signal = (rsi < self.b_rsi_diver_lev) and (rsi > self.b_rsi_lev) if 'D' in current_bunch or 'F' in current_bunch else False
                signals_sum.append((buy_rsi_signal, sell_rsi_signal))

            if 'rsi_overtrading_flag' in current_bunch:
                rsi = self.calculate_rsi(kline_data)
                buy_rsi_signal = rsi <= self.b_rsi_lev
                sell_rsi_signal = rsi >= self.s_rsi_lev
                signals_sum.append((buy_rsi_signal, sell_rsi_signal))

            if 'heikin_ashi_strategy_flag' in current_bunch:
                ema_10, ema_30 = self.calculate_ema_s(kline_data)
                heiken_close, heiken_open, heiken_signal = self.calculate_heikin_ashi(kline_data)
                buy_heikin_ashi_signal = (ema_10 > ema_30) and (heiken_open < ema_10) and (heiken_close > ema_10) and (heiken_signal == 1)
                sell_heikin_ashi_signal = (ema_10 < ema_30) and (heiken_open > ema_10) and (heiken_close < ema_10) and (heiken_signal == -1)
                signals_sum.append((buy_heikin_ashi_signal, sell_heikin_ashi_signal))

            if 'stoch_flag' in current_bunch:
                fastk, slowk = self.calculate_stochastic_oscillator(kline_data)
                buy_stoch_signal = (fastk > slowk) and (fastk < self.b_stoch_q)
                sell_stoch_signal = (fastk < slowk) and (fastk > self.s_stoch_q)
                signals_sum.append((buy_stoch_signal, sell_stoch_signal))

            for buy_signal, sell_signal in signals_sum:
                if buy_signal:
                    buy_signals_counter += 1
                if sell_signal:
                    sell_signals_counter += 1

            if 'U' in current_bunch:
                if len(signals_sum) != 0:
                    total_signal = 'BUY' if buy_signals_counter == len(signals_sum) else 'U_NEUTRAL'

            if 'D'in current_bunch:
                if len(signals_sum) != 0:
                    total_signal = 'SELL' if sell_signals_counter == len(signals_sum) else 'D_NEUTRAL'
        except Exception as ex:
            print(ex)

        return total_signal

    def trends_defender(self, close_price, adx, sma7, sma25, sma99, doji):
        try:
            u_conditions = [close_price > sma7, close_price > sma25, doji == 0]
            d_conditions = [close_price < sma7, close_price < sma25, doji == 0]
            if self.strong_trande_sign:
                u_conditions.append(close_price > sma99)
                d_conditions.append(close_price < sma99)

            if adx > 25:
                u_condition_met = all(u_conditions)
                d_condition_met = all(d_conditions)

                if u_condition_met:
                    return "U"
                elif d_condition_met:
                    return "D"
                else:
                    return "F"
            else:
                return "F"
        except Exception as ex:
            print(f"Error in trends_defender: {ex}")
            return None

    def sigmals_handler_two(self, coins_list):
        orders_stek = []

        for symbol in coins_list:
            try:
                kline_data = None
                kline_data = self.get_klines(symbol, custom_period=None)  
                if len(kline_data) == 0:
                    continue    

                close_price = kline_data['Close'].iloc[-1]
                adx = self.calculate_adx(kline_data)
                sma7, sma25, sma99 = self.calculate_ma_s(kline_data)
                doji = self.calculate_doji(kline_data)
            except Exception as ex:
                print(f"Error processing {symbol} in sigmals_handler_two: {ex}")
                continue
            try:
                trend_sign = self.trends_defender(close_price, adx, sma7, sma25, sma99, doji)
                print(trend_sign)
            except:
                continue
            if trend_sign == 'U':
                current_bunch = self.current_bunch + ['U']
            elif trend_sign == 'D':
                current_bunch = self.current_bunch + ['D']
            elif trend_sign == 'F':
                orders_stek.append({'symbol': symbol, 'side': 'F_NEUTRAL'})
                continue
            try:
                total_signal = self.bunch_handler_func(close_price, current_bunch, kline_data)
            except:
                continue
            if total_signal:
                orders_stek.append({'symbol': symbol, 'side': total_signal})

        return orders_stek

