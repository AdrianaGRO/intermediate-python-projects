import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Test Twilio configuration
print("🧪 Testing Twilio Configuration...")
print(f"Account SID: {os.getenv('TWILIO_ACCOUNT_SID')}")
print(f"From Number: {os.getenv('TWILIO_PHONE_NUMBER')}")
print(f"To Number: {os.getenv('MY_PHONE_NUMBER')}")

# Test sending a simple message
try:
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    
    message = client.messages.create(
        body="🧪 Test message from Stock Alert app!",
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("MY_PHONE_NUMBER")
    )
    
    print(f"✅ Test message sent successfully!")
    print(f"Message SID: {message.sid}")
    print(f"Status: {message.status}")
    
    # Let's also check the message status
    fetched_message = client.messages(message.sid).fetch()
    print(f"Message Status: {fetched_message.status}")
    print(f"Error Code: {fetched_message.error_code}")
    print(f"Error Message: {fetched_message.error_message}")
    
except Exception as e:
    print(f"❌ Error sending message: {e}")