import requests

from datetime import datetime


MY_LAT = 44.4268
MY_LONG = 26.1025

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"Sunrise: {sunrise}, Sunset: {sunset}")
sunrise_hour = int(sunrise.split("T")[1][0:2])
sunset_hour = int(sunset.split("T")[1][0:2])
sunrise_minute = int(sunrise.split("T")[1][3:5])
sunset_minute = int(sunset.split("T")[1][3:5])

# Adjusting for GMT+3 (Bucharest time)
gmt_offset = 3
sunrise_hour += gmt_offset
sunset_hour += gmt_offset
print(f"Sunrise hour : {sunrise_hour}:{sunrise_minute}, Sunset hour : {sunset_hour}:{sunset_minute}")

time_now = datetime.now()
print(time_now.hour)