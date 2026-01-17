# BankServers

Types:

```python
from novabank_server.types import BankServer, BankServerListResponse
```

Methods:

- <code title="post /api/bank-servers">client.bank_servers.<a href="./src/novabank_server/resources/bank_servers.py">create</a>(\*\*<a href="src/novabank_server/types/bank_server_create_params.py">params</a>) -> <a href="./src/novabank_server/types/bank_server.py">BankServer</a></code>
- <code title="get /api/bank-servers/{server_id}">client.bank_servers.<a href="./src/novabank_server/resources/bank_servers.py">retrieve</a>(server_id) -> <a href="./src/novabank_server/types/bank_server.py">BankServer</a></code>
- <code title="put /api/bank-servers/{server_id}">client.bank_servers.<a href="./src/novabank_server/resources/bank_servers.py">update</a>(server_id, \*\*<a href="src/novabank_server/types/bank_server_update_params.py">params</a>) -> <a href="./src/novabank_server/types/bank_server.py">BankServer</a></code>
- <code title="get /api/bank-servers">client.bank_servers.<a href="./src/novabank_server/resources/bank_servers.py">list</a>() -> <a href="./src/novabank_server/types/bank_server_list_response.py">BankServerListResponse</a></code>
- <code title="delete /api/bank-servers/{server_id}">client.bank_servers.<a href="./src/novabank_server/resources/bank_servers.py">delete</a>(server_id) -> None</code>

# BankAccounts

Types:

```python
from novabank_server.types import BankAccount, BankAccountCreate, BankAccountListResponse
```

Methods:

- <code title="post /api/bank-accounts">client.bank_accounts.<a href="./src/novabank_server/resources/bank_accounts.py">create</a>(\*\*<a href="src/novabank_server/types/bank_account_create_params.py">params</a>) -> <a href="./src/novabank_server/types/bank_account.py">BankAccount</a></code>
- <code title="get /api/bank-accounts/{account_id}">client.bank_accounts.<a href="./src/novabank_server/resources/bank_accounts.py">retrieve</a>(account_id) -> <a href="./src/novabank_server/types/bank_account.py">BankAccount</a></code>
- <code title="put /api/bank-accounts/{account_id}">client.bank_accounts.<a href="./src/novabank_server/resources/bank_accounts.py">update</a>(account_id, \*\*<a href="src/novabank_server/types/bank_account_update_params.py">params</a>) -> <a href="./src/novabank_server/types/bank_account.py">BankAccount</a></code>
- <code title="get /api/bank-accounts">client.bank_accounts.<a href="./src/novabank_server/resources/bank_accounts.py">list</a>() -> <a href="./src/novabank_server/types/bank_account_list_response.py">BankAccountListResponse</a></code>
- <code title="delete /api/bank-accounts/{account_id}">client.bank_accounts.<a href="./src/novabank_server/resources/bank_accounts.py">delete</a>(account_id) -> None</code>

# Transactions

Types:

```python
from novabank_server.types import Transaction, TransactionListResponse
```

Methods:

- <code title="post /api/transactions">client.transactions.<a href="./src/novabank_server/resources/transactions.py">create</a>(\*\*<a href="src/novabank_server/types/transaction_create_params.py">params</a>) -> object</code>
- <code title="get /api/transactions/{transaction_id}">client.transactions.<a href="./src/novabank_server/resources/transactions.py">retrieve</a>(transaction_id) -> <a href="./src/novabank_server/types/transaction.py">Transaction</a></code>
- <code title="get /api/transactions">client.transactions.<a href="./src/novabank_server/resources/transactions.py">list</a>() -> <a href="./src/novabank_server/types/transaction_list_response.py">TransactionListResponse</a></code>
- <code title="delete /api/transactions/{transaction_id}">client.transactions.<a href="./src/novabank_server/resources/transactions.py">delete</a>(transaction_id) -> None</code>
- <code title="put /api/transactions/{transaction_id}/status">client.transactions.<a href="./src/novabank_server/resources/transactions.py">update_status</a>(transaction_id, \*\*<a href="src/novabank_server/types/transaction_update_status_params.py">params</a>) -> <a href="./src/novabank_server/types/transaction.py">Transaction</a></code>
