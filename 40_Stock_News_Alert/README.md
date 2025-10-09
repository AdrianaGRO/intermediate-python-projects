# 📈 Stock News Alert System

A Python application that monitors stock price changes and sends SMS alerts with relevant news when significant price movements occur.

## 🚀 Features

- **Stock Price Monitoring**: Tracks daily stock prices using Alpha Vantage API
- **Smart Alerts**: Only sends notifications when price changes exceed 5%
- **News Integration**: Fetches relevant news articles using News API
- **SMS Notifications**: Sends formatted alerts via Twilio SMS
- **Customizable**: Easy to change stock symbols and thresholds

## 📱 How It Works

1. **Fetches Stock Data**: Gets yesterday's and day-before-yesterday's closing prices
2. **Calculates Change**: Computes percentage difference between the two days
3. **Triggers Alert**: If change > 5%, fetches news and sends SMS
4. **Sends Messages**: Delivers 3 formatted SMS messages with stock info and news

## 📋 Requirements

- Python 3.x
- Required packages:
  ```bash
  pip install requests python-dotenv twilio
  ```

## 🔧 Setup

1. **Clone/Download** this project

2. **Get API Keys**:
   - **Alpha Vantage**: Get free API key from [alphavantage.co](https://www.alphavantage.co/support/#api-key)
   - **News API**: Get free API key from [newsapi.org](https://newsapi.org/register)
   - **Twilio**: Sign up at [twilio.com](https://www.twilio.com/try-twilio) for SMS service

3. **Create `.env` file** with your credentials:
   ```env
   ALPHAVANTAGE_API_KEY=your_alpha_vantage_key_here
   NEWS_API_KEY=your_news_api_key_here
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=+1234567890
   MY_PHONE_NUMBER=+1234567890
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## ⚙️ Configuration

### Change Stock Symbol
Edit the constants in `main.py`:
```python
STOCK_NAME = "AAPL"  # Change to any stock symbol
COMPANY_NAME = "Apple Inc"  # Update company name for news search
```

### Adjust Alert Threshold
Modify the percentage threshold:
```python
if percentage_difference > 5:  # Change 5 to your preferred percentage
```

## 📱 Message Format

SMS messages include:
- Stock symbol with trend emoji (🔺 for up, 🔻 for down)
- Percentage change
- News headline (truncated to fit SMS limits)
- News description (truncated to fit SMS limits)

Example:
```
TSLA: 🔺6.25%
Tesla announces new factory in Texas...
Tesla Inc. has announced plans to build...
```

## 🔍 Testing

- **Test APIs**: Run `python test_apis.py` to verify API connections
- **Test Twilio**: Run `python test_twilio.py` to test SMS functionality
- **Lower Threshold**: Temporarily change `> 5` to `> 1` for testing

## 📊 Supported Stocks

Any stock symbol available on Alpha Vantage:
- TSLA (Tesla)
- AAPL (Apple)
- GOOGL (Google)
- MSFT (Microsoft)
- AMZN (Amazon)
- And many more...

## 🚨 Important Notes

- **API Limits**: Free tiers have daily request limits
- **SMS Costs**: Twilio charges for SMS messages (trial account includes credits)
- **International SMS**: Ensure your phone number is verified with Twilio
- **Message Length**: Messages are auto-truncated to fit SMS character limits

## 🔒 Security

- Keep your `.env` file private and never commit it to version control
- Add `.env` to your `.gitignore` file
- Use environment variables in production

## 📝 TODO Completed

- ✅ Get yesterday's closing stock price
- ✅ Get day before yesterday's closing stock price  
- ✅ Calculate positive difference
- ✅ Calculate percentage difference
- ✅ Trigger alerts when change > 5%
- ✅ Fetch news articles from News API
- ✅ Use slice operator for first 3 articles
- ✅ Create formatted messages with list comprehension
- ✅ Send SMS alerts via Twilio

## 🛠️ Future Enhancements

- Add support for multiple stocks
- Implement email notifications
- Create a web dashboard
- Add technical indicators
- Schedule automatic daily runs
- Add database for historical tracking

## 📄 License

This project is for educational purposes. Please respect API terms of service and usage limits.
