from decimal import Decimal
_d997 = Decimal(997)
_d1000 = Decimal(1000)


def findArb(all_pairs, length, token_in, token_out):
    allPath = []
    firstPath = []

    def find_Arb(_all_pairs, _length, _token_in, _token_out, _path):
        new_path = _path.copy()
        for i in range(len(_all_pairs)):
            pair = _all_pairs[i]
            if not pair['token0']['address'] == _token_in['address'] and not pair['token1']['address'] == _token_in[
                'address']:
                continue
            if pair['reserve0'] / pow(10, pair['token0']['decimal']) < 1 or pair['reserve1'] / pow(10, pair['token1'][
                'decimal']) < 1:
                continue
            if _token_in['address'] == pair['token0']['address']:
                temp_out = pair['token1']
            else:
                temp_out = pair['token0']
            pool = [pair['index'], _token_in, temp_out, pair['reserve0'], pair['reserve1']]
            new_path.append(pool)
            if temp_out['address'] == _token_out['address']:
                # only the complete path can be added to allPath
                allPath.append(new_path)
                return
            elif _length > 1:
                pairs_excluding_this_pair = _all_pairs[:i] + _all_pairs[i + 1:]
                find_Arb(pairs_excluding_this_pair, _length - 1, temp_out, _token_out, new_path)
                # remain the new_path to the original state
                new_path = new_path[:-1]

    find_Arb(all_pairs, length, token_in, token_out, firstPath)
    return allPath


def get_optimal_amount(all_paths):
    optimal_path = []
    optimal_amount = 0
    for path in all_paths:
        Ea, Eb = get_EaEb(path)
        if Ea and Eb and Eb * _d997 > Ea * _d1000:
            amount = Decimal(int((Decimal.sqrt(Ea * Eb * _d997 * _d1000) - Ea * _d1000) / _d997))
            # print(type(amount))
            if amount > optimal_amount:
                optimal_amount = amount
                optimal_path = path
    return optimal_amount, optimal_path


# Path sample: [0, {'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 'symbol': 'WETH', 'decimal': 18},
# {'address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 'symbol': 'USDC', 'decimal': 6}, 176560092727090,
# 524595304157729979983018] [5, {'address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 'symbol': 'USDC',
# 'decimal': 6}, {'address': '0x6B175474E89094C44Da98b954EedeAC495271d0F', 'symbol': 'DAI', 'decimal': 18},
# 1916219085245778868760905, 1929099476762] [3, {'address': '0x6B175474E89094C44Da98b954EedeAC495271d0F',
# 'symbol': 'DAI', 'decimal': 18}, {'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 'symbol': 'WETH',
# 'decimal': 18}, 147756526248031590428050982, 441991822316332502643139]


def to_int(n):
    return Decimal(int(n))


def get_EaEb(path):
    Ra = Rb = Ea = Eb = 0
    idx = 0
    for pool in path:
        if idx == 0:
            Ra = pool[3]
            Rb = pool[4]
        if idx == 1:
            Rb1 = pool[3]
            Rc = pool[4]
            Ea = to_int(_d1000 * Ra * Rb1 / (_d1000 * Rb1 + _d997 * Rb))
            Eb = to_int(_d997 * Rb * Rc / (_d1000 * Rb1 + _d997 * Rb))
        if idx > 1:
            Ra = Ea
            Rb = Eb
            Rb1 = pool[3]
            Rc = pool[4]
            Ea = to_int(_d1000 * Ra * Rb1 / (_d1000 * Rb1 + _d997 * Rb))
            Eb = to_int(_d997 * Rb * Rc / (_d1000 * Rb1 + _d997 * Rb))
        idx += 1
    return Ea, Eb
