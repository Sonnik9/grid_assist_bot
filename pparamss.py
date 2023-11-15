from datetime import datetime

class MAIN_PARAMETRS():
    def __init__(self):
        self.SOLI_DEO_GLORIA = 'Soli Deo Gloria!'        
        self.market = 'spot'
        self.test_flag = False # -- real    
        # self.market = 'futures'
        # self.test_flag = True # -- test        

    def update_main_params(self, new_market, new_test_flag=False):
        self.market = new_market
        self.test_flag = new_test_flag

class URL_TEMPLATES(MAIN_PARAMETRS):
    def __init__(self) -> None:
        super().__init__()
        self.URL_PATTERN_DICT= {}
        self.init_urls() 

    def init_urls(self):        
        if self.market == 'spot':                
            self.URL_PATTERN_DICT['all_tikers_url'] = "https://api.binance.com/api/v3/ticker/24hr"
            self.URL_PATTERN_DICT['create_order_url'] = 'https://api.binance.com/api/v3/order' 
            self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://api.binance.com/api/v3/exchangeInfo'
            self.URL_PATTERN_DICT['balance_url'] = 'https://api.binance.com/api/v3/account'
            self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://api.binance.com/api/v3/openOrders'
            self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://api.binance.com/api/v3/allOpenOrders'
            self.URL_PATTERN_DICT['positions_url'] = 'https://api.binance.com/api/v3/account'
            # print('hi')
            self.URL_PATTERN_DICT["klines_url"] = 'https://api.binance.com/api/v3/klines'

        else:
            self.URL_PATTERN_DICT['all_tikers_url'] = "https://fapi.binance.com/fapi/v1/ticker/24hr"
            self.URL_PATTERN_DICT['create_order_url'] = 'https://fapi.binance.com/fapi/v1/order' 
            self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://fapi.binance.com/fapi/v1/exchangeInfo'
            self.URL_PATTERN_DICT['balance_url'] = 'https://fapi.binance.com/fapi/v2/balance'
            self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/openOrders'
            self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/allOpenOrders'
            self.URL_PATTERN_DICT['positions_url'] = 'https://fapi.binance.com/fapi/v2/positionRisk'
            self.URL_PATTERN_DICT["set_leverage_url"] = 'https://fapi.binance.com/fapi/v1/leverage'
            self.URL_PATTERN_DICT["klines_url"] = 'https://fapi.binance.com/fapi/v1/klines'

class TIME_TEMPLATES(URL_TEMPLATES):
   
    def __init__(self) -> None:
        super().__init__()
        self.KLINE_TIME, self.TIME_FRAME = 1, 'h'
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
        self.KLINES_PERIOD = 200   
        self.init_time()        

    def init_time(self):  
        if self.test_flag:
            self.end_date = datetime(2023, 11, 1)
        else:
            self.end_date = None
    # ///////////////////////////////////////////////
    def update_time_temps(self, new_kline_time, new_time_frame, new_end_date, new_klines_period): 
        self.KLINE_TIME, self.TIME_FRAME = int(new_kline_time), new_time_frame.strip().lower()
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
        new_end_date = tuple(new_end_date)
        self.end_date = datetime(new_end_date[0], new_end_date[1], new_end_date[2])        
        self.KLINES_PERIOD = int(new_klines_period)    
        # ///////////////////////////////////////////////////////////////////////////

class INDICATORD_PARAMS(TIME_TEMPLATES):
    def __init__(self) -> None:
        super().__init__()
        self.b_bband_q, self.s_bband_q = 1, 1
        self.b_rsi_lev, self.s_rsi_lev = 33, 67   
        self.b_rsi_diver_lev = 50 
        self.rsi_period = 12    
        self.b_macd_q, self.s_macd_q = 1, 1
        self.b_stoch_q, self.s_stoch_q = 23, 77
        
    def update_ind_params(self, new_b_bband_q, new_s_bband_q, new_b_rsi_lev, new_s_rsi_lev, new_b_macd__q, new_s_macd_q, new_b_stoch_q, new_s_stoch_q):
        self.b_bband_q, self.s_bband_q = new_b_bband_q, new_s_bband_q
        self.b_rsi_lev, self.s_rsi_lev = new_b_rsi_lev, new_s_rsi_lev
        self.b_macd_q, self.s_macd_q = new_b_macd__q, new_s_macd_q
        self.b_stoch_q, self.s_stoch_q = new_b_stoch_q, new_s_stoch_q

