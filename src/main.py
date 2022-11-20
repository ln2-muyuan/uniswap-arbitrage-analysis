import json
import time

from eth_abi import decode_abi
from web3 import Web3
from web3._utils.request import make_post_request

from thread import *

infura_url = "https://mainnet.infura.io/v3/4b0c1a572d1b417990c995ae82480859"
web3 = Web3(Web3.HTTPProvider(infura_url))
pairs = json.load(open('../src/files/pairs_test_2.json'))
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
        response = self.decode_rpc_response(raw_response)
        self.logger.debug("Got response HTTP. URI: %s, Response: %s", self.endpoint_uri, response)
        return response


def get_reserves(pairs):
    batch_provider = BatchHTTPProvider(infura_url)
    r = list(batch_provider.make_batch_request(json.dumps(list(generate_get_reserves_json_rpc(pairs)))))
    for i in range(len(pairs)):
        result = decode_abi(['uint112', 'uint112', 'uint32'], bytes.fromhex(r[i]['result'][2:]))
        pairs[i]['reserve0'] = result[0]
        pairs[i]['reserve1'] = result[1]
    return pairs





def main():
    start_time = time.time()
    if len(pairs) < 200:
        updated_pairs = get_reserves(pairs)
    else:
        threads = []
        updated_pairs = []
        length = 200
        finished_count = 0
        while finished_count < len(pairs):
            if finished_count + length > len(pairs):
                length = len(pairs) - finished_count
            threads.append(MyThread(get_reserves, (pairs[finished_count:finished_count + length],)))
            finished_count += length
        for t in threads:
            t.start()
        for t in threads:
            t.join()
            updated_pairs += t.get_result()
    end_time = time.time()
    print("Updating cost time: " + str(end_time - start_time) + "s")
    # for pair in updated_pairs:
    #     print(pair)


if __name__ == "__main__":
    main()
