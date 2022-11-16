import json
from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/4b0c1a572d1b417990c995ae82480859"
web3 = Web3(Web3.HTTPProvider(infura_url))


token0_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
token1_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

uniswap_v2_factory_address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
uniswap_v2_factory_abi = json.load(open('../src/abi/UniswapV2Factory'))
factory_contract = web3.eth.contract(address=uniswap_v2_factory_address, abi=uniswap_v2_factory_abi)
# allPairsLength = factory_contract.functions.allPairsLength().call()
# print(allPairsLength)


pair = factory_contract.functions.getPair(token0_address, token1_address).call()
print(pair)


