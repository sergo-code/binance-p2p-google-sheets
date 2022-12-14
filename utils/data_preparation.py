import time

from tables import table_p2p, table_market, table_bank_to_bank, table_bank_to_coin_to_bank


def grouping_data(data, symbols, BANKS, Config):
    list_scheme_bank_to_coin_to_bank = list()
    for coin, list_price in data['bankToCoinToBank'].items():
        list_scheme_bank_to_coin_to_bank.append(table_bank_to_coin_to_bank(coin, list_price, BANKS, symbols.copy()))

    schemes = [table_p2p(data['p2pPrice'], BANKS),
               table_market(data['marketPrice']),
               table_bank_to_bank(data['bankToBank'], BANKS, Config.PRICE_FROM)]
    schemes += list_scheme_bank_to_coin_to_bank

    time_update = time.localtime(time.time())

    array = [{'range': 'A1:H1',
              'majorDimension': 'ROWS',
              'values': [['Обновлено в:', f'{time_update.tm_hour}:{time_update.tm_min} по МСК',
                          'Цены от:', Config.PRICE_FROM,
                          'Баланс:', Config.BALANCE,
                          'Спред в:', Config.MODE]]
              }]

    temp_length = 3
    for scheme in schemes:
        _length, _data = scheme
        _length += temp_length - 1
        array.append({'range': f'A{temp_length}:H{_length}',
                      'majorDimension': 'ROWS',
                      'values': _data
                      })
        temp_length = _length + 3
    return array
