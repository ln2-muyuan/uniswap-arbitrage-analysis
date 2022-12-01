import json
import time

pairs = json.load(open('../src/files/pairs_full.json'))

tokenIn = {"address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "symbol": "WETH", "decimal": 18}
tokenOut = {"address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "symbol": "USDC", "decimal": 6}
allPath = []
firstPath = []


def findArb(all_pairs, length, tokenIn, tokenOut, path):
    new_path = path.copy()
    for i in range(len(all_pairs)):
        pair = all_pairs[i]
        if not pair['token0']['address'] == tokenIn['address'] and not pair['token1']['address'] == tokenIn['address']:
            continue
        if pair['reserve0'] / pow(10, pair['token0']['decimal']) < 1 or pair['reserve1'] / pow(10, pair['token1'][
            'decimal']) < 1:
            continue
        if tokenIn['address'] == pair['token0']['address']:
            temp_out = pair['token1']
        else:
            temp_out = pair['token0']
        pool = [pair['index'], tokenIn, temp_out]
        new_path.append(pool)
        global allPath
        if temp_out['address'] == tokenOut['address']:
            # only the complete path can be added to allPath
            allPath.append(new_path)
            return
        elif length > 1:
            pairs_excluding_this_pair = all_pairs[:i] + all_pairs[i + 1:]
            findArb(pairs_excluding_this_pair, length - 1, temp_out, tokenOut, new_path)
            # remain the new_path to the original state
            new_path = new_path[:-1]



def main():
    start_time = time.time()
    findArb(pairs, 5, tokenIn, tokenIn, firstPath)
    # print("\n".join(map(str, allPath)))
    end_time = time.time()
    print("Finding cost time: " + str(end_time - start_time) + "s")
    print("Total path number: " + str(len(allPath)))


main()
