import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv()

# Email credentials
MY_EMAIL = os.getenv("EMAIL_USER")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

#open the file

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    one_quote = random.choice(all_quotes)
    print(one_quote)
    
monday_quote = 0
if dt.datetime.now().weekday() == monday_quote:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="adriana.gropan@gmail.com",
        msg="Subject:Your Motivational Quote\n\n" + one_quote
    )

print("Email sent!")

