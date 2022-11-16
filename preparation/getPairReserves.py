import json

from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/4b0c1a572d1b417990c995ae82480859"
web3 = Web3(Web3.HTTPProvider(infura_url))

uniswap_v2_pair_address = "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"
uniswap_v2_pair_abi = json.load(open('../src/abi/UniswapV2Pair'))
# token0_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
# token1_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

uniswap_v2_pair_contract = web3.eth.contract(address=uniswap_v2_pair_address, abi=uniswap_v2_pair_abi)
reserves = uniswap_v2_pair_contract.functions.getReserves().call()
# token0_address = uniswap_v2_pair_contract.functions.token0().call()
# token1_address = uniswap_v2_pair_contract.functions.token1().call()
print(reserves)
# print(token0_address)
# print(token1_address)

