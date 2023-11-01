import telebot
# import requests
# from bs4 import BeautifulSoup
import schedule
import atexit
import time
import re
import random 
from random import choice 
from UTILS.clean_cache import cleanup_cache
from config import Configg
from pparamss import my_params

class Tg(Configg):

    def __init__(self) -> None:
        super().__init__()
        tg_api_token = self.tg_api_token
        self.bot = telebot.TeleBot(tg_api_token)
        # atexit.register(cleanup_cache) 

    def job(self):
        print('hello job')


    def start_command(self, message):
        self.bot.reply_to(message, "Hello! I'm News Bot!") 
        self.job()

        schedule.every(my_params.interval_shedjule_step).seconds.do(self.job) 
        while True:
            schedule.run_pending()
            time.sleep(5)

    def start_bot(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            # print('start comand')
            self.start_command(message)
        
        self.bot.infinity_polling()

def main_tg_func():    
    tg_api = Tg()
    tg_api.start_bot()
