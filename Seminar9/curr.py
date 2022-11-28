from datetime import datetime
import telebot
from pycbrf import ExchangeRates

bot = telebot.TeleBot('5555105258:AAFuWlivsW9lW0Yy0cqgoP25x1lMGAPFPTE')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = telebot.types.KeyboardButton ('USD')
    itembtn2 = telebot.types.KeyboardButton ('EUR')
    itembtn3 = telebot.types.KeyboardButton ('CNY')
    itembtn4 = telebot.types.KeyboardButton ('GBP')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(chat_id=message.chat.id, text='<b>Привет! Нажмите или введите валюту, чтобы увидеть обменные курсы</b>', reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur', 'cny', 'gbp']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text = f'<b>Сегодня курс {message_norm.upper()} составляет {float(rates[message_norm.upper()].rate)}RUR</b>', parse_mode = 'html')

bot.polling(non_stop=True)