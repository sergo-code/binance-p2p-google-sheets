def table_p2p(p2p_price, BANKS):
    table_price = list()
    table_price.append([f'RUB Курсы P2P', 'USDT', 'BTC', 'BUSD', 'BNB', 'ETH', 'RUB', 'SHIB'])
    for bank, price_list in p2p_price.items():
        for amount, price in price_list.items():
            table_price.append([f'Покупка {BANKS[bank]} от {amount}', price['USDT'], price['BTC'], price['BUSD'],
                                 price['BNB'], price['ETH'], price['RUB'], price['SHIB']])
    return len(table_price), table_price
