
class Parameters:
    def __init__(self):
        self.SOLI_DEO_GLORIA = 'Soli Deo Gloria!'
        self.MARKET = 'futures'
        # self.market = 'spot'
        # self.test_flag = False # -- real
        self.TEST_FLAG = True # -- test
        # self.SLIPPAGE_COEFFICIENT = 0.005  # Коэффициент погрешности 0.5%         
        
class TEMPLATES(Parameters):
   
    def __init__(self) -> None:
        super().__init__()
        self.TERMINATE_TIMER_FLAG = False
        self.REST_TIME = {
            "from": 1,
            "to": 3
        }
        self.KLINE_TIME, self.TIME_FRAME = 1, 'd'
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
        
        # ///////////////////////////////////////////////////////////////////////////////

        # //////////////////////////////////////////////////////////////////////////////
        self.URL_PATTERN_DICT= {}
        if not self.TEST_FLAG:
            if self.MARKET == 'spot':                
                self.URL_PATTERN_DICT['all_tikers_url'] = "https://api.binance.com/api/v3/ticker/24hr"
                self.URL_PATTERN_DICT['create_order_url'] = 'https://api.binance.com/api/v3/order' 
                self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://api.binance.com/api/v3/exchangeInfo'
                self.URL_PATTERN_DICT['balance_url'] = 'https://api.binance.com/api/v3/account'
                self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://api.binance.com/api/v3/openOrders'
                self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://api.binance.com/api/v3/allOpenOrders'

            else:
                self.URL_PATTERN_DICT['all_tikers_url'] = "https://fapi.binance.com/fapi/v1/ticker/24hr"
                self.URL_PATTERN_DICT['create_order_url'] = 'https://fapi.binance.com/fapi/v1/order' 
                self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://fapi.binance.com/fapi/v1/exchangeInfo'
                self.URL_PATTERN_DICT['balance_url'] = 'https://fapi.binance.com/fapi/v1/balance'
                self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/openOrders'
                self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/allOpenOrders'
        else:
            if self.MARKET == 'spot':
                self.URL_PATTERN_DICT['all_tikers_url'] = "https://testnet.binance.com/v3/ticker/24hr"
                self.URL_PATTERN_DICT['create_order_url'] = 'https://testnet.binance.vision/api/v3/order' 
                self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://testnet.binance.vision/api/v3/exchangeInfo'
                self.URL_PATTERN_DICT['balance_url'] = 'https://testnet.binance.vision/api/v3/account'
                self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://testnet.binance.vision/api/v3/openOrders'
                self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://testnet.binance.vision/api/v3/allOpenOrders'

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
        self.SLICE_VOLUME_PAIRS = 10
        self.SLICE_CHANGINGPRICES_PAIRS = 10
        self.FILTER_PRICE = 0.1
        self.problem_pairs = ['SOLUSDT', 'ZECUSDT', 'MKRUSDT', 'COMPUSDT']
        # self.QNT_ROUNDING_TYPE = 'ceil'
        self.QNT_ROUNDING_TYPE = 'round'
        # self.QNT_ROUNDING_TYPE = 'floor'
# //////////////////////////////////////////////////////////////////
        self.interval_shedjule_step = 30
        self.KLINES_PERIOD = 21
        self.pivot_levels_type = 3
        self.grid_decimal = 2.5

my_params = TEMPLATES()

# python -m pparamss
