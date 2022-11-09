def bank_to_coin_to_bank(P2P, MARKET, PRICE_FROM, BALANCE):
    scheme_dict = dict()

    for start_symbol in list(P2P.values())[0][PRICE_FROM].keys():
        scheme_dict[start_symbol] = dict()
        for bank, symbols in P2P.items():
            for to_bank in P2P.keys():
                scheme_dict[start_symbol][f'{bank}To{to_bank}'] = dict()
                for end_symbol in symbols[0].keys():
                    if end_symbol == start_symbol:
                        continue
                    elif start_symbol == 'SHIB' and (end_symbol == 'USDT' or end_symbol == 'BUSD'):
                        bank_to_coin = P2P[bank][PRICE_FROM][start_symbol]
                        coin_to_bank = P2P[to_bank][PRICE_FROM][end_symbol]

                        scheme_dict[start_symbol][f'{bank}To{to_bank}'][end_symbol] = \
                            BALANCE / bank_to_coin * MARKET[start_symbol][end_symbol] * coin_to_bank - BALANCE

                    elif start_symbol == 'SHIB':
                        bank_to_coin = P2P[bank][PRICE_FROM][start_symbol]
                        coin_to_bank = P2P[to_bank][PRICE_FROM][end_symbol]

                        scheme_dict[start_symbol][f'{bank}To{to_bank}'][end_symbol] = \
                            BALANCE / bank_to_coin * MARKET[start_symbol]['USDT'] * MARKET['USDT'][end_symbol] * coin_to_bank - BALANCE

                    elif end_symbol == 'SHIB' and start_symbol != 'USDT' and start_symbol != 'BUSD':
                        bank_to_coin = P2P[bank][PRICE_FROM][start_symbol]
                        coin_to_bank = P2P[to_bank][PRICE_FROM][end_symbol]

                        scheme_dict[start_symbol][f'{bank}To{to_bank}'][end_symbol] = \
                            BALANCE / bank_to_coin * MARKET[start_symbol]['USDT'] * MARKET['USDT'][end_symbol] * coin_to_bank - BALANCE

                    else:
                        bank_to_coin = P2P[bank][PRICE_FROM][start_symbol]
                        coin_to_bank = P2P[to_bank][PRICE_FROM][end_symbol]

                        scheme_dict[start_symbol][f'{bank}To{to_bank}'][end_symbol] = \
                            BALANCE / bank_to_coin * MARKET[start_symbol][end_symbol] * coin_to_bank - BALANCE
    return scheme_dict
