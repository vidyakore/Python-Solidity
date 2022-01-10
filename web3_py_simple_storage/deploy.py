from solcx import compile_standard,install_solc
import json
from web3 import Web3
install_solc('0.6.0')
# install_solc('v0.4.25')
with open("SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
# print(simple_storage_file)

# compiling solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

# print(compiled_sol)

with open("compiled_code.json","w+") as file:
    json.dump(compiled_sol, file)

#get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["first"]["evm"]["bytecode"]["object"]

#get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["first"]["abi"]
# print("abi",abi)

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xE499c7c9255dC167b1CbdE0CA1bdC739DA281613"
private_key = "8f5a74f82876f0922b36c3d734bb302f30e25eaca4d859192e92431b0ef64124"

#create the cotract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
#get the latest trasaction
nonce = w3.eth.getTransactionCount(my_address)
print("nonce = ",nonce)
#1. build a transaction
#2.sign a trasaction
#3. send a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id,"from":my_address,"nonce": nonce}
)

print("transaction",transaction)