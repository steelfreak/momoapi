# momoapi
Basic Start


To create an API user in the MTN MoMo Developer API using Postman, you’ll need to follow these steps. The request will include the headers `X-Reference-Id` and `Ocp-Apim-Subscription-Key`, along with a JSON body containing `providerCallbackHost`.

### Step-by-Step Guide

### A. Generate: API-USER

#### 1\. Open Postman

Launch the Postman application on your computer.

#### 2\. Create a New Request

- Click on the **New** button or the **+** icon to open a new tab.
    
- Select **HTTP Request**.
    

#### 3\. Set the Request Method and URL

- Change the request method to **POST**.
    

Use Address: [https://sandbox.momodeveloper.mtn.com/v1_0/apiuser](https://sandbox.momodeveloper.mtn.com/v1_0/apiuser)

#### 4\. Add Headers

Click on the **Headers** tab and add the following key-value pairs:

| Key | Value |
| --- | --- |
| X-Reference-Id | your-unique-reference-id |
| Ocp-Apim-Subscription-Key | your-subscription-key |

Replace `your-unique-reference-id` and `your-subscription-key` with your actual values. an easier way to find one is here: [https://www.uuidgenerator.net/](https://www.uuidgenerator.net/)

#### 5\. Add the Request Body

Click on the **Body** tab and select **raw**. Then, set the format to **JSON**. Input the following JSON object:

``` json
{
    "providerCallbackHost": "string"
}

 ```

Replace `"string"` with the actual callback host you intend to use though it can still remain as is to avoid confusion.

#### 6\. Send the Request

- Review all the information you entered to ensure it's correct.
    
- Click the **Send** button.
    

#### 7\. Review the Response

- After sending the request, check the response section to see if your API user was created successfully.
    
- A successful response should return a status code of **201 Created** along with a response body containing details about the newly created API user.
    

### Example

Here's a complete example for clarity:

#### Request Example

- **Method**: POST
    
- **URL**: `https://sandbox.momodeveloper.mtn.com/v1_0/apiuser`
    
- **Headers**:
    
    - `X-Reference-Id`: `123456789`
        
    - `Ocp-Apim-Subscription-Key`: `abcdef123456`
        
    - `Content-Type`: `application/json`
        
- ## **Body**:
    ``` json
{
    "providerCallbackHost": "[https://yourcallbackhost.com"](https://yourcallbackhost.com)
}

 ```    

{ "providerCallbackHost": "[https://yourcallbackhost.com"](https://yourcallbackhost.com) }

### Common Issues

- **Invalid Subscription Key**: Make sure your subscription key is correct and active.
    
- **Malformed JSON**: Ensure that your JSON body is well-formed.
    
- **Network Issues**: Check your internet connection if the request fails to send.
    

This should help you create an API user in the MTN MoMo Developer sandbox environment using Postman. Let me know if you need further assistance!

### B. View: API-key

#### 1\. Create a New Request

- Click on the **New** button or the **+** icon to open a new tab.
    
- Select **HTTP Request**.
    

#### 2\. Set the Request Method and URL

- Change the request method to **POST**.
    

Use Address: [https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{X-Reference-Id}/apikey](https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/%7BX-Reference-Id%7D/apikey)

Make sure to used "[X-Reference-Id](https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/%7BX-Reference-Id%7D/apikey)" from step A above without "{", "}".

#### 4\. Add Headers

Click on the **Headers** tab and add the following key-value pairs:

| Key | Value |
| --- | --- |
| X-Reference-Id | your-unique-reference-id |
| Ocp-Apim-Subscription-Key | your-subscription-key |

Replace `your-unique-reference-id` and `your-subscription-key` with your actual values.

#### 5\. Add the Request Body

Click on the **Body** tab and select **raw**. Then, set the format to **JSON**. Input the following JSON object:

``` json
{
    "providerCallbackHost": "string"
}

 ```

Replace `"string"` with the actual callback host you intend to use though it can still remain as is to avoid confusion.

#### 6\. Send the Request

- Review all the information you entered to ensure it's correct.
    
- Click the **Send** button.
    

#### 7\. Review the Response

- After sending the request, check the response section to see if your API user was created successfully.
    
- A successful response should return a status code of **201 Created** along with a response body containing details about the newly created API user.
    

### Example

Here's a complete example for clarity:

#### Request Example

- **Method**: POST
    
- **URL**: `https://sandbox.momodeveloper.mtn.com/v1_0/apiuser`
    
- **Headers**:
    
    - `X-Reference-Id`: `123456789`
        
    - `Ocp-Apim-Subscription-Key`: `abcdef123456`
        
    - `Content-Type`: `application/json`
        
- { "providerCallbackHost": "[https://yourcallbackhost.com"](https://yourcallbackhost.com) }
    

### Common Issues

- **Invalid Subscription Key**: Make sure your subscription key is correct and active.
    
- **Malformed JSON**: Ensure that your JSON body is well-formed.
    
- **Network Issues**: Check your internet connection if the request fails to send.
    

This should help you create an API user in the MTN MoMo Developer sandbox environment using Postman. Let me know if you need further assistance!
