import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def converter(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать колличестов {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]
        return round(total_base*amount)

        return total_base


#https://www.oanda.com/currency-converter/ru/?from=USD&to=RUB&amount=1
#https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}