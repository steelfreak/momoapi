import json
import requests
import os

# Load values from config.json
with open("config.json", "r") as config_file:
    config_data = json.load(config_file)

# Access values
accurl = config_data["ACCURL"]
collections_apiuser = config_data["COLLECTIONS_APIUSER"]
collections_subkey = config_data["COLLECTIONS_SUBKEY"]
provider_callback_host = config_data["PROVIDER_CALLBACK_HOST"]


# Function to create API user
def create_api_user(accurl, collections_apiuser, collections_subkey, provider_callback_host):
    """Creates an API user.

    Args:
        accurl: The base URL of the API.
        collections_apiuser: The unique reference ID for the API user.
        collections_subkey: The subscription key for the API user.
        provider_callback_host: The callback host URL.

    Returns:
        A dictionary containing the API user details, or None if an error occurred.
    """
    url = f"{accurl}/v1_0/apiuser"
    payload = json.dumps({"providerCallbackHost": provider_callback_host})
    headers = {
        'X-Reference-Id': collections_apiuser,
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': collections_subkey
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        print(response.text if response else "No response available")  
        return None  
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        print(response.text if response else "No response available")
        return None

# Call the function to create API user
api_user_data = create_api_user(accurl, collections_apiuser, collections_subkey, provider_callback_host)

if api_user_data:
    print("API user created successfully:")
    print(api_user_data)  
else:
    print("Failed to create API user.")
