"""
Alert system for deal notifications
"""
import json
from datetime import datetime
from pathlib import Path


class AlertManager:
    """Handle deal alerts and notifications"""
    
    def __init__(self):
        self.alerts_file = Path("deals_alerts.json")
        self.html_file = Path("todays_deals.html")
    
    def create_alert(self, deals_summary):
        """Create and save deal alert"""
        if not deals_summary['flight_deals'] and not deals_summary['hotel_deals']:
            print("❌ No deals found today")
            return False
        
        # Save to JSON
        self._save_to_json(deals_summary)
        
        # Generate HTML alert
        self._generate_html_alert(deals_summary)
        
        # Print console summary
        self._print_console_summary(deals_summary)
        
        return True
    
    def _save_to_json(self, deals_summary):
        """Save deals to JSON file"""
        try:
            # Load existing alerts
            alerts_history = []
            if self.alerts_file.exists():
                with open(self.alerts_file, 'r') as f:
                    alerts_history = json.load(f)
            
            # Add today's deals
            alerts_history.append(deals_summary)
            
            # Keep only last 30 days
            alerts_history = alerts_history[-30:]
            
            # Save back
            with open(self.alerts_file, 'w') as f:
                json.dump(alerts_history, f, indent=2, default=str)
            
            print(f"💾 Deals saved to {self.alerts_file}")
            
        except Exception as e:
            print(f"❌ Error saving to JSON: {e}")
    
    def _generate_html_alert(self, deals_summary):
        """Generate HTML alert page"""
        try:
            html_content = self._build_html_content(deals_summary)
            
            with open(self.html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"📄 HTML alert generated: {self.html_file}")
            
        except Exception as e:
            print(f"❌ Error generating HTML: {e}")
    
    def _build_html_content(self, deals_summary):
        """Build HTML content for the alert"""
        cheapest_flight = deals_summary.get('cheapest_flight')
        cheapest_hotel = deals_summary.get('cheapest_hotel')
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Today's Travel Deals from Bucharest</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; }}
        .header {{ text-align: center; color: #2c3e50; margin-bottom: 30px; }}
        .highlight {{ background-color: #e8f5e9; padding: 15px; border-radius: 8px; margin: 20px 0; }}
        .deal-section {{ margin: 20px 0; }}
        .deal-item {{ background: #f8f9fa; padding: 10px; margin: 5px 0; border-left: 4px solid #007bff; }}
        .price {{ color: #28a745; font-weight: bold; font-size: 1.2em; }}
        .airline {{ color: #6c757d; }}
        .cheapest {{ background-color: #fff3cd; border-color: #ffc107; }}
        .warning {{ background-color: #f8d7da; border: 1px solid #f5c6cb; padding: 10px; border-radius: 5px; margin: 15px 0; color: #721c24; }}
        .api-note {{ font-size: 0.9em; color: #6c757d; font-style: italic; }}
        .stats {{ text-align: center; color: #6c757d; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏛️  Today's Travel Deals from Bucharest</h1>
            <p>📅 {deals_summary['date']} | 🌍 {deals_summary['category'].replace('_', ' ').title()} Destinations</p>
        </div>
        
        <div class="warning">
            ⚠️  <strong>Price Accuracy Notice:</strong><br>
            • API prices are from test environment and may not reflect current market rates<br>
            • Always verify final prices on booking sites as they change dynamically<br>
            • Use these results as deal indicators, not final booking prices<br>
            • Check multiple booking platforms for best rates and terms
        </div>
        """
        
        # Add cheapest offers highlight
        if cheapest_flight or cheapest_hotel:
            html += '<div class="highlight"><h2>🏆 TODAY\'S CHEAPEST OFFERS:</h2>'
            
            if cheapest_flight:
                booking_links = cheapest_flight.get('booking_link', {})
                html += f'''
                <div class="cheapest">
                    ✈️  <strong>Flight:</strong> €{cheapest_flight['price']} to {cheapest_flight['destination']} 
                    ({cheapest_flight['airline']})<br>
                    <div style="margin-top: 10px;">
                        <a href="{booking_links.get('skyscanner', '#')}" target="_blank" style="margin-right: 10px; padding: 5px 10px; background: #007bff; color: white; text-decoration: none; border-radius: 3px;">📱 Skyscanner</a>
                        <a href="{booking_links.get('kayak', '#')}" target="_blank" style="margin-right: 10px; padding: 5px 10px; background: #ff6b35; color: white; text-decoration: none; border-radius: 3px;">🔍 Kayak</a>
                        <a href="{booking_links.get('google_flights', '#')}" target="_blank" style="padding: 5px 10px; background: #4285f4; color: white; text-decoration: none; border-radius: 3px;">✈️  Google Flights</a>
                    </div>
                </div>
                '''
            
            if cheapest_hotel:
                hotel_links = cheapest_hotel.get('booking_links', {})
                html += f'''
                <div class="cheapest">
                    🏨 <strong>Hotel:</strong> €{cheapest_hotel['price']} - {cheapest_hotel['name']} 
                    in {cheapest_hotel['city']}<br>
                    <div style="margin-top: 10px;">
                        <a href="{hotel_links.get('booking_com', '#')}" target="_blank" style="margin-right: 10px; padding: 5px 10px; background: #003580; color: white; text-decoration: none; border-radius: 3px;">🏨 Booking.com</a>
                        <a href="{hotel_links.get('hotels_com', '#')}" target="_blank" style="margin-right: 10px; padding: 5px 10px; background: #c41e3a; color: white; text-decoration: none; border-radius: 3px;">🏩 Hotels.com</a>
                        <a href="{hotel_links.get('expedia', '#')}" target="_blank" style="padding: 5px 10px; background: #ffc72c; color: black; text-decoration: none; border-radius: 3px;">✈️  Expedia</a>
                    </div>
                </div>
                '''
            
            html += '</div>'
        
        # Flight deals section
        if deals_summary['flight_deals']:
            html += '<div class="deal-section"><h2>✈️  Flight Deals</h2>'
            
            # Group by destination
            destinations = {}
            for deal in deals_summary['flight_deals']:
                dest = deal['destination']
                if dest not in destinations:
                    destinations[dest] = []
                destinations[dest].append(deal)
            
            for dest, deals in destinations.items():
                html += f'<h3>{dest} ({len(deals)} deals)</h3>'
                for deal in deals[:3]:  # Show top 3 per destination
                    booking_links = deal.get('booking_link', {})
                    html += f'''
                    <div class="deal-item">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span class="price">€{deal['price']}</span> - 
                                <span class="airline">{deal['airline']}</span><br>
                                <span class="api-note">⚠️  API price - verify on booking sites</span>
                            </div>
                            <div>
                                <a href="{booking_links.get('skyscanner', '#')}" target="_blank" style="margin-right: 5px; padding: 3px 8px; background: #007bff; color: white; text-decoration: none; border-radius: 3px; font-size: 0.8em;">Skyscanner</a>
                                <a href="{booking_links.get('kayak', '#')}" target="_blank" style="margin-right: 5px; padding: 3px 8px; background: #ff6b35; color: white; text-decoration: none; border-radius: 3px; font-size: 0.8em;">Kayak</a>
                                <a href="{booking_links.get('google_flights', '#')}" target="_blank" style="padding: 3px 8px; background: #4285f4; color: white; text-decoration: none; border-radius: 3px; font-size: 0.8em;">Google</a>
                            </div>
                        </div>
                    </div>
                    '''
            
            html += '</div>'
        
        # Hotel deals section
        if deals_summary['hotel_deals']:
            html += '<div class="deal-section"><h2>🏨 Hotel Deals</h2>'
            
            # Group by city
            cities = {}
            for deal in deals_summary['hotel_deals']:
                city = deal['city']
                if city not in cities:
                    cities[city] = []
                cities[city].append(deal)
            
            for city, deals in cities.items():
                html += f'<h3>{city} ({len(deals)} deals)</h3>'
                for deal in deals[:3]:  # Show top 3 per city
                    hotel_links = deal.get('booking_links', {})
                    html += f'''
                    <div class="deal-item">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <strong>{deal['name']}</strong><br>
                                <span class="price">€{deal['price']}</span>/night - 
                                Rating: {deal['rating']}/10
                            </div>
                            <div>
                                <a href="{hotel_links.get('booking_com', '#')}" target="_blank" style="margin-right: 5px; padding: 3px 8px; background: #003580; color: white; text-decoration: none; border-radius: 3px; font-size: 0.8em;">Booking</a>
                                <a href="{hotel_links.get('hotels_com', '#')}" target="_blank" style="margin-right: 5px; padding: 3px 8px; background: #c41e3a; color: white; text-decoration: none; border-radius: 3px; font-size: 0.8em;">Hotels</a>
                                <a href="{hotel_links.get('expedia', '#')}" target="_blank" style="padding: 3px 8px; background: #ffc72c; color: black; text-decoration: none; border-radius: 3px; font-size: 0.8em;">Expedia</a>
                            </div>
                        </div>
                    </div>
                    '''
            
            html += '</div>'
        
        # Stats footer
        html += f'''
        <div class="stats">
            📊 Searched with {deals_summary['total_requests']} API requests<br>
            Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </div>
    </div>
</body>
</html>
        '''
        
        return html
    
    def _print_console_summary(self, deals_summary):
        """Print summary to console"""
        print(f"\n🎉 DEALS FOUND!")
        print(f"📊 Summary: {len(deals_summary['flight_deals'])} flights, {len(deals_summary['hotel_deals'])} hotels")
        
        if deals_summary['cheapest_flight']:
            cf = deals_summary['cheapest_flight']
            print(f"✈️  Cheapest Flight (API): €{cf['price']} to {cf['destination']} ({cf['airline']})")
            print(f"   ⚠️  Note: API prices from test environment - verify current rates on booking sites")
        
        if deals_summary['cheapest_hotel']:
            ch = deals_summary['cheapest_hotel']
            print(f"🏨 Cheapest Hotel (API): €{ch['price']} - {ch['name']} in {ch['city']}")
        
        print(f"📄 Check {self.html_file} for detailed view with booking links")