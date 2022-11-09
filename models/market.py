def json_market(symbols_price):
    price_list = dict()

    for item in symbols_price:
        price_list[item['symbol']] = item['price']

    return {
        'USDT': {
            'USDT': 0, 'BTC': 1/float(price_list['BTCUSDT']), 'BUSD': 1/float(price_list['BUSDUSDT']),
            'BNB': 1/float(price_list['BNBUSDT']), 'ETH': 1/float(price_list['ETHUSDT']),
            'RUB': float(price_list['USDTRUB']), 'SHIB': 1/float(price_list['SHIBUSDT'])
        },
        'BTC': {
            'USDT': float(price_list['BTCUSDT']), 'BTC': 0, 'BUSD': float(price_list['BTCBUSD']),
            'BNB': 1/float(price_list['BNBBTC']), 'ETH': 1/float(price_list['ETHBTC']),
            'RUB': float(price_list['BTCRUB']), 'SHIB': 0
        },
        'BUSD': {
            'USDT': float(price_list['BUSDUSDT']), 'BTC': 1/float(price_list['BTCBUSD']), 'BUSD': 0,
            'BNB': 1/float(price_list['BNBBUSD']), 'ETH': 1/float(price_list['ETHBUSD']),
            'RUB': float(price_list['BUSDRUB']), 'SHIB': 1/float(price_list['SHIBBUSD'])
        },
        'BNB': {
            'USDT': float(price_list['BNBUSDT']), 'BTC': float(price_list['BNBBTC']),
            'BUSD': float(price_list['BNBBUSD']), 'BNB': 0, 'ETH': float(price_list['BNBETH']),
            'RUB': float(price_list['BNBRUB']), 'SHIB': 0
        },
        'ETH': {
            'USDT': float(price_list['ETHUSDT']), 'BTC': float(price_list['ETHBTC']),
            'BUSD': float(price_list['ETHBUSD']), 'BNB': 1/float(price_list['BNBETH']), 'ETH': 0,
            'RUB': float(price_list['ETHRUB']), 'SHIB': 0
        },
        'RUB': {
            'USDT': 1/float(price_list['USDTRUB']), 'BTC': 1/float(price_list['BTCRUB']),
            'BUSD': 1/float(price_list['BUSDRUB']), 'BNB': 1/float(price_list['BNBRUB']),
            'ETH': 1/float(price_list['ETHRUB']), 'RUB': 0, 'SHIB': 0
        },
        'SHIB': {
            'USDT': float(price_list['SHIBUSDT']), 'BTC': 0, 'BUSD': float(price_list['SHIBUSDT']),
            'BNB': 0, 'ETH': 0, 'RUB': 0,
            'SHIB': 0
        }
    }
