import json

from eth_abi import decode_abi
from web3 import Web3
from web3._utils.request import make_post_request

_infura_url = "https://mainnet.infura.io/v3/4b0c1a572d1b417990c995ae82480859"
_web3 = Web3(Web3.HTTPProvider(_infura_url))
_uniswap_v2_pair_abi = json.load(open('../src/abi/UniswapV2Pair'))


def _generate_json_rpc(params):
    return {
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": params,
        "id": 1
    }


def _generate_get_reserves_json_rpc(pairs):
    contract = _web3.eth.contract(abi=_uniswap_v2_pair_abi)
    for pair in pairs:
        yield _generate_json_rpc([{
            "to": pair['address'],
            "data": contract.encodeABI(fn_name="getReserves", args=[])
        }, "latest"])


def get_reserves(pairs):
    batch_provider = BatchHTTPProvider(_infura_url)
    r = list(batch_provider.make_batch_request(json.dumps(list(_generate_get_reserves_json_rpc(pairs)))))

    for i in range(len(pairs)):
        result = decode_abi(['uint112', 'uint112', 'uint32'], bytes.fromhex(r[i]['result'][2:]))
        pairs[i]['reserve0'] = result[0]
        pairs[i]['reserve1'] = result[1]



class BatchHTTPProvider(Web3.HTTPProvider):
    def make_batch_request(self, text):
        # this line is different
        request_data = text.encode('utf-8')
        self.logger.debug("Making request HTTP. URI: %s, Request: %s", self.endpoint_uri, request_data)
        raw_response = make_post_request(self.endpoint_uri, request_data, **self.get_request_kwargs())
        response = self.decode_rpc_response(raw_response)
        self.logger.debug("Got response HTTP. URI: %s, Response: %s", self.endpoint_uri, response)
        return response
