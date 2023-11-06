from pparamss import my_params

def sigmals_handler_one(all_coins_indicators):

    signals_stek = []

    for _, item in all_coins_indicators.items():
        recommendation = None
        symboll = None
        try:
            symboll = item.symbol
            recommendation = item.summary["RECOMMENDATION"]
        except Exception as ex:
            pass
        if not my_params.NEUTRAL_FLAG:
            if recommendation == 'STRONG_BUY':
                try:
                    signals_stek.append({'symbol': symboll, 'side': 'BUY'})         
                except:
                    pass
            # elif recommendation == 'STRONG_SELL' and my_params.MARKET == 'futures':
            elif recommendation == 'STRONG_SELL':  
                try:      
                    signals_stek.append({'symbol': symboll, 'side': 'SELL'})            
                except:
                    pass
            else:
                signals_stek.append({'symbol': symboll, 'side': 'NEUTRAL'})
        else:
            if recommendation != 'STRONG_BUY' and recommendation != 'STRONG_SELL':
                signals_stek.append({'symbol': symboll, 'side': 'NEUTRAL'})

    return signals_stek 

# {'Recommend.Other': -0.18181818, 'Recommend.All': 0.04242424, 'Recommend.MA': 0.26666667, 'RSI': 54.20381438, 'RSI[1]': 58.67116828, 'Stoch.K': 35.60606061, 'Stoch.D': 43.30808081, 'Stoch.K[1]': 47.72727273, 'Stoch.D[1]': 44.19939035, 'CCI20': -27.14524637, 'CCI20[1]': 36.1716857, 'ADX': 50.93654474, 'ADX+DI': 26.14947246, 'ADX-DI': 11.02997995, 'ADX+DI[1]': 27.54384028, 'ADX-DI[1]': 11.21820901, 'AO': 6.35764706, 'AO[1]': 6.56176471, 'Mom': -2.2, 'Mom[1]': 1.2, 'MACD.macd': 3.06507751, 'MACD.signal': 3.67487682, 'Rec.Stoch.RSI': 0, 'Stoch.RSI.K': 9.70543452, 'Rec.WR': 0, 'W.R': -73.29545455, 'Rec.BBPower': 0, 'BBPower': -0.76922264, 'Rec.UO': 0, 'UO': 52.37757674, 'close': 241.8, 'EMA5': 243.36709337, 'SMA5': 244.34, 'EMA10': 243.12294056, 'SMA10': 243.48, 'EMA20': 241.21888844, 'SMA20': 242.885, 'EMA30': 238.83675011, 'SMA30': 238.46, 'EMA50': 234.94148358, 'SMA50': 233.106, 'EMA100': 230.0185729, 'SMA100': 225.974, 'EMA200': 225.07772111, 'SMA200': 225.2575, 'Rec.Ichimoku': 0, 'Ichimoku.BLine': 240.4, 'Rec.VWMA': -1, 'VWMA': 243.69529639, 'Rec.HullMA9': -1, 'HullMA9': 244.91666667, 'Pivot.M.Classic.S3': 157.83333333, 'Pivot.M.Classic.S2': 197.73333333, 'Pivot.M.Classic.S1': 220.56666667, 'Pivot.M.Classic.Middle': 237.63333333, 'Pivot.M.Classic.R1': 260.46666667, 'Pivot.M.Classic.R2': 277.53333333, 'Pivot.M.Classic.R3': 317.43333333, 'Pivot.M.Fibonacci.S3': 197.73333333, 'Pivot.M.Fibonacci.S2': 212.97513333, 'Pivot.M.Fibonacci.S1': 222.39153333, 'Pivot.M.Fibonacci.Middle': 237.63333333, 'Pivot.M.Fibonacci.R1': 252.87513333, 'Pivot.M.Fibonacci.R2': 262.29153333, 'Pivot.M.Fibonacci.R3': 277.53333333, 'Pivot.M.Camarilla.S3': 232.4275, 'Pivot.M.Camarilla.S2': 236.085, 'Pivot.M.Camarilla.S1': 239.7425, 'Pivot.M.Camarilla.Middle': 237.63333333, 'Pivot.M.Camarilla.R1': 247.0575, 'Pivot.M.Camarilla.R2': 250.715, 'Pivot.M.Camarilla.R3': 254.3725, 'Pivot.M.Woodie.S3': 183.55, 'Pivot.M.Woodie.S2': 199.175, 'Pivot.M.Woodie.S1': 223.45, 'Pivot.M.Woodie.Middle': 239.075, 'Pivot.M.Woodie.R1': 263.35, 'Pivot.M.Woodie.R2': 278.975, 'Pivot.M.Woodie.R3': 303.25, 'Pivot.M.Demark.S1': 229.1, 'Pivot.M.Demark.Middle': 241.9, 'Pivot.M.Demark.R1': 269, 'open': 244, 'P.SAR': 237.00322915, 'BB.lower': 238.61591345, 'BB.upper': 247.15408655, 'AO[2]': 6.49588235, 'volume': 6169.952, 'change': -0.90163934, 'low': 240.3, 'high': 244.3}


