from API_BINANCE.delete_api import DELETEE_API

class UTILS_FOR_ORDERS(DELETEE_API):

    def __init__(self) -> None:
        super().__init__() 
        # print(self.URL_PATTERN_DICT) 

    def assets_filters(self):
        top_pairs = []
        all_tickers = []
        
        exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
        all_tickers = self.get_all_tickers()
        # print(all_tickers)

        if all_tickers:
            usdt_filtered = [ticker for ticker in all_tickers if
                            ticker['symbol'].upper().endswith('USDT') and
                            not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
                            (float(ticker['lastPrice']) >= self.MIN_FILTER_PRICE) and (float(ticker['lastPrice']) <= self.MAX_FILTER_PRICE)]
            
            # print(usdt_filtered[0])

            sorted_by_volume_data = sorted(usdt_filtered, key=lambda x: float(x['quoteVolume']), reverse=True)
            sorted_by_volume_data = sorted_by_volume_data[:self.SLICE_VOLUME_PAIRS]

            # Filter and sort by priceChangePercent
            sorted_by_price_change_data = sorted(sorted_by_volume_data, key=lambda x: float(x['priceChangePercent']), reverse=True)
            sorted_by_price_change_data = sorted_by_price_change_data[:self.SLICE_VOLATILITY]

            top_pairs = [x['symbol'] for x in sorted_by_price_change_data if x['symbol'] not in self.problem_pairs]

        return top_pairs

# utils_for_orderss = UTILS_FOR_ORDERS()
# print(UTILS_FOR_ORDERS().URL_PATTERN_DICT)

# all_tik = utils_for_orderss.assets_filters()
# print(all_tik)

# python -m API_BINANCE.utils_api


                