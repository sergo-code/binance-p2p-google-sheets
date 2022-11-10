def bank_to_bank(P2P, Config):
    p2p_dict = dict()

    for bank, symbols in P2P.items():
        for to_bank in P2P.keys():
            p2p_dict[f'{bank}To{to_bank}'] = dict()
            p2p_dict[f'{bank}To{to_bank}']['AnyPriceToFixed'] = dict()
            p2p_dict[f'{bank}To{to_bank}']['AnyPriceToAny'] = dict()
            for key, value in {'AnyPriceToFixed': Config.PRICE_FROM, 'AnyPriceToAny': 0}.items():
                if bank == to_bank and key == 'AnyPriceToAny':
                    del p2p_dict[f'{bank}To{to_bank}']['AnyPriceToAny']
                    continue
                else:
                    for symbol in symbols[0].keys():
                        status = Config.BALANCE / P2P[bank][0][symbol] * P2P[to_bank][value][symbol] - Config.BALANCE

                        status = status if Config.MODE == 'RUB' else status/Config.BALANCE * 100

                        p2p_dict[f'{bank}To{to_bank}'][key][symbol] = status
    return p2p_dict
