import json
import requests
from config import exchanges

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(base: str, sym: str, amount: str):
        if base == sym:
            raise APIException(f"Невозможно конвертировать одинаковые валюты {base}.")

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}.")

        try:
            amount = float(amount)
        except:
            raise APIException(f"Не удалось обработать количество {amount}.")

        r = requests.get(f"https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={base_ticker}")
        total_base = json.loads(r.content)[exchanges[base]]

        return total_base