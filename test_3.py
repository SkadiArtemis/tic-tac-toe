import requests
import json
base = 'USD'
res = 'EUR'
r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={res}")
total_base = json.loads(r.content) # преобразовываем полученные данные в словарь
print(total_base) # смотрим как выглядит словарь и какие ключи
print(total_base[res]) # применяем ключ