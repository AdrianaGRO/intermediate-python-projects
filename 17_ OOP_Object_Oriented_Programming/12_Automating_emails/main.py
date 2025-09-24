# ============================================================================
# EMAIL AUTOMATION SYSTEM
# ============================================================================

# IMPORTS
import yagmail
import os
from dotenv import load_dotenv
import pandas as pd
from newsfeed import NewsFeeds

# ============================================================================
# CONFIGURATION
# ============================================================================

# Load environment variables from .env file
load_dotenv()

# Email configuration using environment variables
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# File paths
EXCEL_FILE_PATH = "/Users/adricati/Personal Development/intermediate-python-projects/17_ OOP_Object_Oriented_Programming/12_Automating_emails/people.xlsx"

# ============================================================================
# EMAIL FUNCTIONS
# ============================================================================

def load_email_list():
    """Load email addresses from Excel file."""
    df = pd.read_excel(EXCEL_FILE_PATH)
    email_list = df["email"].tolist()
    print(f"Loaded {len(email_list)} email addresses")
    return email_list

def create_email_connection():
    """Create and return SMTP connection."""
    email_connection = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD)
    print("Email connection established successfully")
    return email_connection

def send_email(email_connection, to_email, subject, content):
    """Send email to a specific recipient."""
    email_connection.send(
        to=to_email,
        subject=subject,
        contents=content
    )
    print(f"Email sent successfully to {to_email}")
    return True

def send_bulk_emails(email_list, subject, content):
    """Send emails to multiple recipients."""
    email_connection = create_email_connection()
    
    success_count = 0
    for email_address in email_list:
        if send_email(email_connection, email_address, subject, content):
            success_count += 1
    
    print(f"Successfully sent {success_count}/{len(email_list)} emails")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("🚀 Starting Personalized News Email System")
    print("=" * 50)
    
    # Load people with their interests
    df = pd.read_excel(EXCEL_FILE_PATH)
    print(f"📊 Loaded {len(df)} people from Excel")
    
    # Create email connection
    email_connection = create_email_connection()
    
    # Send personalized emails to each person
    for _, person in df.iterrows():
        name = person['name']
        email = person['email']
        interest = person['interest']
        
        print(f"\n📧 Preparing email for {name} ({interest} news)")
        
        # Get news for their specific interest using NewsFeeds class
        news_feed = NewsFeeds(interest=interest, from_date="2025-09-23", language="en")
        news_content = news_feed.get_news()
        
        # Create personalized email
        subject = f"🗞️ Your {interest.title()} News Update"
        content = f"""
        Hi {name}!
        
        Hope you're doing well! Here's your personalized news update:
        
        {news_content}
        
        Have a great day!
        Your News Bot from PyArch 🤖
        """
        
        # Send the personalized email
        send_email(email_connection, email, subject, content)
    
    print("\n🎉 All personalized emails sent!")

