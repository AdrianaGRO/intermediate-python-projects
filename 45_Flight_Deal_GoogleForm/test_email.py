import os
from dotenv import load_dotenv
from notification_manager import NotificationManager

# Load environment variables
load_dotenv()

def test_email_functionality():
    """Test the email functionality in NotificationManager"""
    
    # Initialize the notification manager
    notification_manager = NotificationManager()
    
    # Check if email credentials are available
    if not notification_manager.email_enabled:
        print("Email credentials not properly loaded from .env file")
        return
    
    print("Email credentials loaded successfully")
    
    # Test sending an email
    test_recipient = os.getenv("EMAIL_USER")  # Send to yourself for testing
    
    if not test_recipient:
        print("No test recipient email available")
        return
    
    print(f"Attempting to send a test email to {test_recipient}")
    
    try:
        # Create a test email with a flight deal format and a link
        test_subject = "Flight Deals - Test Email with Clickable Link"
        test_body = """Low price alert! Only £199 to fly from OTP to MAD, on 2025-10-20 until 2025-10-27.
Direct flight.

Book here: https://www.google.ro/flights?hl=en#flt=OTP.MAD.2025-10-20*MAD.OTP.2025-10-27"""
        
        success = notification_manager.send_email(
            to_email=test_recipient,
            subject=test_subject,
            body=test_body
        )
        
        if success:
            print("Test email sent successfully!")
        else:
            print("Failed to send test email")
            
    except Exception as e:
        print(f"Error occurred while sending test email: {e}")

if __name__ == "__main__":
    test_email_functionality()