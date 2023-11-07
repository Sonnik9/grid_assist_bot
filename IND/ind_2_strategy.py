from pparamss import my_params
from API_BINANCE.get_api import get_apii
from IND.ta_inds import ta_iindss

def bunch_handler_func(close_price, upper, lower, macd, signal, rsi, fastk, slowk, current_bunch):
    b_bband_q, s_bband_q, b_rsi_lev, s_rsi_lev, b_macd__q, s_macd_q, b_stoch_q, s_stoch_q = 1, 1, 45, 55, 1, 1, 23, 77
    # 33, 67
    # 25, 75

    signals_sum = []
    buy_signals_counter = 0
    sell_signals_counter = 0
    buy_total_signal, sell_total_signal = False, False

    if 'bband_flag' in current_bunch: 
        try:            
            buy_bband_signal = close_price >= lower * b_bband_q
            sell_bband_signal = close_price <= upper * s_bband_q
            signals_sum.append((buy_bband_signal, sell_bband_signal))
        except Exception as ex:
            print(ex)

    if 'macd_lite_flag' in current_bunch:
        try:              
            buy_lite_macd_signal = macd > signal * b_macd__q
            sell_lite_macd_signal = macd < signal * s_macd_q
            signals_sum.append((buy_lite_macd_signal, sell_lite_macd_signal))
        except Exception as ex:
            print(ex)

    if 'macd_strong_flag' in current_bunch:  
        try:        
            buy_strong_macd_signal = (macd > signal * b_macd__q) & (macd < 0)
            sell_strong_macd_signal = (macd < signal * s_macd_q) & (macd > 0)
            signals_sum.append((buy_strong_macd_signal, sell_strong_macd_signal))
        except Exception as ex:
            print(ex)

    if 'rsi_flag' in current_bunch:                
        buy_rsi_signal = rsi <= b_rsi_lev
        sell_rsi_signal = rsi >= s_rsi_lev
        signals_sum.append((buy_rsi_signal, sell_rsi_signal))

    if 'stoch_flag' in current_bunch:
        try:
            buy_stoch_signal = (fastk > slowk) & (fastk < b_stoch_q)
            sell_stoch_signal = (fastk < slowk) & (fastk > s_stoch_q)
            signals_sum.append((buy_stoch_signal, sell_stoch_signal))
        except Exception as ex:
            print(ex)

    for buy_signal, sell_signal in signals_sum:
        if buy_signal:
            buy_signals_counter += 1
        if sell_signal:
            sell_signals_counter += 1

    if 'U' in current_bunch:
        if buy_signals_counter == len(signals_sum):
            buy_total_signal = True 
    if 'D':
        if sell_signals_counter == len(signals_sum):
            sell_total_signal = True
    if 'F' in current_bunch:
        if buy_signals_counter == len(signals_sum):
            buy_total_signal = True 
        if sell_signals_counter == len(signals_sum):
            sell_total_signal = True

    return buy_total_signal, sell_total_signal

def trends_defender(close_price, adx, sma):

    if close_price > sma and adx > 25:
        return "U"
    elif close_price < sma and adx > 25:
        return "D"
    else:
        return "F"
        
def get_ta_signals(top_coins):
    klines_data = []
    for symbol in top_coins:
        # print(symbol)
        try:
            kline_data = get_apii.get_klines(symbol)
            # print(kline_data)
            close_price = kline_data['Close'].iloc[-1]
            adx = ta_iindss.calculate_adx(kline_data)
            sma26 = ta_iindss.calculate_sma(kline_data)
            upper, lower = ta_iindss.calculate_bollinger_bands(kline_data)                 
            macd, signal = ta_iindss.calculate_macd(kline_data)
            rsi = ta_iindss.calculate_rsi(kline_data)
            fastk, slowk = ta_iindss.calculate_stochastic_oscillator(kline_data)   
            klines_data.append({
                'symbol': symbol,
                'close_price': close_price,
                'ADX': adx, 
                'SMA20': sma26, 
                "BB.upper": upper,
                "BB.lower": lower,
                "MACD.macd": macd,
                "MACD.signal": signal,
                "RSI": rsi,
                "Stoch.K": fastk,
                "Stoch.D": slowk,
                })
        except Exception as ex:
            # print(ex) 
            pass

    return klines_data

