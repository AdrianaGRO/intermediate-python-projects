import requests
import os
from dotenv import load_dotenv
load_dotenv()
import pprint



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.sheety_token = os.getenv("SHEETY_TOKEN")
        self.headers = {
            "Authorization": f"Basic {self.sheety_token}",
            "Content-Type": "application/json"
        }
        
    def get_destination_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data["prices"]
    
    def update_destination_codes(self, data):
        endpoint = f"https://api.sheety.co/1af5beda46a1fd3be6c52133da60a214/octoberFlightDeals/prices/{data['id']}"
        body = {
            "price": {
                "iataCode": data["iataCode"]
            }
        }
        response = requests.put(url=endpoint, json=body, headers=self.headers)
        response.raise_for_status()
        print(response.text)
        return response.json()["price"]["iataCode"]
       
        
