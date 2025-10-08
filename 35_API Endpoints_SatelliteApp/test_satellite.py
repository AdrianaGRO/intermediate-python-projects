
#this is a test to see if the notification email is sent when the ISS is close to the specified location
#The notification email should be sent only if the ISS is close to the specified location and it is night time


import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

# Check if it's night time

def is_night():
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
    sunrise_hour = (sunrise_hour + gmt_offset) % 24
    sunset_hour = (sunset_hour + gmt_offset) % 24
    print(f"Sunrise hour : {sunrise_hour}:{sunrise_minute}, Sunset hour : {sunset_hour}:{sunset_minute}")

    time_now = datetime.now()
    print(f"Current time: {time_now.hour}:{time_now.minute}")
    if time_now.hour >= sunset_hour or time_now.hour <= sunrise_hour:
        return True
    else:
        return False

#C (-49.5489, -101.0123)
test_lat = -49.5133
test_long = -101.0123
test_position = (test_lat, test_long)
print(f"Target position: {test_position}")

# Check ISS position and send email if conditions are met
def check_iss_and_notify():
    # Get current ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    
    if response.status_code == 200:
        data = response.json()
        longitude = data["iss_position"]["longitude"]
        latitude = data["iss_position"]["latitude"]
        iss_position = (float(latitude), float(longitude))
        print(f"Current ISS Position: {iss_position}")
        
        # Check if ISS is close to target position (within 5 degrees)
        if abs(iss_position[0] - test_position[0]) <= 5 and abs(iss_position[1] - test_position[1]) <= 5:
            print("The ISS is close to the test position!")
            
            # Check if it's night time
            if is_night():
                print("It's night time! Sending email notification...")
                # Send the email notification
                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                        connection.starttls()
                        connection.login(user=os.getenv("EMAIL_USER"), password=os.getenv("EMAIL_PASSWORD"))
                        connection.sendmail(
                            from_addr=os.getenv("EMAIL_USER"),
                            to_addrs=os.getenv("RECIPIENT_EMAIL"),
                            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
                        )
                    print("Email sent successfully!")
                    return True
                except Exception as e:
                    print(f"Failed to send email: {e}")
                    return False
            else:
                print("It's daytime. No email sent.")
                return False
        else:
            print("The ISS is not close to the test position.")
            print(f"Distance: Lat {abs(iss_position[0] - test_position[0]):.2f}°, Lng {abs(iss_position[1] - test_position[1]):.2f}°")
            return False
    else:
        print(f"Failed to get ISS position. Status code: {response.status_code}")
        return False

# Run the check
check_iss_and_notify()

