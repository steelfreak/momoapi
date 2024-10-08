# Explanation of the Python Code for MoMo Pay and MoMo Token

This code defines a class named `PayClass` that interacts with the MoMo Pay API for collections and disbursements (sending money). It utilizes the `requests` library to make HTTP requests and the `json` library to handle JSON data.

## Breakdown of the Code

### 1. Variables and Keys

- The code defines several variables like `collections_subkey` and `disbursements_subkey`, which are likely subscription keys obtained from the MoMo developer portal.
- It also sets variables for basic authorization keys, environment mode (sandbox or production), and the API base URL.

### 2. Generating Basic Authorization

- The code generates basic authorization keys for both collections and disbursements based on the environment mode.
- In sandbox mode, it automatically creates API users and keys using `uuid.uuid4()`.

### 3. Collections Code

- **`momotoken`**: This function gets a token for MoMo Collections API calls using the `collections_subkey` and basic authorization.

- **`momopay`**: This function initiates a MoMo Pay request. It takes arguments like amount, currency, reference text, phone number, and payer message.
  - It generates a unique reference ID.
  - It constructs the payload with transaction details.
  - It creates headers with the authorization token (obtained from `momotoken`), subscription key, reference ID, and environment indicator.
  - It sends a POST request to the MoMo Pay API and returns a dictionary containing the response status code and reference ID.

- **`verifymomo`**: This function verifies the status of a MoMo Pay transaction using the reference ID.
  - It constructs headers with the authorization token, subscription key, and environment indicator.
  - It sends a GET request to the MoMo Pay API and returns the JSON response.

- **`momobalance`**: This function retrieves the MoMo Collections account balance.
  - It constructs headers with the authorization token, subscription key, and environment indicator.
  - It sends a GET request to the MoMo Collections API and returns the JSON response.

### 4. Disbursements Code

This section is similar to the Collections code but focuses on sending money (disbursements). It defines functions for:

- Generating a disbursement token (`momotokendisbursement`)
- Checking disbursement balance (`momobalancedisbursement`)
- Withdrawing money (`withdrawmtnmomo`)
- Checking the status of a disbursement (`checkwithdrawstatus`)

### 5. Important Notes

- This code appears to be for demonstration purposes only. It does not handle error scenarios or detailed validation.
- You need to replace the placeholder values for subscription keys and other credentials with your actual MoMo developer account details.
- Using this code in production requires proper error handling and security measures.

Overall, this code provides a basic framework for interacting with the MoMo Pay API for collections and disbursements in Python. However, it should be adapted and secured before deployment in a real-world application.





Before You start Go through this below

```markdown
# Dependencies
Install the required package using pip:
```

```bash
pip install basicauth
```

## Requirements for Production Users
- MTN MOMO developer account: [Sign In](https://momodeveloper.mtn.com/signin?ReturnUrl=%2F)
- MTN MOMO developer collections and disbursement API user and key
- MTN MOMO developer subscription key for collections and subscriptions

## Requirements for Sandbox/Testing Users
- Collections and disbursement subscription keys

## What to Do Before You Start Using This
Open `pay.py` and update the following values:

1. Update `collections_subkey` with your collections subscription key:
   ```python
   # Collections Subscription Key:
   collections_subkey = "{{Collections_subscription_key}}"
   ```

2. Update `disbursement_subkey` with your disbursement subscription key:
   ```python
   # Disbursement Subscription Key:
   disbursement_subkey = ""
   ```

3. Only for users in production:
   - Update collections API user:
     ```python
     collections_apiuser = ""
     ```
   - Update API key with your collections key:
     ```python
     api_key_collections = ""
     ```

4. Set application environment. By default, the environment is sandbox:
   ```python
   # Application mode
   environment_mode = "sandbox"
   ```

## Calling Request to Pay
You can call the payment request using the following code:

```python
from pay import PayClass

callPay = PayClass.momopay(amount, currency, txt_ref, phone_number, payermessage)
print(callPay["response"])
```

To return the reference (UUID), print out this:

```python
print(callPay["ref"]) 
```

To return the status code, print out this:

```python
print(callPay["response"])
```

**Note:** If it returns 202 or 200, then it means the request was successful.

## Verify and Check the Transaction Status
To verify if the customer has confirmed the payment, use the following code:

```python
from pay import PayClass

# Verify the transaction
verify = PayClass.verifymomo("Reference returned by momopay function")
```

A status of 200 or 202 means okay. When the transaction is successful, it returns:

```json
{
  "amount": 100,
  "currency": "UGX",
  "financialTransactionId": 23503452,
  "externalId": 947354,
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": 4656473839.0
  },
  "status": "SUCCESSFUL"
}
```

For the complete reference of payment verification, read the documentation [here](https://momodeveloper.mtn.com/docs/services/collection/operations/requesttopay-referenceId-GET).

## Checking the Account Balance

### From the Collections Account
To check the account balance for the money inside the collections wallet account, use:

```python
from pay import PayClass

# Checking the collections balance
checkcollectionsbalance = PayClass.momobalance()
```

If the status is 200 or 202, it means the call was successful, and it will return the account balance.

### From the Disbursement Account
To check the account balance for the money inside the disbursement wallet account, use:

```python
# Checking the disbursement balance
disbursementBalanceCheck = PayClass.momobalancedisbursement()
```

If the status is 200 or 202, it means the call was successful, and it will return the account balance.

## Transfer Money from MTN Disbursement Wallet to an MTN Mobile Money Account
To transfer money from the MTN disbursement account to an MTN mobile money account, use:

```python
from pay import PayClass

# Transfer money from disbursement account
withdrawmoney = PayClass.withdrawmtnmomo(amount, currency, txt_ref, phone_number, payermessage)
```

After a successful transfer, it will either return 202 or 200. To check the status, print this:

```python
print(withdrawmoney["response"])
```

To check the transaction UUID (Reference), print this:

```python
print(withdrawmoney["ref"])
```

**Note:** The call `withdrawmoney["ref"]` returns a unique UUID (reference) which will be used in the next part.

## Checking Withdraw Status
To check the withdraw status after calling a withdraw function, use the following code:

```python
from pay import PayClass

CheckWithdrawStatus = PayClass.checkwithdrawstatus("UUID reference returned from the transfer")
```
```

Feel free to modify any sections as needed!
