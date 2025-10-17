#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData
import os
from dotenv import load_dotenv
load_dotenv()
import pprint
import time

from datetime import datetime, timedelta
import config
from booking_tips import print_booking_tips, get_romanian_booking_sites

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()

print("=== FLIGHT DEAL FINDER FROM BUCHAREST ===")
print(f"Searching for flights from {config.HOME_CITY} ({config.ORIGIN_CITY_IATA})")
print()

# Update destination codes for each row in the sheet data
for row in sheet_data:
    if row["iataCode"] == "":  # Only update if IATA code is missing
        # Get IATA code from flight search API
        iata_code = flight_search.get_destination_code(row["city"])
        time.sleep(2)  # To avoid hitting rate limits
        if iata_code:
            row["iataCode"] = iata_code
            updated_row = data_manager.update_destination_codes(row)
            print(f"Updated {row['city']} with IATA code: {iata_code}")
        else:
            print(f"Could not find IATA code for {row['city']}")
    else:
        print(f"{row['city']} already has IATA code: {row['iataCode']}")

print("\n=== SEARCHING FOR FLIGHT DEALS ===")

# Set up date range for flight search - closer dates for better prices
tomorrow = datetime.now() + timedelta(days=config.SEARCH_DAYS_AHEAD)
# Search in next 2-8 weeks for better prices (budget airlines book closer to departure)
search_until = datetime.now() + timedelta(days=56)  # 8 weeks ahead

# EUR to RON conversion rate (approximate)
EUR_TO_RON = 4.97  # Update this with current exchange rate

# Search for flights to each destination
for destination in sheet_data:
    destination_iata = destination["iataCode"]
    destination_city = destination["city"]
    price_threshold = destination["lowestPrice"]
    
    print(f"\nSearching flights from Bucharest to {destination_city} ({destination_iata})")
    print(f"Price threshold: ${price_threshold}")
    
    # Search for flights with rate limiting
    flight_data = flight_search.search_flights_with_retry(
        origin_airport_code=config.ORIGIN_CITY_IATA,
        destination_airport_code=destination_iata,
        from_time=tomorrow,
        to_time=search_until
    )
    
    if flight_data:
        # Process flight data
        cheapest_flight = FlightData()
        flight_info = cheapest_flight.find_cheapest_flight(flight_data)
        
        if flight_info and flight_info.price:
            price_ron = flight_info.price * EUR_TO_RON
            print(f"Cheapest flight found: {flight_info.price:.2f} {flight_info.currency} (≈ {price_ron:.0f} RON)")
            
            # Convert threshold to EUR for comparison (assuming threshold is in USD, convert to EUR)
            threshold_eur = price_threshold * 0.85  # Approximate USD to EUR
            
            # Check if it's a good deal
            if float(flight_info.price) <= threshold_eur:
                print(f"🎉 DEAL ALERT! Flight to {destination_city} for {flight_info.price:.2f} {flight_info.currency} (≈ {price_ron:.0f} RON)")
                print(f"Details: {flight_info}")
                print(f"💡 Compare with Ryanair/Wizz Air directly for potentially lower prices!")
                
                # Here you could send notification
                # notification_manager = NotificationManager()
                # notification_manager.send_sms(flight_info)
            else:
                print(f"Price {flight_info.price:.2f} {flight_info.currency} (≈ {price_ron:.0f} RON) is above threshold")
            
            # Always show booking tips for better prices
            print_booking_tips(destination_city, flight_info.price)
        else:
            print("No valid flight data found")
    else:
        print("Failed to get flight data")
    
    # Rate limiting between requests
    if destination != sheet_data[-1]:  # Don't wait after the last search
        print(f"Waiting {config.WAIT_BETWEEN_SEARCHES} seconds before next search...")
        time.sleep(config.WAIT_BETWEEN_SEARCHES)

print("\n" + "="*60)
print("🇷🇴 RECOMMENDED BOOKING SITES FOR ROMANIAN TRAVELERS:")
print("="*60)
for i, site in enumerate(get_romanian_booking_sites(), 1):
    print(f"{i}. {site}")

print(f"\n💰 MONEY-SAVING TIPS:")
print(f"• Book directly with airlines (Ryanair, Wizz Air, Blue Air)")
print(f"• Use flexible dates (+/- 3 days)")
print(f"• Consider nearby airports (Budapest, Belgrade)")
print(f"• Clear browser cookies between searches")
print(f"• Book Tuesday/Wednesday departures")
print(f"• Avoid peak travel times (holidays, weekends)")
print("="*60)

