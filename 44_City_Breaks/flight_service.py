"""
Flight search service using Amadeus API
"""
import requests
from datetime import datetime
from config import Config
import time


class FlightService:
    """Handle flight searches using Amadeus API"""
    
    def __init__(self):
        self.client_id = Config.AMADEUS_CLIENT_ID
        self.client_secret = Config.AMADEUS_CLIENT_SECRET
        self.token = None
        self.token_expires = None
    
    def get_access_token(self):
        """Get OAuth access token from Amadeus"""
        if self.token and self.token_expires and datetime.now().timestamp() < self.token_expires:
            return self.token
        
        try:
            base_url = "https://test.api.amadeus.com" if Config.USE_TEST_API else "https://api.amadeus.com"
            auth_url = f"{base_url}/v1/security/oauth2/token"
            auth_data = {
                'grant_type': 'client_credentials',
                'client_id': self.client_id,
                'client_secret': self.client_secret
            }
            
            response = requests.post(auth_url, data=auth_data, timeout=10)
            if response.status_code == 200:
                token_data = response.json()
                self.token = token_data['access_token']
                # Token expires in 1799 seconds, we'll refresh after 1700
                self.token_expires = datetime.now().timestamp() + 1700
                print("✅ Amadeus token obtained")
                return self.token
            else:
                print(f"❌ Token request failed: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error getting token: {e}")
            return None
    
    def search_flights(self, destination_city, departure_date, max_price=None):
        """Search for flights from OTP to destination"""
        token = self.get_access_token()
        if not token:
            return []
        
        destination_code = Config.EUROPEAN_DESTINATIONS.get(destination_city.lower())
        if not destination_code:
            print(f"❌ Airport code not found for {destination_city}")
            return []
        
        try:
            base_url = "https://test.api.amadeus.com" if Config.USE_TEST_API else "https://api.amadeus.com"
            flight_url = f"{base_url}/v2/shopping/flight-offers"
            headers = {'Authorization': f'Bearer {token}'}
            params = {
                'originLocationCode': Config.DEPARTURE_CITY,
                'destinationLocationCode': destination_code,
                'departureDate': departure_date.strftime('%Y-%m-%d'),
                'adults': 1,
                'max': 10
            }
            
            response = requests.get(flight_url, headers=headers, params=params, timeout=15)
            
            if response.status_code != 200:
                print(f"❌ Flight search failed for {destination_city}: {response.status_code}")
                return []
            
            flight_data = response.json()
            deals = []
            max_price = max_price or Config.MAX_FLIGHT_PRICE
            
            for offer in flight_data.get('data', []):
                try:
                    price = float(offer['price']['total'])
                    if price <= max_price:
                        # Get airline code
                        airline_code = 'Unknown'
                        try:
                            airline_code = offer['itineraries'][0]['segments'][0]['carrierCode']
                        except:
                            pass
                        
                        # Try to get booking link
                        booking_link = self._generate_booking_link(offer, destination_code, departure_date)
                        
                        deal = {
                            'destination': destination_city.title(),
                            'destination_code': destination_code,
                            'price': price,
                            'airline': airline_code,
                            'currency': offer['price']['currency'],
                            'departure_date': departure_date.strftime('%Y-%m-%d'),
                            'booking_link': booking_link,
                            'offer_id': offer.get('id', ''),
                            'found_at': datetime.now().isoformat()
                        }
                        deals.append(deal)
                        
                except (KeyError, ValueError):
                    continue
            
            if deals:
                print(f"✈️  Found {len(deals)} flight deals to {destination_city.title()}")
            
            return deals
            
        except Exception as e:
            print(f"❌ Error searching flights to {destination_city}: {e}")
            return []
    
    def _generate_booking_link(self, offer, destination_code, departure_date):
        """Generate booking links for flight offers"""
        try:
            # Create direct search links to popular booking sites
            date_str = departure_date.strftime('%Y-%m-%d')
            
            # Skyscanner link (most reliable)
            skyscanner_link = f"https://www.skyscanner.com/transport/flights/{Config.DEPARTURE_CITY}/{destination_code}/{date_str}/"
            
            # Kayak as backup
            kayak_link = f"https://www.kayak.com/flights/{Config.DEPARTURE_CITY}-{destination_code}/{date_str}"
            
            # Google Flights
            google_flights = f"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI1LTEwLTE2agcIARIDT1RQcgcIARID{destination_code}QAFIAWgBcgIIAQ"
            
            return {
                'skyscanner': skyscanner_link,
                'kayak': kayak_link,
                'google_flights': google_flights,
                'airline': offer.get('validatingAirlineCodes', [''])[0] if offer.get('validatingAirlineCodes') else ''
            }
            
        except Exception as e:
            print(f"Warning: Could not generate booking links: {e}")
            return {
                'skyscanner': f"https://www.skyscanner.com/flights",
                'kayak': f"https://www.kayak.com/flights",
                'google_flights': f"https://www.google.com/travel/flights"
            }
    
    def get_cheapest_flight(self, deals_list):
        """Get the cheapest flight from a list of deals"""
        if not deals_list:
            return None
        
        return min(deals_list, key=lambda x: x['price'])