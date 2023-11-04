# python -m TG.tg_main
import telebot
from telebot import types
from config import Configg

from API_BINANCE.get_api import get_apii
from CALC.utils_calc import find_the_top_coin, find_the_best_coin, find_the_coin_by_custom_way
# from API_BINANCE.utils_api import utils_for_orderss
# from CALC.atr_calc import calculate_atr
# from CALC.grid_number_calc import grid_calc_func
# from CALC.tv_ind import tv_infoo
from pparamss import my_params
import sys, os
import subprocess

class TG_ASSISTENT(Configg):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(self.tg_api_token)
        self.menu_markup = self.create_menu()
        self.custom_flag = False

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("SEARCHING")
        button2 = types.KeyboardButton("CUSTOM CALC")
        button3 = types.KeyboardButton("AUTO CALC")
        button4 = types.KeyboardButton("BALANCE")
        button5 = types.KeyboardButton("RESTART")
        menu_markup.add(button1, button2, button3, button4, button5)
        self.special_button_list = ["SEARCHING", "CUSTOM CALC", "AUTO CALC", "BALANCE"]
        return menu_markup  

    def run(self):

        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)
        @self.bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):
            self.bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

        @self.bot.message_handler(func=lambda message: message.text == "SEARCHING")
        def searching(message):            
            top_updated_coins_list = []
            top_updated_coins_list = find_the_top_coin()
            top_updated_coins_list = [str(x)[1:-1] for x in top_updated_coins_list]
            top_updated_coins_str = '\n'.join(top_updated_coins_list)
            self.bot.send_message(message.chat.id, f"TOP LIST:\n\n{top_updated_coins_str}")
        @self.bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            
            balance = None
            try:
                balance = get_apii.get_balance()
            except:
                pass
            try:
                self.bot.send_message(message.chat.id, f"Your balance is: {balance}")
            except:
                pass
        @self.bot.message_handler(func=lambda message: message.text == "AUTO CALC")
        def auto_calc(message):            
            symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = None, None, None, None, None, None, None
            try:
                symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = find_the_best_coin()
            except:
                pass
            try:
                self.bot.send_message(message.chat.id, f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nStop Loss: {sl}\nTake Profit: {tp}\nGrid numder : {grid_number}")
            except:
                pass

        @self.bot.message_handler(func=lambda message:message.text == "CUSTOM CALC")
        def custom_calc_input(message): 
            self.bot.send_message(message.chat.id, "Please enter the coin (e.g., BTCUSDT):")
            self.custom_flag = True  

        @self.bot.message_handler(func=lambda message: self.custom_flag)
        def custom_calc(message):  

            print('sfmvn sj')
            symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = None, None, None, None, None, None, None
            try:
                print(message.text)
                
                symbol, direction, resistance_piv, support_piv, grid_number, sl, tp = find_the_coin_by_custom_way(message.text)
                response_message = f"Symbol: {symbol}\nDirection: {direction}\nResistance_piv: {resistance_piv}\nSupport_piv: {support_piv}\nStop Loss: {sl}\nTake Profit: {tp}\nGrid number: {grid_number}"
                self.bot.send_message(message.chat.id, response_message)
                self.custom_flag = False
                
            except:
                self.bot.send_message(message.chat.id, "Please enter a valid coin (e.g., BTCUSDT)")

            # elif message.text not in self.special_button_list and message.text != '/start':
            #     self.bot.send_message(message.chat.id, f"Select the valid option!")

        self.bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()

# main_tg_func()
