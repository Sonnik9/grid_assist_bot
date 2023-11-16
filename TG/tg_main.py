# # python -m TG.tg_main
import telebot
from telebot import types
from config import Configg
from BACKTEST.back_test import BACKTESTT
import time

class TG_CONNECTOR(BACKTESTT):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(Configg().tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SEARCHING", "SETTINGS", "CALC", "BALANCE", "RESTART", "1", "2"]        
        self.custom_redirect_flag = False  
        self.calc_flag = False
        self.settings_flag = False
        
    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("SEARCHING")
        button2 = types.KeyboardButton("SETTINGS")
        button3 = types.KeyboardButton("CALC")
        button4 = types.KeyboardButton("BACKTEST")
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
                # print(message.text)
                return message.text
            except:
                time.sleep(2 + i*decimal)        
        return None    
    
class TG_ASSISTENT(TG_CONNECTOR):
    def __init__(self):
        super().__init__()

    def update_main_paramss(self, new_market):
        super().update_main_params(new_market)
        self.init_urls()

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
            top_updated_coins_list = self.find_the_top_coin()
            for i in range(len(top_updated_coins_list)):
                top_updated_coins_list[i] = f"{top_updated_coins_list[i]['symbol']}: {top_updated_coins_list[i]['side']}"

            top_updated_coins_str = '\n'.join(top_updated_coins_list)
            response_message = f"TOP LIST:\n\n{top_updated_coins_str}"
            message.text = self.connector_func(bot, message, response_message) 

        @bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):
            response_message = "Please select a market type:\nSpot: 1;\nFutures: 2;" 
            message.text = self.connector_func(bot, message, response_message) 
            self.settings_flag = True

        @bot.message_handler(func=lambda message: message.text == "1"  and self.settings_flag)
        def set_spot_answer(message): 
            self.update_main_paramss('spot')
            response_message = f'The market was changed to {self.market.upper()} type'
            message.text = self.connector_func(bot, message, response_message) 
            self.settings_flag = False 

        @bot.message_handler(func=lambda message: message.text == "2" and self.settings_flag)
        def set_futures_answer(message): 
            self.update_main_paramss('futures')
            response_message = f'The market was changed to {self.market.upper()} type'
            message.text = self.connector_func(bot, message, response_message) 
            self.settings_flag = False

        @bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            balance = self.get_balance()
            response_message = f"Your {self.market} balance is: {balance}"
            message.text = self.connector_func(bot, message, response_message)            

        @bot.message_handler(func=lambda message: message.text == "CALC")
        def custom_calc_redirect(message):
            response_message = "Please enter a coin (e.g., BTC)"
            message.text = self.connector_func(bot, message, response_message)            
            self.custom_redirect_flag = True

        @bot.message_handler(func=lambda message: self.custom_redirect_flag)
        def custom_calc(message):
            symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = None, None, None, None, None, None, None
            try:                 
                symbol = message.text.strip().upper() + 'USDT'               
                symbol, direction, resistance_piv, support_piv, grid_number, tp, sl = self.find_the_best_coin(symbol)                
            except: 
                response_message = "Enter a VALID coin (e.g., BTCUSDT)"
                message.text = self.connector_func(bot, message, response_message)    

            try:
                response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
                message.text = self.connector_func(bot, message, response_message)
                self.custom_redirect_flag = False                
            except Exception as ex:
                print(ex)

        @bot.message_handler(func=lambda message: message.text == "BACKTEST")
        def custom_calc_redirect(message):
            response_message = "Please enter a coin for bbacktesting (e.g., BTC)"
            message.text = self.connector_func(bot, message, response_message)            
            self.bt_flag = True

        @bot.message_handler(func=lambda message: self.bt_flag)
        def custom_calc_redirect(message):
            symbol = message.text.strip().upper() + 'USDT'
            bt_repl = self.backtest_main(symbol) 
            try:
                response_message = bt_repl
                # response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
                message.text = self.connector_func(bot, message, response_message) 
            except Exception as ex:
                print(ex)        
            self.bt_flag = False

        @bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            response_message = f"Try again and enter a valid option."
            message.text = self.connector_func(bot, message, response_message)  
                     

        bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()