import json
import time

from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/4b0c1a572d1b417990c995ae82480859"
web3 = Web3(Web3.HTTPProvider(infura_url))
uniswap_v2_pair_address = "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"
uniswap_v2_pair_abi = json.load(open('../src/abi/UniswapV2Pair'))
# You only instantiate the contract once
uniswap_v2_pair_contract = web3.eth.contract(address=uniswap_v2_pair_address, abi=uniswap_v2_pair_abi)



all_pairs = json.load(open('../src/files/pairs_test.json'))
updated_pairs = []
start_time = time.time()
for pair in all_pairs:
    dict = { }
    dict['index'] = pair['index']
    dict['address'] = pair['address']
    dict['token0'] = pair['token0']
    dict['token1'] = pair['token1']
    dict['reserve0'] = uniswap_v2_pair_contract.functions.getReserves().call()[0]
    dict['reserve1'] = uniswap_v2_pair_contract.functions.getReserves().call()[1]
    updated_pairs.append(dict)

end_time = time.time()
print("Update cost: ", end_time - start_time, "s")
with open('../src/files/pairs_test.json', 'w') as outfile:
    json.dump(updated_pairs, outfile)

# print(updated_pairs)