class FILTER_SET(INDICATORD_PARAMS):
    def __init__(self) -> None:
        super().__init__()
        self.SLICE_VOLUME_PAIRS = 41 # volums
        self.SLICE_VOLATILITY = 39 # volatility
        self.MIN_FILTER_PRICE = 0.01 # min price
        self.MAX_FILTER_PRICE = 3000000 # max price
        # self.problem_pairs = ['SOLUSDT', 'ZECUSDT', 'MKRUSDT', 'COMPUSDT', 'ORDIUSDT']
        self.problem_pairs = ['DOGEUSDT'] # problem coins list

    def update_filter_set(self, new_slice_volun_pairs, new_slice_volatility, new_min_filter_price, new_max_filter_price, new_problem_pairs):       
        self.SLICE_VOLUME_PAIRS = new_slice_volun_pairs
        self.SLICE_VOLATILITY = new_slice_volatility
        self.MIN_FILTER_PRICE = new_min_filter_price 
        self.MAX_FILTER_PRICE = new_max_filter_price 
        self.problem_pairs = new_problem_pairs 

class STRATEGY_SET(FILTER_SET):
    def __init__(self) -> None:
        super().__init__()
        self.inds_source = 'ta'         
        self.BUNCH_VARIANT = 7
        self.strong_trande_sign = True
        self.PIVOT_GENERAL_TYPE = 'Classic'
        # self.PIVOT_GENERAL_TYPE = 'Fibonacci'
        self.pivot_levels_type = 1
        self.grid_decimal = 5
        self.init_strategy_set()

    def update_strategy_set(self, new_ind_strategy, new_inds_source, new_BUNCH_VARIANT, new_pivot_gen_type, new_pivot_levels_type, new_grid_decimal):
        self.ind_strategy = new_ind_strategy       
        self.inds_source = new_inds_source         
        self.BUNCH_VARIANT = new_BUNCH_VARIANT
        self.PIVOT_GENERAL_TYPE = new_pivot_gen_type
        self.pivot_levels_type = new_pivot_levels_type
        self.grid_decimal = new_grid_decimal

    def init_strategy_set(self):
        if self.BUNCH_VARIANT == 1:
            self.current_bunch = ['bband_flag', 'macd_lite_flag', 'rsi_diver_flag']
        elif self.BUNCH_VARIANT == 2:
            self.current_bunch = ['bband_flag', 'macd_lite_flag', 'stoch_flag']
        elif self.BUNCH_VARIANT == 3:
            self.current_bunch = ['bband_flag', 'macd_lite_flag', 'doji_flag'] 
        elif self.BUNCH_VARIANT == 4:
            self.current_bunch = ['bband_flag', 'macd_strong_flag']
        elif self.BUNCH_VARIANT == 5:
            self.current_bunch = ['bband_flag', 'macd_lite_flag', 'rsi_overtrading_flag']
        elif self.BUNCH_VARIANT == 6:
            self.current_bunch = ['bband_flag', 'rsi_overtrading_flag']
        elif self.BUNCH_VARIANT == 7:
            self.current_bunch = ['heikin_ashi_flag', 'rsi_diver_flag'] 
        if self.BUNCH_VARIANT == 8:
            self.current_bunch = ['bband_flag', 'macd_lite_flag']
        elif self.BUNCH_VARIANT == 9:
            self.current_bunch = ['bband_flag', 'macd_lite_flag', 'ma_99_checkin_flag', 'rsi_diver_flag'] 

# python -m pparamss
