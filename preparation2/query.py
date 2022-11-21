import requests


def run_query(query):
    request = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2', json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))


query = """
    {
        pairs(first: 10) {
            id
            token0 {
                id
                symbol
                decimals
            }
            token1 {
                id
                symbol
                decimals
            }
            reserve0
            reserve1
        }    
    }
"""

result = run_query(query)
print(result)

