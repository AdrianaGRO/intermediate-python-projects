import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Sheety endpoint with error handling
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
if not SHEETY_PRICES_ENDPOINT:
    raise ValueError("Missing SHEETY_PRICES_ENDPOINT environment variable. Please set it in your .env file.")


class DataManager:

    def __init__(self):
        self._token = os.getenv("SHEETY_TOKEN")
        self._headers = {"Authorization": f"Bearer {self._token}"}
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._headers)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=self._headers,
                json=new_data
            )
            print(response.text)


#GET USERS FROM GOOGLE FORM
    def get_customers_email(self):
        users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        if not users_endpoint:
            print("Warning: Missing SHEETY_USERS_ENDPOINT environment variable. Cannot retrieve customer emails.")
            return []
        
        try:
            # Get users data from Sheety API
            response = requests.get(url=users_endpoint, headers=self._headers)
            response.raise_for_status()  # Will raise an error for bad responses
            
            # Parse the JSON response
            data = response.json()
            print(f"Retrieved users data: {data}")  # Print full response for debugging
            
            # Check if 'users' key exists in the response
            if "users" in data:
                users_data = data["users"]
                print(f"Found {len(users_data)} users")
                return users_data
            else:
                # Try to find any key that might contain user data
                possible_keys = [key for key in data.keys() if key.lower() in ["user", "users", "customers", "people", "emails", "subscribers"]]
                if possible_keys:
                    users_key = possible_keys[0]
                    print(f"Using '{users_key}' instead of 'users' key")
                    return data[users_key]
                else:
                    print(f"Warning: Could not find users data in response. Available keys: {list(data.keys())}")
                    return []
        except Exception as e:
            print(f"Error retrieving customer emails: {e}")
            return []
