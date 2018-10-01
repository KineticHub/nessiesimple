import apiUtil
api = apiUtil.ApiUtil()

# ATMs
atm_request = api.get_endpoint("/atms?lat=38.9283&lng=-77.1753&rad=1")
print(atm_request.get("data")[0])

while api.has_next_page(atm_request):
    atm_request = api.get_next_page(atm_request)
    print(atm_request.get("data"))

# Customers
payload = {
    "first_name": "test",
    "last_name": "mylittlecustomer",
    "address": {
        "street_number": "123",
        "street_name": "Sesame St",
        "city": "Rainbow",
        "state": "VA",
        "zip": "54321"
    }
}
customer_create_request = api.post_endpoint("/customers?", payload)
print(customer_create_request)

# Accounts
customer_id = customer_create_request.get("objectCreated").get("_id")
payload = {
  "type": "Credit Card",
  "nickname": "cool account",
  "rewards": 0,
  "balance": 0,
  "account_number": "1234567891011234"
}
accounts_create_request = api.post_endpoint("/customers/" + customer_id + "/accounts?", payload)
print(accounts_create_request)
accounts_request = api.get_endpoint("/accounts?")
account_id = accounts_request[0].get("_id")
print(accounts_request)

# Bills
payload = {
    "status": "pending",
    "payee": "puff the magic dragon",
    "nickname": "nessie",
    "payment_date": "2018-09-12",
    "payment_amount": 10,  # this was missing in example api
    "recurring_date": 1
}
bill_create_request = api.post_endpoint("/accounts/" + account_id + "/bills?", payload)
print(bill_create_request)

# Purchases
purchases_request = api.get_endpoint("/accounts/" + account_id + "/purchases?")
print(purchases_request)

# Deposits
payload = {
    "medium": "balance",
    "transaction_date": "2018-09-12",
    "status": "pending",
    "description": "ramen noodles",
    "amount": 10  # not documented
}
deposit_create_request = api.post_endpoint("/accounts/" + account_id + "/deposits?", payload)
print(deposit_create_request)

# Enterprise
enterprise_accounts_request = api.get_endpoint("/enterprise/accounts?")
print(enterprise_accounts_request.get("results")[0])

# Delete
data_delete_request = api.delete_endpoint("/data?type=Accounts")
