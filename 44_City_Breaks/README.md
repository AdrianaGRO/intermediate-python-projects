# City Break Deal Monitor 🏖️

A modular Python application that monitors flight and hotel prices daily from Bucharest (OTP) and alerts you when great deals are found.

## What It Does

- **Daily Monitoring**: Checks for flight and hotel deals automatically
- **Price Alerts**: Notifies when prices drop below your configured targets
- **Smart Rotation**: Rotates through different European city categories daily
- **Multiple Destinations**: Tracks flights from Bucharest to cities across Europe
- **Configurable Limits**: Set your own price thresholds for flights and hotels

## Quick Setup

### 1. Get API Keys (Free)
- **Amadeus**: [developers.amadeus.com](https://developers.amadeus.com) (2,000 calls/month free)
- **RapidAPI**: [rapidapi.com](https://rapidapi.com) (Booking.com API)

### 2. Configure
Add your keys to `.env`:
```
AMADEUS_CLIENT_ID=your_client_id
AMADEUS_CLIENT_SECRET=your_client_secret  
RAPIDAPI_KEY=your_rapidapi_key
```

### 3. Install & Run
```bash
pip install -r requirements.txt
python3 main_clean.py
```


## Daily Automation

Set up daily monitoring at 9 AM:
```bash
chmod +x run_daily_deals.sh
crontab -e
# Add: 0 9 * * * /path/to/run_daily_deals.sh
```

## Files Created

- `deals_alerts.json` - All deals found
- `todays_deals.html` - Email-ready alerts with deal details
