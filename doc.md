# MTN Mobile Money API Integration

## Description

This project demonstrates how to integrate with the MTN Mobile Money API to create an API user. It utilizes the `requests` library to make HTTP requests and the `json` library to handle JSON data. Credentials and configuration values are stored securely in a `config.json` file.


## Packages Used

1.  **requests**
    -   Used for making HTTP requests to the MTN Mobile Money API.
    -   Installation: `!pip install requests==2.31.0`
2.  **json**
    -   Used for encoding and decoding JSON data.
    -   Included in the Python standard library, no installation needed.
3.  **os**
    -   Used for interacting with the operating system, primarily for file operations.
    -   Included in the Python standard library, no installation needed.


## Configuration

1.  **config.json:**
    -   Create a file named `config.json` in the same directory as your Python script.
    -   Populate the file with your API credentials and configuration values:

``` json
  {
      "ACCURL": "https://sandbox.momodeveloper.mtn.com",
      "COLLECTIONS_APIUSER": "your_api_user",
      "COLLECTIONS_SUBKEY": "your_sub_key",
      "PROVIDER_CALLBACK_HOST": "https://google.com"
    }

```

``` bash

  -   Replace placeholders with your actual values.
  -   Keep this file secure and do not commit it to version control.

```

    -   Replace placeholders with your actual values.
    -   Keep this file secure and do not commit it to version control.

## Usage

1.  Install the `requests` package if you haven't already.
2.  Create the `config.json` file and add your credentials.
3.  Run the Python script.

## Function: `create_api_user`

``` python

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
    # ... (function implementation) ...

```



"""

-   This function makes a POST request to the MTN Mobile Money API to create an API user.
-   It handles potential errors during the request and JSON decoding.
-   Returns the API user details if successful, otherwise returns `None`.


## Error Handling

-   The code includes `try-except` blocks to handle potential errors:
    -   `requests.exceptions.RequestException`: Catches errors related to the HTTP request (e.g., connection issues, timeouts).
    -   `json.JSONDecodeError`: Catches errors during JSON decoding of the response.
-   Error messages are printed to the console for debugging purposes.

## Security Considerations

-   Store your API credentials securely in the `config.json` file.
-   Do not commit the `config.json` file to version control.
-   Consider using environment variables or a secrets management tool for enhanced security in production environments.

