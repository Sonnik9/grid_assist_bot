from pparamss import my_params
from config import Configg
import pandas as pd
from API_BINANCE.get_api import get_apii

class DELETEE_API(Configg):

    def __init__(self) -> None:
        super().__init__()
        self.method = 'DELETE'

    def cancel_all_orders_for_position(self, symbol_list):
        cancel_orders_list = []      

        for item in symbol_list:
            cancel_order = None
            params = {}
            params["symbol"] = item
            params = self.get_signature(params)
            url = my_params.URL_PATTERN_DICT['cancel_all_orders_url']
            
            cancel_order = self.HTTP_request(url, method=self.method, headers=self.header, params=params)
            cancel_orders_list.append(cancel_order)
            
        return cancel_orders_list
    
    def cancel_all_open_orders(self):

        cancel_orders = None
        all_orders = None
        all_orders = get_apii.get_all_orders()

        for item in all_orders:
            params = {}
            params["symbol"] = item["symbol"]
            params = self.get_signature(params)
            url = my_params.URL_PATTERN_DICT['cancel_all_orders_url']
            method = 'DELETE'
            cancel_orders = self.HTTP_request(url, method=method, headers=self.header, params=params)
            # print(cancel_orders)

        return 
    
delete_apii = DELETEE_API()