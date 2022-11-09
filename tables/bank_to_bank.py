def table_bank_to_bank(_bank_to_bank, BANKS, PRICE_FROM):
    table_price = list()
    table_price.append([f'Покупаем по цене 1,\n продаем по цене 2',
                        'USDT', 'BTC', 'BUSD', 'BNB', 'ETH', 'RUB', 'SHIB'])
    type_amount = {'AnyPriceToAny': 'любой суммы', 'AnyPriceToFixed': PRICE_FROM}
    for bank, price_from in _bank_to_bank.items():
        for amount, price in price_from.items():
            _bank = bank.split('To')
            table_price.append([f'С {BANKS[_bank[0]]} от любой суммы\n на {BANKS[_bank[1]]} от {type_amount[amount]}',
                                price['USDT'], price['BTC'], price['BUSD'], price['BNB'],
                                price['ETH'], price['RUB'], price['SHIB']])
    return len(table_price), table_price
