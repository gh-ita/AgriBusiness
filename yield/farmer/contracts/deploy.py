from solcx import compile_standard, install_solc
import json 
from web3 import Web3

with open("C:/Users/ghita/OneDrive/Bureau/Yield/yield/farmer/contracts/SimpleStorage.sol", "r") as file :
    simple_storage_file = file.read()
#Compile Solidity
#install_solc("0.8.0")


compiled_sol = compile_standard(
    {
    "language": "Solidity",
    "sources": {"SimpleStorage.sol":{"content": simple_storage_file}},
    "settings":{
        "outputSelection" :{
            '*':{
                "*": ["abi","metadata","evm.bytecode","evm.sourceMap"]
            }
        }
    }
    },
    solc_version ="0.8.0"

)
with open("compiled_code.json","w") as file :
    json.dump(compiled_sol, file)

#get bytecode 
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["Yield"]["evm"]["bytecode"]["object"]

#get abi

abi = compiled_sol["contracts"]["SimpleStorage.sol"]["Yield"]["abi"]

#Connecting to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xB8C92A007846Ee8E4B562bA2aDCfddC96B908305"
private_key = "0x7f138354321f61330e01b6d2f3d0f40308389098e1ce653c6fd29fb610d37ae4"

#create contract 
SimpleStorage = w3.eth.contract(abi = abi, bytecode = bytecode) 
#Get the latest transaction 
nonce = w3.eth.get_transaction_count(my_address)

transaction = SimpleStorage.constructor().build_transaction({"chainId": chain_id,"from": my_address,"nonce":nonce})
signed_txn = w3.eth.account.sign_transaction(transaction,private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

