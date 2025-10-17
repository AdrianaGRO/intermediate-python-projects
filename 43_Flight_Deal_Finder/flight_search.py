
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from rate_limiter import rate_limited



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.token = self.get_token()

    #Authorizing the Application
    def get_token(self):
        url_token = "https://test.api.amadeus.com/v1/security/oauth2/token"
        params_token = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        response = requests.post(url_token, data=params_token)
        response.raise_for_status()
        token = response.json().get("access_token")
        return token
    
    @rate_limited(max_calls_per_minute=8)  # Conservative rate limiting
    def get_destination_code(self, city_name):
        """Get IATA code for a city using Amadeus API"""
        if not self.token:
            return None
            
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS"
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data["data"]:
                # Return the IATA code of the first airport found
                return data["data"][0]["iataCode"]
            else:
                print(f"No IATA code found for {city_name}")
                return None
        except Exception as e:
            print(f"Error getting IATA code for {city_name}: {e}")
            return None
    
    @rate_limited(max_calls_per_minute=5)  # More conservative for flight searches
    def search_flights(self, origin_airport_code, destination_airport_code, from_time, to_time):
        """Search for flights using Amadeus API with rate limit handling"""
        if not self.token:
            print("No valid token available")
            return None
            
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "originLocationCode": origin_airport_code,
            "destinationLocationCode": destination_airport_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "false",  # Allow connecting flights for better prices
            "max": 50,  # Get more options to find cheaper flights
            "currencyCode": "EUR",  # Force EUR pricing
            "travelClass": "ECONOMY"  # Economy class for budget prices
        }
        
        # Add return date if to_time is provided (round trip)
        if to_time:
            params["returnDate"] = to_time.strftime("%Y-%m-%d")
        
        try:
            response = requests.get(url, headers=headers, params=params)
            
            # Handle rate limiting
            if response.status_code == 429:
                print("Rate limit reached. Waiting 60 seconds...")
                import time
                time.sleep(60)
                # Retry once after waiting
                response = requests.get(url, headers=headers, params=params)
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                print("Authentication failed. Refreshing token...")
                self.token = self.get_token()
                return None
            else:
                print(f"HTTP error searching flights: {e}")
                return None
        except Exception as e:
            print(f"Error searching flights: {e}")
            return None
    
    def search_flights_with_retry(self, origin_airport_code, destination_airport_code, from_time, to_time, max_retries=3):
        """Search flights with automatic retry and exponential backoff"""
        import time
        import random
        
        for attempt in range(max_retries):
            try:
                result = self.search_flights(origin_airport_code, destination_airport_code, from_time, to_time)
                if result:
                    return result
                    
                # If no result, wait before retry
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)  # Exponential backoff with jitter
                    print(f"Attempt {attempt + 1} failed. Retrying in {wait_time:.1f} seconds...")
                    time.sleep(wait_time)
                    
            except Exception as e:
                print(f"Attempt {attempt + 1} failed with error: {e}")
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(wait_time)
        
        print(f"All {max_retries} attempts failed")
        return None

