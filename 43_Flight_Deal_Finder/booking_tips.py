"""
Flight comparison helper - suggests alternative booking methods for better prices
"""

def get_budget_airline_suggestions(destination_city, destination_code):
    """Suggest budget airlines and direct booking sites for Romanian travelers"""
    
    budget_suggestions = {
        "Madrid": {
            "airlines": ["Ryanair", "Wizz Air", "Vueling"],
            "tips": "Check Ryanair from OTP, often has deals under 200 RON"
        },
        "Amsterdam": {
            "airlines": ["KLM", "Ryanair", "Wizz Air"],
            "tips": "KLM often has direct flights, Ryanair via secondary airports"
        },
        "London": {
            "airlines": ["Ryanair", "Wizz Air", "Blue Air"],
            "tips": "Ryanair to Stansted/Luton usually cheapest, Wizz Air to Luton"
        },
        "Istanbul": {
            "airlines": ["Turkish Airlines", "Pegasus", "AtlasGlobal"],
            "tips": "Turkish Airlines direct, Pegasus budget option"
        },
        "Athens": {
            "airlines": ["Aegean Airlines", "Ryanair", "Blue Air"],
            "tips": "Blue Air often has good deals, check Aegean for direct flights"
        },
        "Prague": {
            "airlines": ["Wizz Air", "Ryanair", "Czech Airlines"],
            "tips": "Wizz Air usually cheapest option from Bucharest"
        },
        "Tokyo": {
            "airlines": ["Turkish Airlines", "Lufthansa", "Austrian Airlines"],
            "tips": "Look for connecting flights via Istanbul, Frankfurt, or Vienna"
        }
    }
    
    city_upper = destination_city.upper()
    if city_upper in budget_suggestions or destination_city in budget_suggestions:
        suggestion = budget_suggestions.get(city_upper) or budget_suggestions.get(destination_city)
        return suggestion
    
    return {
        "airlines": ["Ryanair", "Wizz Air", "Blue Air"],
        "tips": "Check budget airlines directly for better prices"
    }

def print_booking_tips(destination_city, api_price_eur):
    """Print helpful booking tips for Romanian travelers"""
    suggestion = get_budget_airline_suggestions(destination_city, "")
    api_price_ron = api_price_eur * 4.97
    
    print(f"\n💡 BOOKING TIPS for {destination_city}:")
    print(f"   API Price: {api_price_eur:.2f} EUR (≈ {api_price_ron:.0f} RON)")
    print(f"   Recommended airlines: {', '.join(suggestion['airlines'])}")
    print(f"   Tip: {suggestion['tips']}")
    print(f"   📱 Also check: Google Flights, Skyscanner, eDreams")
    print(f"   🔍 Search tips: Be flexible with dates, check nearby airports")
    print()

def get_romanian_booking_sites():
    """Return list of popular booking sites used in Romania"""
    return [
        "https://www.skyscanner.ro",
        "https://www.momondo.ro", 
        "https://www.kayak.com",
        "https://www.edreams.ro",
        "https://www.google.com/flights",
        "Direct airline websites (often cheapest)"
    ]