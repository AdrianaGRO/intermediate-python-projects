"""
Deal finder that coordinates flight and hotel searches
"""
import random
import time
from datetime import datetime, timedelta
from config import Config
from flight_service import FlightService
from hotel_service import HotelService


class DealFinder:
    """Main class that coordinates deal searching"""
    
    def __init__(self):
        self.flight_service = FlightService()
        self.hotel_service = HotelService()
        self.request_count = 0
    
    def find_daily_deals(self):
        """Find the best deals for today"""
        today = datetime.now().date()
        travel_date = today + timedelta(days=1)  # Tomorrow's travel
        
        print(f"\n🔍 Searching for deals from {Config.DEPARTURE_CITY_NAME} on {today}")
        print(f"📅 Travel date: {travel_date}")
        
        # Select cities for today (rotated based on day of year)
        cities_to_check = self._get_daily_cities(today)
        category = self._get_daily_category(today)
        
        print(f"🌍 Today's focus: {category.replace('_', ' ').title()} destinations")
        print(f"🎯 Checking {len(cities_to_check)} cities: {', '.join([c.title() for c in cities_to_check])}")
        
        all_flight_deals = []
        all_hotel_deals = []
        
        for i, city in enumerate(cities_to_check):
            if self.request_count >= Config.MAX_API_REQUESTS:
                print(f"⚠️  Reached API limit ({Config.MAX_API_REQUESTS} requests)")
                break
            
            print(f"\n🏛️  Checking {city.title()} ({i+1}/{len(cities_to_check)})...")
            
            # Search flights
            flight_deals = self.flight_service.search_flights(
                city, travel_date, Config.MAX_FLIGHT_PRICE
            )
            all_flight_deals.extend(flight_deals)
            self.request_count += 1
            
            # Search hotels (every other city to manage API usage)
            if i % 2 == 0 and self.request_count < Config.MAX_API_REQUESTS:
                hotel_deals = self.hotel_service.search_hotels(
                    city, travel_date, travel_date + timedelta(days=2), Config.MAX_HOTEL_PRICE
                )
                all_hotel_deals.extend(hotel_deals)
                self.request_count += 1
            
            # Rate limiting
            time.sleep(Config.REQUEST_DELAY)
        
        return self._summarize_deals(all_flight_deals, all_hotel_deals, category)
    
    def _get_daily_cities(self, date):
        """Get cities to check based on the day"""
        category = self._get_daily_category(date)
        cities = Config.CITY_GROUPS[category]
        
        # Use date as seed for consistent daily rotation
        random.seed(date.timetuple().tm_yday)
        return random.sample(cities, min(6, len(cities)))
    
    def _get_daily_category(self, date):
        """Get city category based on the day"""
        categories = list(Config.CITY_GROUPS.keys())
        # Rotate category based on day of year
        return categories[date.timetuple().tm_yday % len(categories)]
    
    def _summarize_deals(self, flight_deals, hotel_deals, category):
        """Create a summary of all deals found"""
        summary = {
            'date': datetime.now().date().isoformat(),
            'category': category,
            'total_requests': self.request_count,
            'flight_deals': flight_deals,
            'hotel_deals': hotel_deals,
            'cheapest_flight': None,
            'cheapest_hotel': None
        }
        
        # Find cheapest deals
        if flight_deals:
            summary['cheapest_flight'] = self.flight_service.get_cheapest_flight(flight_deals)
        
        if hotel_deals:
            summary['cheapest_hotel'] = self.hotel_service.get_cheapest_hotel(hotel_deals)
        
        return summary