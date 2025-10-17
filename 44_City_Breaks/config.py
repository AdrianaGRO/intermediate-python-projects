"""
Configuration settings for the City Break Deal Monitor
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class for API keys and settings"""
    
    # API Keys
    AMADEUS_CLIENT_ID = os.getenv('AMADEUS_CLIENT_ID')
    AMADEUS_CLIENT_SECRET = os.getenv('AMADEUS_CLIENT_SECRET')
    RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
    
    # Default settings
    DEPARTURE_CITY = 'OTP'  # Bucharest (Otopeni)
    DEPARTURE_CITY_NAME = 'Bucharest'
    
    # API Environment (set to False for production API with real prices)
    USE_TEST_API = True  # True = test API (may have cached prices), False = production API
    
    # Price limits
    MAX_FLIGHT_PRICE = 120
    MAX_HOTEL_PRICE = 180
    
    # API limits
    MAX_API_REQUESTS = 15
    REQUEST_DELAY = 1.5
    
    # European cities with airport codes
    EUROPEAN_DESTINATIONS = {
        # Western Europe
        'paris': 'CDG',
        'amsterdam': 'AMS',
        'bruges': 'BRU',
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
        'pisa': 'PSA',
        
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
        
        # Southern Europe - Other
        'dubrovnik': 'DBV',
        'split': 'SPU',
        'kotor': 'TGD',
        'istanbul': 'IST',
        
        # Central Europe
        'prague': 'PRG',
        'vienna': 'VIE',
        'budapest': 'BUD',
        'salzburg': 'SZG',
        'munich': 'MUC',
        'berlin': 'BER',
        'zurich': 'ZUR',
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
        'sofia': 'SOF',
        'belgrade': 'BEG'
    }
    
    # City groups for daily rotation
    CITY_GROUPS = {
        'iconic': ['paris', 'london', 'rome', 'barcelona', 'amsterdam'],
        'eastern_gems': ['prague', 'budapest', 'vienna', 'krakow', 'warsaw'],
        'mediterranean': ['athens', 'dubrovnik', 'florence', 'lisbon', 'valencia'],
        'nordic': ['copenhagen', 'stockholm', 'helsinki', 'oslo'],
        'cultural': ['istanbul', 'brussels', 'munich', 'zurich', 'edinburgh']
    }