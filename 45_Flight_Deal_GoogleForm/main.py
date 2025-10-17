import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
customers = data_manager.get_customers_email()

# Set your origin airport
ORIGIN_CITY_IATA = "OTP"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    
    # First search for direct flights
    direct_flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        is_direct=True
    )
    
    # Check if we found direct flights
    cheapest_flight = find_cheapest_flight(direct_flights)
    
    # If no direct flights are found, search for indirect flights
    if cheapest_flight.price == "N/A":
        print(f"No direct flights found for {destination['city']}. Searching for indirect flights...")
        # Slowing down requests to avoid rate limit
        time.sleep(2)
        
        indirect_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(indirect_flights)
    
    if cheapest_flight.price != "N/A":
        stops_text = "direct flight" if cheapest_flight.stops == 0 else f"flight with {cheapest_flight.stops} stop(s)"
        print(f"{destination['city']}: £{cheapest_flight.price} ({stops_text})")
    else:
        print(f"No flights found for {destination['city']}")
    
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # Only proceed if we found a flight deal (price is lower than our target)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        
        # Prepare flight description text
        flight_type = "Direct flight" if cheapest_flight.stops == 0 else f"Flight with {cheapest_flight.stops} stop(s)"
        
        # Create the message for SMS/WhatsApp
        sms_message = (f"Low price alert! Only £{cheapest_flight.price} to fly "
                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}. "
                  f"{flight_type}.")
        
        # Create the subject and body for emails
        email_subject = f"Low price alert! Only £{cheapest_flight.price} to {destination['city']}!"
        
        # Map of IATA codes to their country's Google Flights domain
        google_flights_domains = {
            "OTP": "ro",  # Bucharest, Romania
            "MAD": "es",  # Madrid, Spain
            "BCN": "es",  # Barcelona, Spain
            "LON": "co.uk",  # London, UK
            "CDG": "fr",  # Paris, France
            "FCO": "it",  # Rome, Italy
            "ATH": "gr",  # Athens, Greece
        }
        
        # Default to .com if we don't have a specific country mapping
        domain = google_flights_domains.get(ORIGIN_CITY_IATA, "com")
        
        # Create Google Flights URL with the appropriate domain for the origin country
        flights_url = f"https://www.google.{domain}/flights?hl=en#flt={cheapest_flight.origin_airport}.{cheapest_flight.destination_airport}.{cheapest_flight.out_date}*{cheapest_flight.destination_airport}.{cheapest_flight.origin_airport}.{cheapest_flight.return_date}"
        
        email_body = (f"Low price alert! Only £{cheapest_flight.price} to fly "
                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.\n"
                  f"{flight_type}.\n\n"
                  f"Book here: {flights_url}")
        
        # Try SMS first, then WhatsApp as a fallback
        try:
            notification_manager.send_sms(message_body=sms_message)
        except Exception as e:
            print(f"SMS failed, trying WhatsApp: {e}")
            notification_manager.send_whatsapp(message_body=sms_message)
            
        # Send emails to all registered customers
        if customers:
            print(f"Sending flight deal notifications to {len(customers)} registered customers...")
            for customer in customers:
                # Check for different possible field names in Google Form responses
                customer_email = (customer.get("email") or 
                                 customer.get("emailAddress") or 
                                 customer.get("Email") or 
                                 customer.get("userEmail") or
                                 customer.get("whatIsYourEmailAddress?"))
                
                customer_name = (customer.get("firstName") or 
                                customer.get("name") or 
                                customer.get("Name") or
                                customer.get("whatIsYourFirstName?") or
                                "Valued Customer")
                
                if customer_email:
                    # Personalize email if customer name is available
                    personalized_body = f"Hello {customer_name},\n\n{email_body}"
                    
                    print(f"Sending email notification to {customer_email}")
                    try:
                        notification_manager.send_email(
                            to_email=customer_email,
                            subject=email_subject,
                            body=personalized_body
                        )
                        # Sleep briefly to avoid email rate limiting
                        time.sleep(1)
                    except Exception as e:
                        print(f"Failed to send email to {customer_email}: {e}")
                else:
                    print(f"Skipping customer with no email: {customer}")
        else:
            print("No registered customers found to send email notifications.")
            try:
                notification_manager.send_whatsapp(message_body=sms_message)
            except Exception as e:
                print(f"WhatsApp also failed: {e}")
                print(f"MESSAGE THAT WOULD HAVE BEEN SENT: {sms_message}")

        # Email functionality is already handled in the try-except block above
        # No need for duplicate email handling code

print("Script completed.")
