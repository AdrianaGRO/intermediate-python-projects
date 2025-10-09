import requests
import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client

API_KEY = os.getenv("Open_Weather_API_Key")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)    

Bucharest_lat = 44.4268
Bucharest_lon = 26.1025 

params = {
    "lat": Bucharest_lat,
    "lon": Bucharest_lon,
    "appid": API_KEY,
    "cnt": 4
}

url = f"http://api.openweathermap.org/data/2.5/forecast?lat={params['lat']}&lon={params['lon']}&appid={params['appid']}"
response = requests.get(url)
response.raise_for_status()
data = response.json()

#Take the dt_text for the next 12 hours

dt_text = []
hourly_data = data["list"][:12]
for hour in hourly_data:
    dt_text.append(hour["dt_txt"])

#Weather condition codes
weather_id = []
for hour in hourly_data:
    condition_code = hour["weather"][0]["id"]
    weather_id.append(condition_code)
#Set up if will rain or not
will_rain = False
for condition in weather_id:
    if condition < 700:
        will_rain = True    

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Adriana, it's going to rain today. Remember to bring an ☔️",
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("MY_PHONE_NUMBER")
    )
    print("SMS sent successfully!")
    print(message.sid)