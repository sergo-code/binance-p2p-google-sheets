import os
import time
import json
from dotenv import load_dotenv

from api import GoogleSheetsAPI, BinanceAPI
from models import json_market, bank_to_bank, bank_to_coin_to_bank
from utils import startup_table, grouping_data


with open('data/banks.json', encoding='utf8') as file:
    BANKS = json.load(file)


class Config:
    BALANCE = 100000
    PRICE_FROM = 1000
    MODE = 'RUB'


def main(binance, sheets):
    try:
        os.environ['TZ'] = 'Europe/Moscow'
        time.tzset()
    except AttributeError:
        print('The time zone is not supported!')

    global BALANCE, PRICE_FROM, MODE
    while True:
        time_start = time.time()

        temp_price = sheets.reader_sheets('D1:D1', 'int')
        if temp_price:
            Config.PRICE_FROM = temp_price

        temp_balance = sheets.reader_sheets('F1:F1', 'int')
        if temp_balance:
            Config.BALANCE = temp_balance

        data = dict()
        market = binance.get_market_price()

        data['p2pPrice'] = binance.get_p2p_price(Config)
        data['marketPrice'] = json_market(market)

        temp_mode = sheets.reader_sheets('H1:H1', 'str')
        if temp_mode:
            Config.MODE = temp_mode

        data['bankToBank'] = bank_to_bank(data['p2pPrice'], Config)
        data['bankToCoinToBank'] = bank_to_coin_to_bank(data['p2pPrice'], data['marketPrice'], Config)

        array = grouping_data(data, binance.symbols, BANKS, Config)

        sheets.writer_sheets(array)

        time.sleep(5*60 - (time.time() - time_start))


if __name__ == '__main__':
    load_dotenv()
    sheets_id = os.getenv('SHEET_ID')
    sheets = GoogleSheetsAPI(sheets_id)
    binance = BinanceAPI()
    # startup_table(sheets)
    try:
        main(binance, sheets)
    except KeyboardInterrupt:
        print('exit...')
