# python -m TG.tg_main
import telebot
from telebot import types
from config import Configg
from API_BINANCE.get_api import get_apii
from API_BINANCE.utils_api import utils_for_orderss
from CALC.atr_calc import calculate_atr
from CALC.grid_number_calc import grid_calc_func
from CALC.tv_ind import tv_infoo
from pparamss import my_params

class TG_ASSISTENT(Configg):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(self.tg_api_token)
        self.menu_markup = self.create_menu()

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("SET UP")
        button2 = types.KeyboardButton("CUSTOM CALC")
        button3 = types.KeyboardButton("AUTO CALC")
        button4 = types.KeyboardButton("BALANCE")
        menu_markup.add(button1, button2, button3, button4)
        return menu_markup
    
    def calc_set(self):
        top_coins = []
        top_coins = utils_for_orderss.assets_filters()
        tv_info_repl = None
        upper_piv, resistance_piv = None, None
        symbol = top_coins[0]
        data = get_apii.get_klines(symbol) 
        print(symbol)   
        character = 'INDS'
        assets = []
        assets.append(symbol)
        tv_info_repl = tv_infoo.get_tv_info(character, assets)
        upper_piv, resistance_piv = tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.R{my_params.pivot_levels_type}'], tv_info_repl[symbol][f'Pivot.M.{my_params.PIVOT_GENERAL_TYPE}.S{my_params.pivot_levels_type}']
        atr = calculate_atr(data)
        print(upper_piv, resistance_piv)
        grid_number = grid_calc_func(upper_piv, resistance_piv, atr)
        return symbol, upper_piv, resistance_piv, grid_number

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @self.bot.message_handler(func=lambda message: message.text in ["SET UP", "CUSTOM CALC", "AUTO CALC", "BALANCE"])
        def handle_button_selection(message):
            if message.text == "SET UP":
                pass
            if message.text == "CUSTOM CALC":
                pass
            elif message.text == 'BALANCE':
                balance = get_apii.get_balance()
                self.bot.send_message(message.chat.id, f"Your balance is: {balance}")
            elif message.text == 'AUTO CALC':
                symbol, upper_piv, resistance_piv, grid_number = self.calc_set()
                self.bot.send_message(message.chat.id, f"Symbol: {symbol}\nUpper_piv: {upper_piv}\nResistance_piv: {resistance_piv}\nGrid numder : {grid_number}")

        self.bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()

main_tg_func()
