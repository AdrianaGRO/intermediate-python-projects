"""
Price comparison tool - helps understand API vs real booking site prices
"""
import webbrowser
from datetime import datetime, timedelta
from config import Config

def compare_stockholm_prices():
    """Open multiple booking sites for Stockholm comparison"""
    print("🔍 Opening price comparison for Bucharest → Stockholm")
    print("📅 Date: Tomorrow (Oct 16, 2025)")
    print()
    
    # Stockholm booking URLs
    urls = {
        "Skyscanner": "https://www.skyscanner.com/transport/flights/OTP/ARN/2025-10-16/",
        "Kayak": "https://www.kayak.com/flights/OTP-ARN/2025-10-16",
        "Google Flights": "https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI1LTEwLTE2agcIARIDT1RQcgcIARIDARNQAFIAWgBcgIIAQ",
        "Momondo": "https://www.momondo.com/flight-search/OTP-ARN/2025-10-16",
        "Expedia": "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:OTP,to:ARN,departure:2025-10-16"
    }
    
    print("Opening booking sites for comparison:")
    for site, url in urls.items():
        print(f"🌐 {site}: {url}")
        try:
            webbrowser.open(url)
        except:
            print(f"   ❌ Could not open {site} automatically")
    
    print()
    print("💡 Price Comparison Tips:")
    print("• Check all sites as prices vary significantly")
    print("• Look for different airlines (Norwegian, SAS, Ryanair, etc.)")
    print("• Consider flexible dates (+/- 1-2 days)")
    print("• Clear browser cookies between searches")
    print("• Check for hidden fees before final booking")

def analyze_price_difference():
    """Analyze why API prices differ from booking sites"""
    print("📊 Why API Prices Differ from Booking Sites:")
    print("=" * 50)
    print()
    print("🔹 Test API Environment:")
    print("   • Uses cached/demo data, not live market prices")
    print("   • May show historical or promotional rates")
    print("   • Updated less frequently than booking sites")
    print()
    print("🔹 Dynamic Pricing:")
    print("   • Flight prices change every few minutes")
    print("   • Based on demand, competition, time of booking")
    print("   • Airlines adjust prices based on seat availability")
    print()
    print("🔹 Different Search Parameters:")
    print("   • API searches may use different filters")
    print("   • Booking sites include taxes, fees immediately")
    print("   • Different baggage/service inclusions")
    print()
    print("🔹 Market Reality Check:")
    print("   • €41 Bucharest→Stockholm is extremely low (60%+ below normal)")
    print("   • Typical prices: €80-150 for this route")
    print("   • Such deals occasionally exist but rare")
    print()
    print("💡 Recommendations:")
    print("✅ Use our tool to identify potentially good routes")
    print("✅ Always verify prices on 2-3 booking sites")
    print("✅ Set realistic expectations (API shows possibilities)")
    print("✅ Book quickly if you find a genuine low price")

def main():
    print("💰 Price Analysis Tool")
    print("=" * 30)
    print()
    print("Options:")
    print("1. Open Stockholm price comparison in browser")
    print("2. Analyze why API prices differ")
    print("3. Both")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        compare_stockholm_prices()
    elif choice == "2":
        analyze_price_difference()
    elif choice == "3":
        compare_stockholm_prices()
        print("\n" + "="*50 + "\n")
        analyze_price_difference()
    elif choice == "4":
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()