from datetime import datetime

class MAIN_PARAMETRS:
    def __init__(self):
        self.SOLI_DEO_GLORIA = 'Soli Deo Gloria!'
        self.MARKET = 'futures'
        # self.market = 'spot'
        self.TEST_FLAG = True # -- test
        # self.test_flag = False # -- real        

class URL_TEMPLATES(MAIN_PARAMETRS):
    def __init__(self) -> None:
        super().__init__()
        self.URL_PATTERN_DICT= {}
        if not self.TEST_FLAG:
            if self.MARKET == 'spot':                
                self.URL_PATTERN_DICT['all_tikers_url'] = "https://api.binance.com/api/v3/ticker/24hr"
                self.URL_PATTERN_DICT['create_order_url'] = 'https://api.binance.com/api/v3/order' 
                self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://api.binance.com/api/v3/exchangeInfo'
                self.URL_PATTERN_DICT['balance_url'] = 'https://api.binance.com/api/v3/account'
                self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://api.binance.com/api/v3/openOrders'
                self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://api.binance.com/api/v3/allOpenOrders'
                self.URL_PATTERN_DICT['positions_url'] = 'https://api.binance.com/api/v3/account'
                self.URL_PATTERN_DICT["klines_url"] = 'https://api.binance.com/api/v1/klines'

            else:
                self.URL_PATTERN_DICT['all_tikers_url'] = "https://fapi.binance.com/fapi/v1/ticker/24hr"
                self.URL_PATTERN_DICT['create_order_url'] = 'https://fapi.binance.com/fapi/v1/order' 
                self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://fapi.binance.com/fapi/v1/exchangeInfo'
                self.URL_PATTERN_DICT['balance_url'] = 'https://fapi.binance.com/fapi/v1/balance'
                self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/openOrders'
                self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/allOpenOrders'
                self.URL_PATTERN_DICT['positions_url'] = 'https://fapi.binance.com/fapi/v2/positionRisk'
                self.URL_PATTERN_DICT["set_leverage_url"] = 'https://fapi.binance.com/fapi/v1/leverage'
                self.URL_PATTERN_DICT["klines_url"] = 'https://fapi.binance.com/fapi/v1/klines'

        else:
            if self.MARKET == 'spot':
                self.URL_PATTERN_DICT['all_tikers_url'] = "https://testnet.binance.com/v3/ticker/24hr"
                self.URL_PATTERN_DICT['create_order_url'] = 'https://testnet.binance.vision/api/v3/order' 
                self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://testnet.binance.vision/api/v3/exchangeInfo'
                self.URL_PATTERN_DICT['balance_url'] = 'https://testnet.binance.vision/api/v3/account'
                self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://testnet.binance.vision/api/v3/openOrders'
                self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://testnet.binance.vision/api/v3/allOpenOrders'
                self.URL_PATTERN_DICT['positions_url'] = 'https://testnet.binanceapi.com/api/v3/account'
                self.URL_PATTERN_DICT["klines_url"] = 'https://testnet.binanceapi.com/api/v1/klines'

            else:
                self.URL_PATTERN_DICT['all_tikers_url'] = "https://testnet.binancefuture.com/fapi/v1/ticker/24hr"
                self.URL_PATTERN_DICT['create_order_url'] = 'https://testnet.binancefuture.com/fapi/v1/order'
                self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://testnet.binancefuture.com/fapi/v1/exchangeInfo'
                self.URL_PATTERN_DICT['balance_url'] = 'https://testnet.binancefuture.com/fapi/v2/balance'
                self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://testnet.binancefuture.com/fapi/v1/openOrders'
                self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://testnet.binancefuture.com/fapi/v1/allOpenOrders'
                self.URL_PATTERN_DICT['positions_url'] = 'https://testnet.binancefuture.com/fapi/v2/positionRisk'
                self.URL_PATTERN_DICT["set_leverage_url"] = 'https://testnet.binancefuture.com/fapi/v1/leverage'
                self.URL_PATTERN_DICT["klines_url"] = 'https://testnet.binancefuture.com/fapi/v1/klines'
        # ////////////////////////////////////////////////////////////////////////////
       
class TIME_TEMPLATES(URL_TEMPLATES):
   
    def __init__(self) -> None:
        super().__init__()
        # self.TERMINATE_TIMER_FLAG = False        
        self.REST_TIME = {
            "from": 1,
            "to": 3
        }
        self.KLINE_TIME, self.TIME_FRAME = 1, 'd'
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
        self.end_date = datetime(2023, 11, 1)
        # self.end_date = None
        self.KLINES_PERIOD = 70        
        # //////////////////////////////////////////////////////////////////////////////

class INDICATORD_PARAMS(TIME_TEMPLATES):
    def __init__(self) -> None:
        super().__init__()
        self.b_bband_q, self.s_bband_q = 1, 1
        self.b_rsi_lev, self.s_rsi_lev = 33, 67 
        self.b_macd__q, self.s_macd_q = 1, 1
        self.b_stoch_q, self.s_stoch_q = 23, 77


class STRATEGY_SET(INDICATORD_PARAMS):
    def __init__(self) -> None:
        super().__init__()
        self.ind_strategy = 2
        self.inds_source = 'tv'
        # self.inds_source = 'ta'         
        self.BUNCH_VARIANT = 3
        if self.BUNCH_VARIANT == 1:
            self.current_bunch = ['bband_flag', 'macd_lite_flag', 'engulfing_flag']
        if self.BUNCH_VARIANT == 2:
            self.current_bunch = ['bband_flag', 'macd_lite_flag']
        elif self.BUNCH_VARIANT == 3:
            self.current_bunch = ['bband_flag', 'macd_strong_flag']
        elif self.BUNCH_VARIANT == 4:
            self.current_bunch = ['bband_flag', 'macd_lite_flag', 'rsi_flag']
        elif self.BUNCH_VARIANT == 5:
            self.current_bunch = ['bband_flag', 'rsi_flag'] 

        self.PIVOT_GENERAL_TYPE = 'Classic'
        # self.PIVOT_GENERAL_TYPE = 'Fibonacci'
        self.pivot_levels_type = 1
        self.grid_decimal = 10

        # //////////////////////// coins filter params //////////////////////
        self.SLICE_VOLUME_PAIRS = 12 # volums
        self.SLICE_CHANGINGPRICES_PAIRS = 11 # volatility
        # self.SLICE_MARKET_CAP_RANK = 10 #stakan
        # self.SLICE_SENTIMENTE_DATA_30D = 9 # ??
        self.MIN_FILTER_PRICE = 0.1 # min price
        self.MAX_FILTER_PRICE = 3000000 # max price
        self.problem_pairs = ['SOLUSDT', 'ZECUSDT', 'MKRUSDT', 'COMPUSDT', 'ORDIUSDT'] 

        #/////////////////////////////// other params//////////////////////
        # self.QNT_ROUNDING_TYPE = 'ceil'
        self.QNT_ROUNDING_TYPE = 'round'
        # self.QNT_ROUNDING_TYPE = 'floor'
        # //////////////////////////////////////////////////////////////////

my_params = STRATEGY_SET()

# python -m pparamss
