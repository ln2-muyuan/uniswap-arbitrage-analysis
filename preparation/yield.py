import json
from web3 import Web3
from web3._utils.request import make_post_request

infura_url = "https://mainnet.infura.io/v3/4b0c1a572d1b417990c995ae82480859"
web3 = Web3(Web3.HTTPProvider(infura_url))
pairs = json.load(open('../src/files/pairs_test.json'))
uniswap_v2_pair_abi = json.load(open('../src/abi/UniswapV2Pair'))


def generate_json_rpc(params):
    return {
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": params,
        "id": 1
    }


def generate_get_reserves_json_rpc(pairs):
    contract = web3.eth.contract(abi=uniswap_v2_pair_abi)
    for pair in pairs:
        yield generate_json_rpc([{
            "to": pair['address'],
            "data": contract.encodeABI(fn_name="getReserves", args=[])
        }, "latest"])


class BatchHTTPProvider(Web3.HTTPProvider):
    def make_batch_request(self, text):
        # this line is different
        request_data = text.encode('utf-8')
        self.logger.debug("Making request HTTP. URI: %s, Request: %s", self.endpoint_uri, request_data)
        raw_response = make_post_request(self.endpoint_uri, request_data, **self.get_request_kwargs())
        response = self.decodce_rpc_response(raw_response)
        self.logger.debug("Got response HTTP. URI: %s, Response: %s", self.endpoint_uri, response)
        return response


batch_provider = BatchHTTPProvider(infura_url)
# print(batch_provider.make_batch_request(next(generate_get_reserves_json_rpc(pairs))))


def main():
    # for i in generate_get_reserves_json_rpc(pairs):
    #     print(i)

    # print(list(generate_get_reserves_json_rpc(pairs)))
    print(next(generate_get_reserves_json_rpc(pairs)))


if __name__ == "__main__":
    main()
