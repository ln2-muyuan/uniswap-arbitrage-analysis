import json

tokenIn = {"address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "symbol": "WETH", "decimal": 18}
tokenOut = {"address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "symbol": "USDC", "decimal": 6}
allPath = [tokenIn]
pairs = json.load(open('../src/files/pairs_full.json'))


# def get_selected_pairs(all_pairs, token):
#     all_pools = []
#     for pair in all_pairs:
#         if pair['token0']['address'] == token['address'] or pair['token1']['address'] == token['address']:
#             all_pools.append(pair)
#     return all_pools


# print(get_selected_pairs(pairs, tokenOut))

# def findArb(path, length):
#     newpath = path.copy()
#     print("hello")
#     if length == 0:
#         print(newpath)
#         return
#     else:
#         findArb(newpath, length - 1)
#
#
# findArb(allPath, 4)
