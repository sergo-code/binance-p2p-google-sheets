import os
import time
import json
from dotenv import load_dotenv

from api import GoogleSheetsAPI, BinanceAPI
from models import json_market, bank_to_bank, bank_to_coin_to_bank
from utils import startup_table, grouping_data


BALANCE = 100000
PRICE_FROM = 1000

with open('data/banks.json', encoding='utf8') as file:
    BANKS = json.load(file)


def main(binance, sheets):
    global BALANCE, PRICE_FROM
    while True:
        time_start = time.time()

        temp_price = sheets.reader_sheets('D1:D1')
        if temp_price:
            PRICE_FROM = temp_price

        temp_balance = sheets.reader_sheets('F1:F1')
        if temp_balance:
            BALANCE = temp_balance

        data = dict()
        market = binance.get_market_price()

        data['p2pPrice'] = binance.get_p2p_price(PRICE_FROM)
        data['marketPrice'] = json_market(market)
        data['bankToBank'] = bank_to_bank(data['p2pPrice'], PRICE_FROM, BALANCE)
        data['bankToCoinToBank'] = bank_to_coin_to_bank(data['p2pPrice'], data['marketPrice'], PRICE_FROM, BALANCE)

        array = grouping_data(data, binance.symbols, BANKS, PRICE_FROM, BALANCE)

        sheets.writer_sheets(array)

        time.sleep(5*60 - (time.time() - time_start))


if __name__ == '__main__':
    load_dotenv()
    sheets_id = os.getenv('SHEET_ID')
    sheets = GoogleSheetsAPI(sheets_id)
    binance = BinanceAPI()
    # startup_table(api)
    main(binance, sheets)
