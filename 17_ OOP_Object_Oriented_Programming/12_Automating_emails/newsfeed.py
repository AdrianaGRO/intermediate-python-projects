import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class NewsFeeds:
    
    """Representing news feed fetching based on interest, date, and language."""
    base_url = "https://newsapi.org/v2/everything"
    
    def __init__(self, interest, from_date="2025-09-01", language="en"):
        self.interest = interest
        self.from_date = from_date
        self.language = language
        

    def get_news(self):
        
        api_key = os.getenv('NEWS_API_KEY')

        url = f"{NewsFeeds.base_url}?qInTitle={self.interest}&from={self.from_date}&language={self.language}&sortBy=publishedAt&apiKey={api_key}"
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_content = ""
        for article in articles:
            email_content += f"Title: {article['title']}\n"
            email_content += f"Description: {article['description']}\n"
            email_content += f"URL: {article['url']}\n"
            email_content += "\n"

        return email_content


class EmailSender:
    """Class to handle email sending functionality."""
    
    def __init__(self):
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.email_connection = None
    
    def create_connection(self):
        """Create SMTP connection."""
        import yagmail
        self.email_connection = yagmail.SMTP(user=self.email_user, password=self.email_password)
        print("Email connection established successfully")
        return True
    
    def send_email(self, to_email, subject, content):
        """Send email to recipient."""
        if not self.email_connection:
            self.create_connection()
        
        self.email_connection.send(
            to=to_email,
            subject=subject,
            contents=content
        )
        print(f"Email sent successfully to {to_email}")
        return True


# Example usage (only for testing the classes directly)
if __name__ == "__main__":
    # Test the NewsFeeds class
    print("Testing NewsFeeds class...")
    news_feed = NewsFeeds(interest="python", from_date="2025-09-23", language="en")
    news_content = news_feed.get_news()
    print(f"Found {len(news_content.split('Title:')) - 1} articles")
    print(news_content[:200] + "...")  # Show first 200 characters

