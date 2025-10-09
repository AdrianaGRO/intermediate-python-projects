import requests
import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client  


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
TEST_PERCENTAGE = 10

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv("ALPHAVANTAGE_API_KEY")
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()
daily_data = data["Time Series (Daily)"]
dates = list(daily_data.keys())
yesterday_date =dates[0]
yesterday_closing_price = daily_data[yesterday_date]["4. close"]
print(f"Yesterday ({yesterday_date}) : {yesterday_closing_price} USD closing price")

day_before_yesterday_date = dates[1]
day_before_yesterday_closing_price = daily_data[day_before_yesterday_date]["4. close"]
print(f"Day before yesterday ({day_before_yesterday_date}) : {day_before_yesterday_closing_price} USD closing price")


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
percentage_difference = (difference / float(yesterday_closing_price)) * 100
print(f"Percentage difference: {percentage_difference:.2f}%")


if percentage_difference > 5:
    params = {
        "q": COMPANY_NAME,
        "apiKey": os.getenv("NEWS_API_KEY"),
        "pageSize": 3
    }
    
    response = requests.get(NEWS_ENDPOINT, params=params)
    news_data = response.json()
    articles = news_data.get('articles', [])
    
    first_three_articles = articles[:3]
    
    print(f"\nFound {len(articles)} articles, showing first 3:")
    for i,article in enumerate(first_three_articles, 1):
        print(f"\n--- Article {i} ---")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")

    
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN") )
    messages = [f"TSLA: {'🔺' if float(yesterday_closing_price) > float(day_before_yesterday_closing_price) else '🔻'}{percentage_difference:.2f}%\n{article['title'][:60]}...\n{article['description'][:80]}..." for article in first_three_articles]
    from_number = os.getenv("TWILIO_PHONE_NUMBER")
    to_number = os.getenv("MY_PHONE_NUMBER")
    for message in messages:
        sent_message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"Message sent with SID: {sent_message.sid}")


