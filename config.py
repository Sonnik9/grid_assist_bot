from pparamss import my_params
import logging, os, inspect
from dotenv import load_dotenv
import time
import hmac
import hashlib
import requests

logging.basicConfig(filename='config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

load_dotenv()

class Configg():

    def __init__(self) -> None:
        if not my_params.TEST_FLAG:
            self.api_key  = os.getenv("BINANCE_API_PUBLIC_KEY_REAL", "")
            self.api_secret = os.getenv("BINANCE_API_PRIVATE_KEY_REAL", "")

        else:
            if my_params.MARKET == 'spot':
                self.api_key  = os.getenv("BINANCE_API_PUBLIC_KEY_SPOT_TEST", "")
                self.api_secret = os.getenv("BINANCE_API_PRIVATE_KEY_SPOT_TEST", "")

            if my_params.MARKET == 'futures':
                self.api_key  = os.getenv("BINANCE_API_PUBLIC_KEY_FUTURES_TEST", "")
                self.api_secret = os.getenv("BINANCE_API_PRIVATE_KEY_FUTURES_TEST", "")
        self.tg_api_token = os.getenv("TG_API_TOKEN", "")
        
        
        # print(self.api_key)
        # print(self.api_secret)
        # print(self.tg_api_token)
        self.header = {
            'X-MBX-APIKEY': self.api_key
        }

    def get_signature(self, params):
        try:
            params['timestamp'] = int(time.time() *1000)
            params_str = '&'.join([f'{k}={v}' for k,v in params.items()])
            hash = hmac.new(bytes(self.api_secret, 'utf-8'), params_str.encode('utf-8'), hashlib.sha256)        
            params['signature'] = hash.hexdigest()
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

        return params
   
    def HTTP_request(self, url, **kwards):

        response = None
        multipliter = 2

        for i in range(2):
            try:
                # print('hi')
                response = requests.request(url=url, **kwards)
                # print(response)
                if response.status_code == 200:
                    break
                else:
                    time.sleep((i+1) * multipliter)              
   
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
                time.sleep((i+1) * multipliter)                
                
        try:
            # print(response)
            response = response.json()
        except:
            pass

        return response

# python -m config
