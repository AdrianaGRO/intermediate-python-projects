"""
Main application - City Break Deal Monitor from Bucharest (OTP)
Clean, modular architecture with separate classes for each responsibility.
"""
from deal_finder import DealFinder
from alert_manager import AlertManager
from config import Config


def main():
    """Main function to run the deal monitor"""
    print("🇷🇴 City Break Deal Monitor - Departing from Bucharest (OTP)")
    print("=" * 60)
    
    # Initialize services
    deal_finder = DealFinder()
    alert_manager = AlertManager()
    
    try:
        # Find today's deals
        deals_summary = deal_finder.find_daily_deals()
        
        # Create alerts if deals found
        if deals_summary['flight_deals'] or deals_summary['hotel_deals']:
            alert_manager.create_alert(deals_summary)
        else:
            print("\n❌ No deals found today within our price limits")
            print(f"💰 Flight limit: €{Config.MAX_FLIGHT_PRICE}")
            print(f"🏨 Hotel limit: €{Config.MAX_HOTEL_PRICE}")
    
    except KeyboardInterrupt:
        print("\n⚠️  Search interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running deal monitor: {e}")
    
    print("\n✅ Deal monitoring complete!")


if __name__ == "__main__":
    main()