# Configuration for Flight Deal Finder

# Bucharest Airport Codes
ORIGIN_CITY_IATA = "OTP"  # Henri Coandă International Airport (main airport)
# Alternative options:
# "BUH" - All Bucharest airports
# "BBU" - Băneasa Airport

# API Rate Limiting Settings
MAX_API_CALLS_PER_MINUTE = 5
WAIT_BETWEEN_SEARCHES = 3  # seconds

# Flight Search Settings
SEARCH_DAYS_AHEAD = 1  # Start searching from tomorrow
SEARCH_WINDOW_MONTHS = 6  # Search up to 6 months ahead
MAX_PASSENGERS = 2

# Deal Alert Settings
SEND_SMS_ALERTS = False  # Set to True when SMS is configured
SEND_EMAIL_ALERTS = True  # Set to True when email is configured

# Romanian specific settings
HOME_CITY = "Bucharest"
HOME_COUNTRY = "Romania"
CURRENCY = "EUR"  # Keeping prices in EUR as returned by flight APIs