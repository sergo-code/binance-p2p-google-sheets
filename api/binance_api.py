import json
import requests


class BinanceAPI:
    def __init__(self):
        self.banks = self.get_banks()
        self.symbols = self.get_coins()
        self.bundle = self.get_bundle()

    def get_bundle(self):
        with open('data/bundle.txt') as file:
            return [line.rstrip() for line in file]

    def get_coins(self):
        with open('data/coins.txt') as file:
            return [line.rstrip() for line in file]

    def get_banks(self):
        with open('data/banks.json') as file:
            return list(json.load(file).keys())

    def get_p2p_price(self, PRICE_FROM):
        trans = [PRICE_FROM, 0]

        url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
        headers = {
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36',
        }
        symbols_dict = dict()

        for bank in self.banks:
            symbols_dict[bank] = dict()
            for amount in trans:
                symbols_dict[bank][amount] = dict()
                for symbol in self.symbols:
                    data = {
                        "page": 1,
                        "rows": 1,
                        "payTypes": [bank],
                        "asset": f"{symbol}",
                        "tradeType": "BUY",
                        "fiat": "RUB",
                        "merchantCheck": 'false',
                        "transAmount": f"{amount}"
                    }
                    response = requests.post(url=url, headers=headers, data=str(data))

                    value = float(response.json()['data'][0]['adv']['price'])
                    symbols_dict[bank][amount][symbol] = value

        return symbols_dict

    def get_market_price(self):
        params = str(self.bundle).replace(' ', '')
        url = 'https://api.binance.com/api/v3/ticker/price?symbols={}'.format(params.replace('\'', '\"'))
        return requests.get(url=url).json()


if __name__ == '__main__':
    print(get_market_price())
