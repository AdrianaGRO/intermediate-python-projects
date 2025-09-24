"""
Simple News Email Automation
Fetches news and sends emails to people based on their interests
"""

import requests
import yagmail
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_news(topic, date="2025-09-23"):
    """Get news articles for a specific topic."""
    api_key = os.getenv('NEWS_API_KEY')
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={date}&language=en&sortBy=publishedAt&apiKey={api_key}"
    
    response = requests.get(url)
    articles = response.json()['articles']
    
    # Format news content
    content = f"📰 Latest {topic.upper()} News:\n\n"
    for i, article in enumerate(articles[:3], 1):  # Only top 3 articles
        content += f"{i}. {article['title']}\n"
        content += f"   {article['description']}\n"
        content += f"   Read more: {article['url']}\n\n"
    
    return content

def send_email(to_email, subject, content):
    """Send email to one person."""
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    
    try:
        # Create email connection and send
        email = yagmail.SMTP(user=email_user, password=email_password)
        email.send(to=to_email, subject=subject, contents=content)
        print(f"✅ Email sent to {to_email}")
        return True
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")
        return False

def main():
    """Main function - does everything!"""
    print("🚀 Starting Simple News Emailer")
    print("=" * 40)
    
    # 1. Load people from Excel
    try:
        df = pd.read_excel('people.xlsx')
        print(f"📊 Loaded {len(df)} people from Excel")
    except Exception as e:
        print(f"❌ Error loading Excel: {e}")
        return
    
    # 2. Send personalized emails
    for _, person in df.iterrows():
        name = person['name']
        email = person['email']
        interest = person['interest']
        
        print(f"\n📧 Preparing email for {name} ({interest} news)")
        
        # Get news for their interest
        news_content = get_news(interest)
        
        # Create personalized email
        subject = f"🗞️ Your {interest.title()} News Update"
        email_body = f"""
Hi {name}!

Hope you're doing well! Here's your personalized news update:

{news_content}

Have a great day!
Your News Bot 🤖
        """
        
        # Send the email
        send_email(email, subject, email_body)
    
    print("\n🎉 All done!")

if __name__ == "__main__":
    main()