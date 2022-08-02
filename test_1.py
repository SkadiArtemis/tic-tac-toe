@bot.message_handler(content_types=['text', ])
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) !=3:
            raise APIException("Неверное количество параметров!")

        base, sym, amount = values
        total_base = Convertor.convert(base, sym, amount)

    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя!\n{e}")

    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду: \n{e}")
    else:
        text = f"Ценa {amount} {base} в {sym} - {total_base}"







bot.polling()




@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException("Неверное количество параметров!")

        base, sym, amount = values
        total_base = CurrencyConvertor.get_price(base, sym, amount)

    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя!\n{e}")

    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду: \n{e}")
    else:
        text = f"Ценa {amount} {base} в {sym} - {total_base}"

