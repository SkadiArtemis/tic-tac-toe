import requests
import json
from config import exchanges

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: int):
        if base == quote:
            raise APIException(f"Невозможно конвертировать одинаковые валюты {base}.")

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}.")

        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}.")

        try:
            amount = float(amount)
        except:
            raise APIException(f"Не удалось обработать количество {amount}.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}")
        total_base = json.loads(r.content)[exchanges[quote]]*float(amount)


        return total_base



