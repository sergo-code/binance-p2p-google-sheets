def table_bank_to_coin_to_bank(coin, _bank_to_coin_to_bank, BANKS, coins):
    table_price = list()

    coins.remove(coin)
    if coin == 'SHIB':
        for i, _coin in enumerate(coins):
            if _coin == 'BUSD' or _coin == 'USDT':
                coins[i] = f'{coin}->{_coin}'
            else:
                coins[i] = f'{coin}->USDT->{_coin}'
    elif coin != 'USDT' and coin != 'BUSD':
        coins[-1] = f'USDT->{coins[-1]}'
        coins = list(map(lambda to_coin: f'{coin}->{to_coin}', coins))
    else:
        coins = list(map(lambda to_coin: f'{coin}->{to_coin}', coins))
    coins.insert(0, coin)
    table_price.append(coins)

    for bank, list_price in _bank_to_coin_to_bank.items():
        _bank = bank.split('To')
        if coin == 'BTC':
            table_price.append([f'С {BANKS[_bank[0]]} на {BANKS[_bank[1]]}',
                                list_price['USDT'], list_price['BUSD'], list_price['BNB'],
                                list_price['ETH'], list_price['RUB'], list_price['SHIB']])
        elif coin == 'USDT':
            table_price.append([f'С {BANKS[_bank[0]]} на {BANKS[_bank[1]]}',
                                list_price['BTC'], list_price['BUSD'], list_price['BNB'],
                                list_price['ETH'], list_price['RUB'], list_price['SHIB']])
        elif coin == 'BUSD':
            table_price.append([f'С {BANKS[_bank[0]]} на {BANKS[_bank[1]]}',
                                list_price['USDT'], list_price['BTC'], list_price['BNB'],
                                list_price['ETH'], list_price['RUB'], list_price['SHIB']])
        elif coin == 'RUB':
            table_price.append([f'С {BANKS[_bank[0]]} на {BANKS[_bank[1]]}',
                                list_price['USDT'], list_price['BTC'], list_price['BUSD'],
                                list_price['BNB'], list_price['ETH'], list_price['SHIB']])
        elif coin == 'ETH':
            table_price.append([f'С {BANKS[_bank[0]]} на {BANKS[_bank[1]]}',
                                list_price['USDT'], list_price['BTC'], list_price['BUSD'],
                                list_price['BNB'], list_price['RUB'], list_price['SHIB']])
        elif coin == 'BNB':
            table_price.append([f'С {BANKS[_bank[0]]} на {BANKS[_bank[1]]}',
                                list_price['USDT'], list_price['BTC'], list_price['BUSD'],
                                list_price['ETH'], list_price['RUB'], list_price['SHIB']])
        elif coin == 'SHIB':
            table_price.append([f'С {BANKS[_bank[0]]} на {BANKS[_bank[1]]}',
                                list_price['USDT'], list_price['BTC'], list_price['BUSD'],
                                list_price['BNB'], list_price['ETH'], list_price['RUB']])
    return len(table_price), table_price
