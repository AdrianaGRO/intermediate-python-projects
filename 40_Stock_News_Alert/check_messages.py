import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

print("🔍 Checking recent messages...")

# Get recent messages
messages = client.messages.list(limit=5)

for message in messages:
    print(f"\n--- Message {message.sid} ---")
    print(f"From: {message.from_}")
    print(f"To: {message.to}")
    print(f"Status: {message.status}")
    print(f"Error Code: {message.error_code}")
    print(f"Error Message: {message.error_message}")
    print(f"Date: {message.date_created}")

print("\n🔍 Checking account info...")
account = client.api.accounts(os.getenv("TWILIO_ACCOUNT_SID")).fetch()
print(f"Account Status: {account.status}")
print(f"Account Type: {account.type}")