"""
Hotel search service using Booking.com API via RapidAPI
"""
import requests
from datetime import datetime
from config import Config


class HotelService:
    """Handle hotel searches using Booking.com API"""
    
    def __init__(self):
        self.rapidapi_key = Config.RAPIDAPI_KEY
        self.headers = {
            'X-RapidAPI-Key': self.rapidapi_key,
            'X-RapidAPI-Host': 'booking-com.p.rapidapi.com'
        }
    
    def search_hotels(self, destination_city, checkin_date, checkout_date, max_price=None):
        """Search for hotels in destination city"""
        try:
            # First, get location info
            location_id = self._get_location_id(destination_city)
            if not location_id:
                return []
            
            # Search hotels
            hotels_url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
            params = {
                'dest_id': location_id,
                'order_by': 'price',
                'adults_number': 1,
                'checkin_date': checkin_date.strftime('%Y-%m-%d'),
                'checkout_date': checkout_date.strftime('%Y-%m-%d'),
                'filter_by_currency': 'EUR',
                'locale': 'en-us',
                'room_number': 1,
                'units': 'metric'
            }
            
            response = requests.get(hotels_url, headers=self.headers, params=params, timeout=15)
            
            if response.status_code != 200:
                print(f"❌ Hotel search failed for {destination_city}: {response.status_code}")
                return []
            
            hotel_data = response.json()
            deals = []
            max_price = max_price or Config.MAX_HOTEL_PRICE
            
            for hotel in hotel_data.get('result', []):
                try:
                    # Get price per night
                    price_info = hotel.get('composite_price_breakdown', {})
                    if not price_info:
                        continue
                    
                    price_per_night = float(price_info.get('net_amount', {}).get('value', 0))
                    if price_per_night > 0 and price_per_night <= max_price:
                        # Generate booking links
                        booking_links = self._generate_hotel_booking_links(destination_city, checkin_date, checkout_date)
                        
                        deal = {
                            'city': destination_city.title(),
                            'name': hotel.get('hotel_name', 'Unknown Hotel'),
                            'price': price_per_night,
                            'currency': price_info.get('net_amount', {}).get('currency', 'EUR'),
                            'rating': hotel.get('review_score', 0),
                            'distance_km': hotel.get('distance', 0),
                            'checkin_date': checkin_date.strftime('%Y-%m-%d'),
                            'checkout_date': checkout_date.strftime('%Y-%m-%d'),
                            'booking_links': booking_links,
                            'hotel_id': hotel.get('hotel_id', ''),
                            'found_at': datetime.now().isoformat()
                        }
                        deals.append(deal)
                        
                except (KeyError, ValueError, TypeError):
                    continue
            
            if deals:
                print(f"🏨 Found {len(deals)} hotel deals in {destination_city.title()}")
            
            return deals
            
        except Exception as e:
            print(f"❌ Error searching hotels in {destination_city}: {e}")
            return []
    
    def _get_location_id(self, city_name):
        """Get Booking.com location ID for a city"""
        try:
            locations_url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
            params = {
                'locale': 'en-us',
                'name': city_name
            }
            
            response = requests.get(locations_url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                locations = response.json()
                if locations and len(locations) > 0:
                    return locations[0].get('dest_id')
            
            print(f"❌ Could not find location ID for {city_name}")
            return None
            
        except Exception as e:
            print(f"❌ Error getting location for {city_name}: {e}")
            return None
    
    def _generate_hotel_booking_links(self, city, checkin_date, checkout_date):
        """Generate hotel booking links"""
        try:
            checkin_str = checkin_date.strftime('%Y-%m-%d')
            checkout_str = checkout_date.strftime('%Y-%m-%d')
            
            # Booking.com
            booking_link = f"https://www.booking.com/searchresults.html?ss={city}&checkin={checkin_str}&checkout={checkout_str}&group_adults=1"
            
            # Hotels.com  
            hotels_link = f"https://www.hotels.com/search.do?destination={city}&startDate={checkin_str}&endDate={checkout_str}&rooms=1&adults=1"
            
            # Expedia
            expedia_link = f"https://www.expedia.com/Hotel-Search?destination={city}&startDate={checkin_str}&endDate={checkout_str}&rooms=1&adults=1"
            
            return {
                'booking_com': booking_link,
                'hotels_com': hotels_link,
                'expedia': expedia_link
            }
            
        except Exception as e:
            print(f"Warning: Could not generate hotel booking links: {e}")
            return {
                'booking_com': 'https://www.booking.com',
                'hotels_com': 'https://www.hotels.com',
                'expedia': 'https://www.expedia.com'
            }
    
    def get_cheapest_hotel(self, deals_list):
        """Get the cheapest hotel from a list of deals"""
        if not deals_list:
            return None
        
        return min(deals_list, key=lambda x: x['price'])