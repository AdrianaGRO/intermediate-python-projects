"""
Simple Daily Deal Monitor for Travel Deals
Monitors flight and hotel prices and alerts when targets are met
"""
import requests
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SimpleConfig:
    """Simple configuration"""
    AMADEUS_CLIENT_ID = os.getenv('AMADEUS_CLIENT_ID')
    AMADEUS_CLIENT_SECRET = os.getenv('AMADEUS_CLIENT_SECRET')
    RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
    
    @classmethod
    def is_valid(cls):
        return all([cls.AMADEUS_CLIENT_ID, cls.AMADEUS_CLIENT_SECRET, cls.RAPIDAPI_KEY])

class SimpleDealMonitor:
    """Simple deal monitoring system"""
    
    def __init__(self):
        self.deals_file = 'deals.json'
        self.load_deals()
    
    def load_deals(self):
        """Load existing deals"""
        try:
            if os.path.exists(self.deals_file):
                with open(self.deals_file, 'r') as f:
                    self.deals = json.load(f)
            else:
                self.deals = []
        except:
            self.deals = []
    
    def save_deals(self):
        """Save deals to file"""
        with open(self.deals_file, 'w') as f:
            json.dump(self.deals, f, indent=2, default=str)
    
    def get_amadeus_token(self):
        """Get Amadeus access token"""
        try:
            url = "https://test.api.amadeus.com/v1/security/oauth2/token"
            data = {
                'grant_type': 'client_credentials',
                'client_id': SimpleConfig.AMADEUS_CLIENT_ID,
                'client_secret': SimpleConfig.AMADEUS_CLIENT_SECRET
            }
            response = requests.post(url, data=data, timeout=10)
            if response.status_code == 200:
                return response.json().get('access_token')
        except:
            pass
        return None
    
    def get_airport_code(self, city_name):
        """Get airport code for a city (comprehensive European mapping)"""
        airport_codes = {
            # Western Europe
            'paris': 'CDG',
            'amsterdam': 'AMS',
            'bruges': 'BRU',  # Brussels Airport for Bruges
            'edinburgh': 'EDI',
            'london': 'LHR',
            'dublin': 'DUB',
            'brussels': 'BRU',
            
            # Southern Europe - Italy
            'florence': 'FLR',
            'venice': 'VCE',
            'rome': 'FCO',
            'milan': 'MXP',
            'verona': 'VRN',
            'bologna': 'BLQ',
            'naples': 'NAP',
            'pisa': 'PSA',  # For Cinque Terre
            
            # Southern Europe - Spain & Portugal
            'barcelona': 'BCN',
            'madrid': 'MAD',
            'seville': 'SVQ',
            'granada': 'GRX',
            'valencia': 'VLC',
            'lisbon': 'LIS',
            'porto': 'OPO',
            
            # Southern Europe - Greece
            'athens': 'ATH',
            'santorini': 'JTR',
            'mykonos': 'JMK',
            'thessaloniki': 'SKG',
            'chania': 'CHQ',
            'heraklion': 'HER',
            'rhodes': 'RHO',
            'nafplio': 'ATH',  # Use Athens for Nafplio
            
            # Southern Europe - Other
            'dubrovnik': 'DBV',
            'split': 'SPU',
            'kotor': 'TGD',  # Podgorica for Montenegro
            'istanbul': 'IST',
            
            # Central Europe
            'prague': 'PRG',
            'vienna': 'VIE',
            'budapest': 'BUD',
            'salzburg': 'SZG',
            'munich': 'MUC',
            'berlin': 'BER',
            'zurich': 'ZUR',
            'lucerne': 'ZUR',  # Use Zurich for Lucerne
            'innsbruck': 'INN',
            
            # Northern Europe
            'copenhagen': 'CPH',
            'stockholm': 'ARN',
            'bergen': 'BGO',
            'oslo': 'OSL',
            'helsinki': 'HEL',
            'reykjavik': 'KEF',
            
            # Eastern Europe
            'krakow': 'KRK',
            'warsaw': 'WAW',
            'tallinn': 'TLL',
            'riga': 'RIX',
            'vilnius': 'VNO',
            'bucharest': 'OTP'
        }
        return airport_codes.get(city_name.lower())

    def search_flights(self, origin, destination, date, target_price):
        """Search for flights under target price"""
        token = self.get_amadeus_token()
        if not token:
            print(f"❌ Could not get Amadeus token")
            return []
        
        try:
            # Get airport codes
            origin_code = self.get_airport_code(origin)
            dest_code = self.get_airport_code(destination)
            
            if not origin_code or not dest_code:
                print(f"❌ Could not find airports for {origin} → {destination}")
                return []
            
            # Search flights
            flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
            headers = {'Authorization': f'Bearer {token}'}
            params = {
                'originLocationCode': origin_code,
                'destinationLocationCode': dest_code,
                'departureDate': date,
                'adults': 1,
                'max': 10
            }
            
            response = requests.get(flight_url, headers=headers, params=params, timeout=15)
            if response.status_code != 200:
                print(f"❌ Flight search failed: {response.status_code}")
                return []
            
            flight_data = response.json()
            good_deals = []
            
            for offer in flight_data.get('data', []):
                try:
                    price = float(offer['price']['total'])
                    if price <= target_price:
                        # Get airline info
                        airline_code = 'Unknown'
                        try:
                            airline_code = offer['itineraries'][0]['segments'][0]['carrierCode']
                        except:
                            pass
                            
                        deal = {
                            'type': 'flight',
                            'route': f"{origin} → {destination}",
                            'price': price,
                            'airline': airline_code,
                            'target': target_price,
                            'date': date,
                            'found_on': datetime.now().isoformat(),
                            'details': {
                                'from': origin_code,
                                'to': dest_code,
                                'currency': offer['price']['currency']
                            }
                        }
                        good_deals.append(deal)
                        print(f"🎉 FLIGHT DEAL: {origin} → {destination} for €{price} ({airline_code}) - target: €{target_price}")
                except:
                    continue
            
            return good_deals
            
        except Exception as e:
            print(f"❌ Error searching flights: {e}")
            return []
    
    def search_hotels(self, city, checkin, checkout, target_price, max_distance_km=3):
        """Search for hotels under target price"""
        try:
            # Search locations
            url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
            headers = {
                "X-RapidAPI-Key": SimpleConfig.RAPIDAPI_KEY,
                "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
            }
            
            response = requests.get(url, headers=headers, 
                                  params={"name": city, "locale": "en-us"}, timeout=10)
            
            if response.status_code != 200:
                print(f"❌ Could not search {city} locations")
                return []
            
            locations = response.json()
            if not locations:
                print(f"❌ No locations found for {city}")
                return []
            
            dest_id = locations[0].get('dest_id')
            if not dest_id:
                print(f"❌ No destination ID for {city}")
                return []
            
            # Search hotels
            search_url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
            params = {
                "dest_id": str(dest_id),
                "order_by": "popularity",
                "locale": "en-us",
                "checkout_date": checkout,
                "checkin_date": checkin,
                "adults_number": 1,
                "room_number": 1,
                "currency": "EUR",
                "page_number": 0
            }
            
            response = requests.get(search_url, headers=headers, params=params, timeout=15)
            if response.status_code != 200:
                print(f"❌ Hotel search failed for {city}")
                return []
            
            hotel_data = response.json()
            good_deals = []
            
            for hotel in hotel_data.get('result', []):
                try:
                    price_breakdown = hotel.get('price_breakdown', {})
                    gross_price = price_breakdown.get('gross_price')
                    
                    if not gross_price or gross_price == 'N/A':
                        continue
                    
                    price = float(gross_price)
                    distance_str = hotel.get('distance_to_cc', '999')
                    
                    # Parse distance
                    if 'km' in str(distance_str):
                        distance = float(str(distance_str).replace('km', '').strip())
                    else:
                        distance = 999
                    
                    if price <= target_price and distance <= max_distance_km:
                        deal = {
                            'type': 'hotel',
                            'city': city,
                            'name': hotel.get('hotel_name', 'Unknown'),
                            'price': price,
                            'target': target_price,
                            'distance_km': distance,
                            'checkin': checkin,
                            'checkout': checkout,
                            'found_on': datetime.now().isoformat(),
                            'details': {
                                'rating': hotel.get('review_score', 0),
                                'location': hotel.get('address', '')
                            }
                        }
                        good_deals.append(deal)
                        print(f"🏨 HOTEL DEAL: {hotel.get('hotel_name')} in {city} for €{price}/night ({distance}km from center)")
                except:
                    continue
            
            return good_deals
            
        except Exception as e:
            print(f"❌ Error searching hotels: {e}")
            return []
    
    def check_deals(self):
        """Check for flight and hotel deals across beautiful European cities"""
        today = datetime.now().date()
        print(f"\n🔍 Checking deals for {today}")
        
        # Diverse European cities selection (rotated daily to respect API limits)
        european_cities = {
            'iconic': ['paris', 'london', 'rome', 'barcelona', 'amsterdam'],
            'eastern_gems': ['prague', 'budapest', 'vienna', 'krakow', 'bucharest'],
            'mediterranean': ['athens', 'dubrovnik', 'florence', 'lisbon', 'valencia'],
            'nordic': ['copenhagen', 'stockholm', 'helsinki', 'reykjavik', 'oslo'],
            'cultural': ['istanbul', 'brussels', 'munich', 'zurich', 'edinburgh']
        }
        
        # Rotate cities based on day of year to vary searches
        import random
        random.seed(today.timetuple().tm_yday)  # Consistent daily rotation
        category = random.choice(list(european_cities.keys()))
        cities_to_check = random.sample(european_cities[category], min(6, len(european_cities[category])))
        
        print(f"🌍 Today's focus: {category.replace('_', ' ').title()} destinations")
        
        all_deals = []
        cheapest_flight = None
        cheapest_hotel = None
        request_count = 0
        max_requests = 15  # API rate limit protection
        
        for i, city in enumerate(cities_to_check):
            if request_count >= max_requests:
                print(f"⚠️  Reached API limit ({max_requests} requests), stopping here")
                break
                
            print(f"�️  Checking {city.title()} ({i+1}/{len(cities_to_check)})...")
            
            # Check flights
            flight_deals = self.search_flights('madrid', city, today + timedelta(days=1), 120)
            request_count += 1
            
            if flight_deals:
                all_deals.append(f"✈️  Flights to {city.title()}: {len(flight_deals)} deals under €120")
                for deal in flight_deals[:1]:  # Show top deal per city
                    deal_info = f"   • €{deal['price']} - {deal['airline']}"
                    all_deals.append(deal_info)
                    
                    # Track cheapest flight
                    if not cheapest_flight or deal['price'] < cheapest_flight['price']:
                        cheapest_flight = deal.copy()
                        cheapest_flight['destination'] = city.title()
            
            # Check hotels (alternate cities to manage API usage)
            if i % 2 == 0 and request_count < max_requests:
                hotel_deals = self.search_hotels(city, today + timedelta(days=1), today + timedelta(days=3), 180)
                request_count += 1
                
                if hotel_deals:
                    all_deals.append(f"🏨 Hotels in {city.title()}: {len(hotel_deals)} deals under €180")
                    for deal in hotel_deals[:1]:  # Show top deal per city
                        deal_info = f"   • {deal['name']}: €{deal['price']}"
                        all_deals.append(deal_info)
                        
                        # Track cheapest hotel
                        if not cheapest_hotel or deal['price'] < cheapest_hotel['price']:
                            cheapest_hotel = deal.copy()
                            cheapest_hotel['city'] = city.title()
            
            # Rate limiting delay
            import time
            time.sleep(1.5)
        
        # Add today's cheapest offers summary
        if cheapest_flight or cheapest_hotel:
            summary = ["🏆 THE CHEAPEST OFFERS FOR TODAY ARE:"]
            if cheapest_flight:
                summary.append(f"   ✈️  Flight: €{cheapest_flight['price']} to {cheapest_flight['destination']} ({cheapest_flight['airline']})")
            if cheapest_hotel:
                summary.append(f"   🏨 Hotel: €{cheapest_hotel['price']} - {cheapest_hotel['name']} in {cheapest_hotel['city']}")
            summary.append(f"   📊 Searched {len(cities_to_check)} {category.replace('_', ' ')} cities with {request_count} API requests")
            summary.append("")  # Empty line separator
            
            all_deals = summary + all_deals
        
        if all_deals:
            self.create_alert(all_deals)
            return True
        else:
            print("❌ No deals found today")
            return False
    
    def create_alert(self, new_deals):
        """Create simple HTML alert"""
        if not new_deals:
            return
        
        html = f"""
        <html>
        <head><title>Travel Deals Alert</title></head>
        <body>
        <h2>🎉 {len(new_deals)} New Travel Deals Found!</h2>
        <p><strong>Found on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        """
        
        for deal in new_deals:
            if deal['type'] == 'flight':
                savings = deal['target'] - deal['price']
                html += f"""
                <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
                <h3>✈️ {deal['route']}</h3>
                <p><strong>Price:</strong> €{deal['price']} <span style="color: green;">(Save €{savings}!)</span></p>
                <p><strong>Date:</strong> {deal['date']}</p>
                <p><strong>Route:</strong> {deal['details']['from']} → {deal['details']['to']}</p>
                </div>
                """
            elif deal['type'] == 'hotel':
                savings = deal['target'] - deal['price']
                html += f"""
                <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
                <h3>🏨 {deal['name']}</h3>
                <p><strong>Price:</strong> €{deal['price']}/night <span style="color: green;">(Save €{savings}!)</span></p>
                <p><strong>Location:</strong> {deal['city']} ({deal['distance_km']}km from center)</p>
                <p><strong>Dates:</strong> {deal['checkin']} → {deal['checkout']}</p>
                <p><strong>Rating:</strong> {deal['details']['rating']}</p>
                </div>
                """
        
        html += "</body></html>"
        
        filename = f"deal_alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        with open(filename, 'w') as f:
            f.write(html)
        print(f"📧 Alert saved: {filename}")

def main():
    """Main function"""
    monitor = SimpleDealMonitor()
    monitor.check_deals()

if __name__ == "__main__":
    main()