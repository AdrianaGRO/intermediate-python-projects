#Automated Birthday Email

# TODO 1: Update the birthdays.csv
# TODO 2: Check if today matches a birthday in the birthdays.csv
# TODO 3: If step 2 is true, pick a random letter from letter_templates
# TODO 4: Replace the [NAME] placeholder with the person's actual name from birthdays.csv
# TODO 5: Send the letter generated in step 4 to that person's email address.

import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import pandas as pd
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

# Email credentials
MY_EMAIL = os.getenv("EMAIL_USER")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get today's date
now = dt.datetime.now()
today_tuple = (now.month, now.day)

with open("birthdays.csv") as data_file:
    data = pd.read_csv(data_file)
    # Find all people with birthdays today
    todays_birthdays = data[(data["month"] == today_tuple[0]) & (data["day"] == today_tuple[1])]
    
    if not todays_birthdays.empty:
        print(f"🎉 Found {len(todays_birthdays)} birthday(s) today!")
        
        # Send email to each person with a birthday today
        for index, person in todays_birthdays.iterrows():
            try:
                print(f"\n📧 Processing birthday for: {person['name']} ({person['email']})")
                
                # Pick a random letter template for each person
                file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
                with open(file_path) as letter_file:
                    letter_contents = letter_file.read()
                    letter_contents = letter_contents.replace("[NAME]", person["name"])
                
                print("� Attempting to send email...")
                
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    print("🔐 Logging in to Gmail...")
                    connection.login(MY_EMAIL, MY_PASSWORD)
                    print("� Sending email...")
                    
                    # Create proper email message with UTF-8 encoding
                    msg = MIMEMultipart()
                    msg['From'] = MY_EMAIL
                    msg['To'] = person["email"]
                    msg['Subject'] = "Happy Birthday!"
                    
                    # Add body to email
                    msg.attach(MIMEText(letter_contents, 'plain', 'utf-8'))
                    
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=person["email"],
                        msg=msg.as_string()
                    )
                
                print(f"✅ Email sent successfully to {person['name']}!")
                
            except Exception as e:
                print(f"❌ Failed to send email to {person['name']}: {e}")
                print("🔧 Please check your email credentials and internet connection")
    else:
        print("No birthdays today.")



