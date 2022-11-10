def bank_to_coin_to_bank(P2P, MARKET, Config):
    scheme_dict = dict()

    for start_symbol in list(P2P.values())[0][Config.PRICE_FROM].keys():
        scheme_dict[start_symbol] = dict()
        for bank, symbols in P2P.items():
            for to_bank in P2P.keys():
                scheme_dict[start_symbol][f'{bank}To{to_bank}'] = dict()
                for end_symbol in symbols[0].keys():
                    if end_symbol == start_symbol:
                        continue
                    else:
                        bank_to_coin = P2P[bank][Config.PRICE_FROM][start_symbol]
                        coin_to_bank = P2P[to_bank][Config.PRICE_FROM][end_symbol]

                        if start_symbol == 'SHIB' and (end_symbol == 'USDT' or end_symbol == 'BUSD'):
                            status = Config.BALANCE / bank_to_coin * MARKET[start_symbol][end_symbol] \
                                     * coin_to_bank - Config.BALANCE

                        elif start_symbol == 'SHIB':
                            status = Config.BALANCE / bank_to_coin * MARKET[start_symbol]['USDT'] \
                                     * MARKET['USDT'][end_symbol] * coin_to_bank - Config.BALANCE

                        elif end_symbol == 'SHIB' and start_symbol != 'USDT' and start_symbol != 'BUSD':
                            status = Config.BALANCE / bank_to_coin * MARKET[start_symbol]['USDT'] * MARKET['USDT'][
                                end_symbol] \
                                     * coin_to_bank - Config.BALANCE
                        else:
                            status = Config.BALANCE / bank_to_coin * MARKET[start_symbol][end_symbol]\
                                     * coin_to_bank - Config.BALANCE

                    status = status if Config.MODE == 'RUB' else status / Config.BALANCE * 100
                    scheme_dict[start_symbol][f'{bank}To{to_bank}'][end_symbol] = status
    return scheme_dict
