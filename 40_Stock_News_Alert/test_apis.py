import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_alpha_vantage():
    """Test Alpha Vantage API"""
    print("🧪 Testing Alpha Vantage API...")
    
    api_key = os.getenv('ALPHAVANTAGE_API_KEY')
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSLA",
        "apikey": api_key
    }
    
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        if "Error Message" in data:
            print(f"❌ Error: {data['Error Message']}")
        elif "Note" in data:
            print(f"⚠️ API Limit: {data['Note']}")
        else:
            print("✅ Alpha Vantage API working!")
            print(f"Available keys: {list(data.keys())}")
    else:
        print(f"❌ Request failed with status {response.status_code}")

def test_news_api():
    """Test News API"""
    print("\n🧪 Testing News API...")
    
    api_key = os.getenv('NEWS_API_KEY')
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "Tesla",
        "apiKey": api_key,
        "pageSize": 3
    }
    
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'ok':
            print("✅ News API working!")
            print(f"Total articles found: {data.get('totalResults')}")
            print(f"Articles returned: {len(data.get('articles', []))}")
        else:
            print(f"❌ News API Error: {data.get('message')}")
    else:
        print(f"❌ Request failed with status {response.status_code}")

if __name__ == "__main__":
    test_alpha_vantage()
    test_news_api()