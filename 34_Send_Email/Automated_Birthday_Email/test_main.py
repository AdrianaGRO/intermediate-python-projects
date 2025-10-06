#Automated Birthday Email - Test Version
import os
from dotenv import load_dotenv
import datetime as dt
import pandas as pd
import random

load_dotenv()

# Email credentials
MY_EMAIL = os.getenv("EMAIL_USER")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get today's date
now = dt.datetime.now()
today_tuple = (now.month, now.day)
print(f"Today's date: {now.month}/{now.day}")

with open("birthdays.csv") as data_file:
    data = pd.read_csv(data_file)
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
    print(f"Found {len(birthdays_dict)} birthdays in the CSV file")
    
    if today_tuple in birthdays_dict:
        birthdays_data = birthdays_dict[today_tuple]
        print(f"🎉 It's {birthdays_data['name']}'s birthday today!")
        
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        print(f"Using template: {file_path}")
        
        with open(file_path) as letter_file:
            letter_contents = letter_file.read()
            letter_contents = letter_contents.replace("[NAME]", birthdays_data["name"])
        
        print(f"Email would be sent to: {birthdays_data['email']}")
        print("Email content:")
        print("-" * 50)
        print(f"Subject: Happy Birthday!")
        print()
        print(letter_contents)
        print("-" * 50)
        print("✅ Test completed successfully! File paths are working correctly.")
    else:
        print("No birthdays today.")