import json
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
from web3.providers.rpc import HTTPProvider

'''
If you use one of the suggested infrastructure providers, the url will be of the form
now_url  = f"https://eth.nownodes.io/{now_token}"
alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
infura_url = f"https://mainnet.infura.io/v3/{infura_token}"
'''

def connect_to_eth():
    url = "https://mainnet.infura.io/v3/8054c6b6305148d7be6d257adef7a4e6"  # FILL THIS IN
    w3 = Web3(HTTPProvider(url))
    assert w3.is_connected(), f"Failed to connect to provider at {url}"
    return w3

def connect_with_middleware(contract_json):
    with open(contract_json, "r") as f:
        d = json.load(f)
        d = d['bsc']
        address = d['address']
        abi = d['abi']

    # Connect to Binance Smart Chain (BSC) testnet
    url = "https://data-seed-prebsc-1-s1.binance.org:8545"  # HTTP URL
    w3 = Web3(HTTPProvider(url))
    assert w3.is_connected(), f"Failed to connect to provider at {url}"

    # Inject POA middleware for BSC chains
    w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

    # Create contract object
    contract = w3.eth.contract(address=Web3.to_checksum_address(address), abi=abi)

    return w3, contract

if __name__ == "__main__":
    connect_to_eth()