def sigmals_handler_two(data): 
    # print('ksfbvkfbvfk')
    
    close_price, adx, sma, upper, lower, macd, signal, rsi, fastk, slowk = None, None, None, None, None, None, None, None, None, None
    
    orders_stek = []

    if my_params.inds_source == 'tv':
        data_previous_stek = []
        for _, item in data.items():
            try: 
                symboll = item.symbol  
                close_price = item.indicators['close']        
                adx = item.indicators["ADX"] 
                sma = item.indicators["SMA20"] 
                upper, lower = item.indicators["BB.upper"], item.indicators["BB.lower"] 
                macd, signal = item.indicators["MACD.macd"], item.indicators["MACD.signal"]     
                rsi = item.indicators["RSI"]
                fastk, slowk = item.indicators["Stoch.K"], item.indicators["Stoch.D"]
                data_previous_stek.append((symboll, close_price, adx, sma, upper, lower, macd, signal, rsi, fastk, slowk))
            except Exception as ex:
                pass
    elif my_params.inds_source == 'ta':
        # print('hello ta')
        data_previous_stek = []
        for item in data:
            try:
                symboll = item["symbol"]
                close_price = item['close_price']        
                adx = item["ADX"] 
                sma = item["SMA20"] 
                upper, lower = item["BB.upper"], item["BB.lower"] 
                macd, signal = item["MACD.macd"], item["MACD.signal"]     
                rsi = item["RSI"]
                fastk, slowk = item["Stoch.K"], item["Stoch.D"]
                data_previous_stek.append((symboll, close_price, adx, sma, upper, lower, macd, signal, rsi, fastk, slowk))
            except:
                pass
    for symboll, close_price, adx, sma, upper, lower, macd, signal, rsi, fastk, slowk in data_previous_stek:
        buy_signal, sell_signal = False, False
        trende_sign = trends_defender(close_price, adx, sma)
        # print(trende_sign)

        if not my_params.NEUTRAL_FLAG:                            
            if trende_sign == 'U':
                if my_params.BUNCH_VARIANT == 1:
                    current_bunch = ['bband_flag', 'macd_strong_flag', 'U']
                elif my_params.BUNCH_VARIANT == 2:
                    current_bunch = ['bband_flag', 'macd_lite_flag', 'rsi_flag', 'U']
                # current_bunch = ['bband_flag', 'macd_lite_flag', 'U']            
                
            if trende_sign == 'D':
                if my_params.BUNCH_VARIANT == 1:
                    current_bunch = ['bband_flag', 'macd_strong_flag', 'D']
                elif my_params.BUNCH_VARIANT == 2:
                    current_bunch = ['bband_flag', 'macd_lite_flag', 'rsi_flag', 'D']
                # current_bunch = ['bband_flag', 'macd_lite_flag', 'D']            
            
        if trende_sign == 'F':
            if my_params.BUNCH_VARIANT == 1:               
                current_bunch = ['macd_strong_flag', 'stoch_flag', 'F']
            elif my_params.BUNCH_VARIANT == 2:
                current_bunch = ['macd_lite_flag', 'stoch_flag', 'F']

        buy_signal, sell_signal = bunch_handler_func(close_price, upper, lower, macd, signal, rsi, fastk, slowk, current_bunch)
        
        if not my_params.NEUTRAL_FLAG:
            if buy_signal:
                orders_stek.append({'symbol': symboll, 'side': 'BUY'})
            # elif sell_signal and my_params.MARKET == 'futures':
            elif sell_signal:        
                orders_stek.append({'symbol': symboll, 'side': 'SELL'})
            elif buy_signal == sell_signal:
                orders_stek.append({'symbol': symboll, 'side': 'NEUTRAL'})
        else:
            if buy_signal == sell_signal:
                orders_stek.append({'symbol': symboll, 'side': 'NEUTRAL'})

    return orders_stek