from config import Configg
import pandas as pd
from pparamss import STRATEGY_SET
from datetime import datetime

class GETT_API(Configg):
    
    def __init__(self) -> None:
        super().__init__()  
        
    def get_all_tickers(self):
        method = 'GET'

        all_tickers = None
        url = self.URL_PATTERN_DICT['all_tikers_url']       
        # print(url)
        all_tickers = self.HTTP_request(url, method=method, headers=self.header)

        return all_tickers
    
    def get_excangeInfo(self, symbol):
        method = 'GET'

        exchangeInfo = None
        if symbol:            
            url = f"{self.URL_PATTERN_DICT['exchangeInfo_url']}?symbol={symbol}"
        else:
            url = self.URL_PATTERN_DICT['exchangeInfo_url']        
        exchangeInfo = self.HTTP_request(url, method=method, headers=self.header)

        return exchangeInfo
    
    def get_balance(self):
        method = 'GET'
        current_balance = None 
        url = self.URL_PATTERN_DICT['balance_url']
        # print(url)
        params = {}
        
        if not self.test_flag:
            params['recvWindow'] = 5000
            params = self.get_signature(params)
            current_balance = self.HTTP_request(url, method=method, headers=self.header, params=params)
            
            if self.market == 'spot':                
                current_balance = dict(current_balance)                
                current_balanceE = current_balance['balances']
                current_balance = [(x['free'], x['locked']) for x in current_balanceE if x['asset'] == 'USDT'][0]          
            if self.market == 'futures':                
                current_balanceE = list(current_balance)
                current_balance = [(x['balance'], x['crossUnPnl']) for x in current_balanceE if x['asset'] == 'USDT'][0]
        else:
            params = self.get_signature(params)
            current_balance = self.HTTP_request(url, method=method, headers=self.header, params=params)
            current_balance = float([x['balance'] for x in current_balance if x['asset'] == 'USDT'][0])  
            # print(current_balance)
            
        return current_balance
    
    def get_position_price(self, symbol):
        method = 'GET'

        positions = None        
        url = self.URL_PATTERN_DICT['positions_url']
        params = {}
        params = self.get_signature(params)
        positions = self.HTTP_request(url, method=method, headers=self.header, params=params)
        # print(positions)
        positions = float([x for x in positions if x['symbol'] == symbol][0]["entryPrice"])

        return positions
    
    def get_klines(self, symbol, custom_period):
        method = 'GET'
        params = {}
        klines = None
        data = None
        url = self.URL_PATTERN_DICT["klines_url"]
        params["symbol"] = symbol
        params["interval"] = self.INTERVAL
        print(self.INTERVAL)

        if self.end_date and isinstance(self.end_date, datetime):
            params["endTime"] = int(self.end_date.timestamp() * 1000)
        if custom_period:
            params["limit"] = custom_period
        # params = self.get_signature(params)
        klines = self.HTTP_request(url, method=method, headers=self.header, params=params)

        if klines:
            try:
                data = pd.DataFrame(klines).iloc[:, :6]
                data.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
                data = data.set_index('Time')
                data.index = pd.to_datetime(data.index, unit='ms')
                data = data.astype(float)
            except Exception as e:
                print(f"Error processing klines: {e}")

        # len_data = len(data) if data is not None else 0
        # print(f"len data: {len_data}")
        return data

    
# ////////////////////////////////////////////////////////////////////////////////////

    def get_all_orders(self):
        method = 'GET'

        all_orders = None        
        params = {}               
        url = self.URL_PATTERN_DICT['get_all_orders_url']
        params = self.get_signature(params)
        all_orders = self.HTTP_request(url, method=method, headers=self.header, params=params)

        return all_orders
    
    def get_open_positions(self):
        method = 'GET'

        all_positions = None        
        params = {}          
        symbol = None     
        url = self.URL_PATTERN_DICT['positions_url']
        if symbol:
            params["symbol"] = symbol
        params = self.get_signature(params)
        all_positions = self.HTTP_request(url, method=method, headers=self.header, params=params)
        all_positions = [x for x in all_positions if float(x["positionAmt"]) != 0]

        return all_positions 
# //////////////////////////////////////////////////////////////////////////////////

# get_apii = GETT_API()

# kl = get_apii.get_klines('BNBUSDT')
# print(kl)
# python -m API_BINANCE.get_api
