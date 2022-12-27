import time
from thread import *
from rpc import *
from dfs import *


def updated_pairs(pairs_to_be_updated):
    if len(pairs_to_be_updated) < 200:
        get_reserves(pairs_to_be_updated)
    else:
        threads = []
        all_updated_pairs = []
        length = 200
        finished_count = 0
        while finished_count < len(pairs_to_be_updated):
            if finished_count + length > len(pairs_to_be_updated):
                length = len(pairs_to_be_updated) - finished_count
            threads.append(MyThread(get_reserves, (pairs_to_be_updated[finished_count:finished_count + length],)))
            finished_count += length
        for t in threads:
            t.start()
        for t in threads:
            t.join()
            if t.get_result() is not None:
                all_updated_pairs.extend(t.get_result())


def main():
    if infura_url is None:
        print("Please set infura_url in rpc.py")
        return
    start_time = time.time()
    # change the dataset here
    pairs = json.load(open('files/pairs_test3.json'))
    updated_pairs(pairs)
    end_time = time.time()
    print("Updating cost time: " + str(end_time - start_time) + "s")
    # enter the target token
    token_in = {"address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "symbol": "WETH", "decimal": 18}
    start_time = time.time()
    all_path = findArb(pairs, 6, token_in, token_in)
    end_time = time.time()
    print("Finding cost time: " + str(end_time - start_time) + "s")
    print("Total path number: " + str(len(all_path)))
    amount, path = get_optimal_amount(all_path)
    print("Optimal input amount: " + str(amount))
    print("Optimal arbitrage path: " + "\n".join(map(str, path)))


if __name__ == '__main__':
    main()
