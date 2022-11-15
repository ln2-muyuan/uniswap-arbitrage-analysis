import json

from web3 import Web3



infura_url = "https://mainnet.infura.io/v3/4b0c1a572d1b417990c995ae82480859"
web3 = Web3(Web3.HTTPProvider(infura_url))

pool_address = "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"
abi = json.load(open('../src/abi/UniswapV2Pair'))
token0_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
token1_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

print(abi)
contract = web3.eth.contract(address = pool_address, abi = abi)




