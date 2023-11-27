# # python -m TG.tg_main
import telebot
from telebot import types
from config import Configg
import time
from datetime import datetime
from time_keep import kline_waiter


from CALC.calc_controller import CALC_MANAGER

class TG_CONNECTOR(CALC_MANAGER):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(Configg().tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SEARCHING", "SETTINGS", "GO", "TEST", "BALANCE", "RESTART", "1", "2"]        
        self.custom_redirect_flag = False  
        self.calc_flag = False
        self.settings_flag = False
        self.market_flag = False
        self.test_tg_flag = False
        self.bt_redirect_1_flag = False
        self.bt_redirect_2_flag = False
        self.time_keeper_flag = False
        self.test_symbol = None
        
    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("SEARCHING")
        button2 = types.KeyboardButton("SETTINGS")
        button3 = types.KeyboardButton("GO")        
        button4 = types.KeyboardButton("WAIT TIME")
        button5 = types.KeyboardButton("BALANCE")
        button6 = types.KeyboardButton("RESTART")
        menu_markup.add(button1, button2, button3, button4, button5, button6)        
        return menu_markup

    def connector_func(self, bot, message, response_message):
        retry_number = 3
        decimal = 2        
        for i in range(retry_number):
            try:
                bot.send_message(message.chat.id, response_message)                
                return message.text
            except:
                time.sleep(2 + i*decimal)        
        return None    
    
class TG_ASSISTENT(TG_CONNECTOR):
    def __init__(self):
        super().__init__()

    def update_main_paramss(self, new_market, new_test_flag):
        self.market = new_market
        self.test_flag = new_test_flag
        self.init_itits()

    def run(self):
        bot = self.bot        

        @bot.message_handler(commands=['start'])
        def handle_start(message):
            bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):
            bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == "SEARCHING")
        def searching(message):
            top_updated_coins_list = []
            top_updated_coins_list = self.find_the_top_coin()
            try:
                for i in range(len(top_updated_coins_list)):
                    top_updated_coins_list[i] = f"{top_updated_coins_list[i]['symbol']}: {top_updated_coins_list[i]['side']}"
            except Exception as ex:
                print(ex)
            print(top_updated_coins_list)
            top_updated_coins_str = '\n'.join(top_updated_coins_list)
            response_message = f"MARKET:{self.market.upper()}\  '1h'  '4h'  '1d':\n\n{top_updated_coins_str}"
            message.text = self.connector_func(bot, message, response_message) 

        @bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):
            response_message = "Please select a settings options:\nMarket: 1;\nTest_flag: 2;" 
            message.text = self.connector_func(bot, message, response_message) 
            self.settings_flag = True

        @bot.message_handler(func=lambda message: message.text == "1"  and self.settings_flag)
        def settingss1(message):
            response_message = "Please select a market type:\nSpot: 1;\nFutures: 2;" 
            message.text = self.connector_func(bot, message, response_message)           
            self.market_flag = True
            self.settings_flag = False

        @bot.message_handler(func=lambda message: message.text == "1"  and self.market_flag)
        def set_spot_answer(message): 
            self.update_main_paramss('spot', self.test_flag)
            response_message = f'The market was changed to {self.market.upper()} type'
            message.text = self.connector_func(bot, message, response_message) 
            self.market_flag = False 
            self.settings_flag = False

        @bot.message_handler(func=lambda message: message.text == "2" and self.market_flag)
        def set_futures_answer(message): 
            self.update_main_paramss('futures', self.test_flag)
            response_message = f'The market was changed to {self.market.upper()} type'
            message.text = self.connector_func(bot, message, response_message) 
            self.market_flag = False 
            self.settings_flag = False

        @bot.message_handler(func=lambda message: message.text == "2"  and self.settings_flag)
        def settingss2(message):
            response_message = "Please change a test flag:\nFalse: 1;\nTrue: 2;" 
            message.text = self.connector_func(bot, message, response_message)           
            self.test_tg_flag = True
            self.settings_flag = False

        @bot.message_handler(func=lambda message: message.text == "1"  and self.test_tg_flag)
        def set_testFalse_flag_answer(message): 
            self.update_main_paramss(self.market, False)
            response_message = f'The testFlag was changed to False'
            message.text = self.connector_func(bot, message, response_message) 
            self.test_tg_flag = False 
            self.settings_flag = False

        @bot.message_handler(func=lambda message: message.text == "2"  and self.test_tg_flag)
        def set_testTrue_flag_answer(message): 
            self.update_main_paramss(self.market, True)
            response_message = f'The testFlag was changed to True'
            message.text = self.connector_func(bot, message, response_message) 
            self.test_tg_flag = False 
            self.settings_flag = False

        @bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            balance = self.get_balance()
            response_message = f"Your {self.market} balance is: {balance}"
            message.text = self.connector_func(bot, message, response_message)   

        # //////////////////////////////////////////////////////////////////////  

        @bot.message_handler(func=lambda message: message.text == "GO")
        def custom_calc_redirect(message):
            response_message = "Please enter a coin (e.g., BTC)"
            message.text = self.connector_func(bot, message, response_message)            
            self.custom_redirect_flag = True

        @bot.message_handler(func=lambda message: self.custom_redirect_flag)
        def custom_calc(message):
            direction, last_close_price, resistance_piv, support_piv, grid_number, sl, tp = '', '', '', '', '', '', ''
            symbol = message.text.strip().upper() + 'USDT'

            try:       
                answer = self.find_the_best_coin(symbol)  
                direction = answer['direction'] + '  '
                last_close_price = answer['last_close_price']
                resistance_piv = answer['resistance_piv']
                support_piv = answer['support_piv']
                tp = answer['tp']
                sl = answer['sl']
                grid_number = answer['grid_number']
            except Exception as ex:
                print(ex)

                          
            except: 
                response_message = "Enter a VALID coin (e.g., BTCUSDT)"
                message.text = self.connector_func(bot, message, response_message)    

            try:
                response_message = f"MARKET: {self.market.upper()}  '1h'  '4h'  '1d'\n\nSymbol: {symbol}\nDirection: {direction}\nLastClosePrice: {last_close_price}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
                message.text = self.connector_func(bot, message, response_message)
                self.custom_redirect_flag = False                
            except Exception as ex:
                print(ex)

        # ////////////////////////////////////////////////////////////////////////

        @bot.message_handler(func=lambda message: message.text == "WAIT TIME")
        def test_func(message):
            response_message = "Please enter a time_frame using '/' (e.g., '1/h)"
            message.text = self.connector_func(bot, message, response_message)            
            self.time_keeper_flag = True
        @bot.message_handler(func=lambda message: self.time_keeper_flag)
        def wait_time_calculate(message):
            wait_time = None
            interval = message.text
            wait_time = kline_waiter(interval)
            try:  
                message.text = self.connector_func(bot, message, wait_time)
            except:
                pass
            self.time_keeper_flag = False


        # @bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        # def exceptions_input(message):
        #     response_message = f"Try again and enter a valid option."
        #     message.text = self.connector_func(bot, message, response_message)                 

        bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()