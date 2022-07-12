import telebot
from extensions1 import APIException, CurrencyConverter
from config import TOKEN, exchanges
import traceback


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Приветствую!\
    Чтобы начать работу введите коменду боту в следующем формате: \n<имя валюты>\
     <имя валюты, в которую хотете перевести> \
     <количество переводимой валюты>\nУвидеть список переводимых валют: /values"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for i in exchanges.keys():
        text = '\n' .join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Неверное количество параметров!')

        base, quote, amount = values
        total_base = CurrencyConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        text = f"Ценa {amount} {base} в {quote} - {total_base}"
        bot.send_message(message.chat.id, text)


bot.polling()
