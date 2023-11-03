from pparamss import my_params
from API_BINANCE.get_api import get_apii
# from API_BINANCE.post_api import post_apii

class UTILS_FOR_ORDERS():

    def __init__(self) -> None:
        pass

    def assets_filters(self):
        top_pairs = []
        all_tickers = []
        exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
        all_tickers = get_apii.get_all_tickers()

        if all_tickers:
            usdt_filtered = [ticker for ticker in all_tickers if
                            ticker['symbol'].upper().endswith('USDT') and
                            not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
                            (float(ticker['lastPrice']) >= my_params.MIN_FILTER_PRICE) and (float(ticker['lastPrice']) <= my_params.MAX_FILTER_PRICE)]
            
            # print(usdt_filtered[0])

            sorted_by_volume_data = sorted(usdt_filtered, key=lambda x: float(x['quoteVolume']), reverse=True)
            sorted_by_volume_data = sorted_by_volume_data[:my_params.SLICE_VOLUME_PAIRS]

            # Filter and sort by priceChangePercent
            sorted_by_price_change_data = sorted(sorted_by_volume_data, key=lambda x: float(x['priceChangePercent']), reverse=True)
            sorted_by_price_change_data = sorted_by_price_change_data[:my_params.SLICE_CHANGINGPRICES_PAIRS]

            top_pairs = [x['symbol'] for x in sorted_by_price_change_data if x['symbol'] not in my_params.problem_pairs]

        return top_pairs

utils_for_orderss = UTILS_FOR_ORDERS()

# python -m API_BINANCE.utils_api


                