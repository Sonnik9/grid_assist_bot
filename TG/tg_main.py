# # python -m TG.tg_main
import telebot
from telebot import types
from config import Configg

from API_BINANCE.get_api import get_apii
from CALC.calc_controller import calc_controllerr

from pparamss import my_params
import sys, os
import subprocess

# class TG_ASSISTENT(Configg):
#     def __init__(self):
#         super().__init__()
#         self.bot = telebot.TeleBot(self.tg_api_token)
#         self.menu_markup = self.create_menu()
#         self.reserved_frathes_list = ["SEARCHING", "SETTINGS", "CALC", "BALANCE", "RESTART", 1, 2]        
#         self.custom_redirect_flag = False  
#         self.calc_flag = False      

#     def create_menu(self):
#         menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
#         button1 = types.KeyboardButton("SEARCHING")
#         button2 = types.KeyboardButton("SETTINGS")
#         button3 = types.KeyboardButton("CALC")
#         button4 = types.KeyboardButton("BALANCE")
#         button5 = types.KeyboardButton("RESTART")
#         menu_markup.add(button1, button2, button3, button4, button5)        
#         return menu_markup  

#     def run(self):

#         @self.bot.message_handler(commands=['start'])
#         def handle_start(message):
#             self.bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)
#         @self.bot.message_handler(func=lambda message: message.text == 'RESTART')
#         def handle_start(message):
#             self.bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

#         @self.bot.message_handler(func=lambda message: message.text == "SEARCHING")
#         def searching(message):            
#             top_updated_coins_list = []
#             top_updated_coins_list = calc_controllerr.find_the_top_coin()
#             top_updated_coins_list = [str(x)[1:-1] for x in top_updated_coins_list]
#             top_updated_coins_str = '\n'.join(top_updated_coins_list)
#             self.bot.send_message(message.chat.id, f"TOP LIST:\n\n{top_updated_coins_str}")
#         @self.bot.message_handler(func=lambda message: message.text == "BALANCE")
#         def balance(message):
            
#             balance = None
#             try:
#                 balance = get_apii.get_balance()
#             except:
#                 pass
#             try:
#                 self.bot.send_message(message.chat.id, f"Your balance is: {balance}")
#             except:
#                 pass

#         @self.bot.message_handler(func=lambda message:message.text == "CALC")
#         def calc_input(message): 
#             self.bot.send_message(message.chat.id, "Please choice the way of calculation:\nDefault - 1;\nCustom - 2;")
#             self.calc_flag = True

#         @self.bot.message_handler(func=lambda message:message.text == "1" and self.calc_flag)
#         def default_calc(message): 
#             # print('default calc')
#             symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = None, None, None, None, None, None, None
#             try:
#                 symbol = None
#                 target = 'default_calc'
#                 self.calc_flag = False  
#                 symbol, direction, resistance_piv, support_piv, grid_number, tp, sl = calc_controllerr.find_the_best_coin(symbol, target)                
#             except:
#                 pass
#             try:
#                 response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
#                 self.bot.send_message(message.chat.id, response_message)   
                        
#             except Exception as ex:
#                 print(ex)
#                 response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
#                 self.bot.send_message(message.chat.id, response_message)              

#         @self.bot.message_handler(func=lambda message:message.text == "2" and self.calc_flag)
#         def custom_calc_redirect(message): 
#             self.bot.send_message(message.chat.id, "Please enter a coin (e.g., BTCUSDT)")
#             self.custom_redirect_flag = True 

#         @self.bot.message_handler(func=lambda message: self.custom_redirect_flag)
#         def custom_calc(message):
#             # print('custom calc')
#             symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = None, None, None, None, None, None, None
#             try:                 
#                 symbol = message.text
#                 print(symbol)
#                 target = 'custom_calc'
#                 symbol, direction, resistance_piv, support_piv, grid_number, tp, sl = calc_controllerr.find_the_best_coin(symbol, target)                
#             except:               
#                 self.bot.send_message(message.chat.id, "Enter a VALID coin (e.g., BTCUSDT)")
#             try:
#                 response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
#                 self.bot.send_message(message.chat.id, response_message)
#                 self.custom_redirect_flag = False
#                 self.calc_flag = False        
#             except Exception as ex:
#                 print(ex)
#                 response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
#                 self.bot.send_message(message.chat.id, response_message)
#                 self.custom_redirect_flag = False
#                 self.calc_flag = False
#         @self.bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
#         def exceptions_input(message):
#             self.bot.send_message(message.chat.id, f"Try again and enter a valid option!")

#         self.bot.polling()

# def main_tg_func():   
#     my_bot = TG_ASSISTENT()
#     my_bot.run()

# # main_tg_func()
class TG_CONNECTOR(Configg):
    def __init__(self):
        self.bot = telebot.TeleBot(Configg().tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SEARCHING", "SETTINGS", "CALC", "BALANCE", "RESTART", 1, 2]        
        self.custom_redirect_flag = False  
        self.calc_flag = False

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("SEARCHING")
        button2 = types.KeyboardButton("SETTINGS")
        button3 = types.KeyboardButton("CALC")
        button4 = types.KeyboardButton("BALANCE")
        button5 = types.KeyboardButton("RESTART")
        menu_markup.add(button1, button2, button3, button4, button5)        
        return menu_markup


class TG_ASSISTENT(TG_CONNECTOR):
    def __init__(self):
        super().__init__()
        self.calc_flag = False

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
            top_updated_coins_list = calc_controllerr.find_the_top_coin()
            top_updated_coins_list = [str(x)[1:-1] for x in top_updated_coins_list]
            top_updated_coins_str = '\n'.join(top_updated_coins_list)
            bot.send_message(message.chat.id, f"TOP LIST:\n\n{top_updated_coins_str}")

        @bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            balance = get_apii.get_balance()
            bot.send_message(message.chat.id, f"Your balance is: {balance}")

        @bot.message_handler(func=lambda message: message.text == "CALC")
        def calc_input(message):
            bot.send_message(message.chat.id, "Please choice the way of calculation:\nDefault: 1;\nCustom: 2;")
            self.calc_flag = True

        @bot.message_handler(func=lambda message: message.text == "1" and self.calc_flag)
        def default_calc(message):
            symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = calc_controllerr.find_the_best_coin(symbol, 'default_calc')
            response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
            bot.send_message(message.chat.id, response_message)

        @bot.message_handler(func=lambda message: message.text == "2" and self.calc_flag)
        def custom_calc_redirect(message):
            bot.send_message(message.chat.id, "Please enter a coin (e.g., BTCUSDT)")
            self.custom_redirect_flag = True

        @bot.message_handler(func=lambda message: self.custom_redirect_flag)
        def custom_calc(message):
            symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = calc_controllerr.find_the_best_coin(symbol, 'custom_calc')
            response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nTake Profit: {tp}\nStop Loss: {sl}\nGrid number: {grid_number}"
            bot.send_message(message.chat.id, response_message)
            self.custom_redirect_flag = False
            self.calc_flag = False

        @bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            bot.send_message(message.chat.id, f"Try again and enter a valid option.")

        bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()