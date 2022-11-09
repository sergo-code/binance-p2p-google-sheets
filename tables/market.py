def table_market(market_price):
    table_price = list()
    table_price.append([f'Курсы крипты по маркету', 'USDT', 'BTC', 'BUSD', 'BNB', 'ETH', 'RUB', 'SHIB'])

    for symbol, price_list in market_price.items():
        table_price.append([symbol, price_list['USDT'], price_list['BTC'], price_list['BUSD'],
                            price_list['BNB'], price_list['ETH'], price_list['RUB'], price_list['SHIB']])
    return len(table_price), table_price
