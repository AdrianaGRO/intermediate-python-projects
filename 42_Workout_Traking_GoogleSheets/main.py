from datetime import datetime
import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

#Api endpoint Nutritionix
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_NUTRIENTS_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/nutrients"

params_nutritionix = {
    "query": input("Tell me which exercises you did: "),
    "gender": "female",
    "weight_kg": 62,
    "height_cm": 173,
    "age": 39
}

# params_nutritionix_nutrients = {
#     "query": input("Tell me which food you ate: ")
# }   

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
response = requests.post(NUTRITIONIX_ENDPOINT, json=params_nutritionix, headers=headers)
response.raise_for_status()
result = response.json()
exercises = result["exercises"]
print(exercises)
# response_nutrients = requests.post(NUTRITIONIX_NUTRIENTS_ENDPOINT, json=params_nutritionix_nutrients, headers=headers)
# response_nutrients.raise_for_status()
# result_nutrients = response_nutrients.json()
# foods = result_nutrients["foods"]
# print(foods)

# Sheety headers with authentication
sheety_headers = {
    "Authorization": f"Basic {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

now = datetime.now()
date = now.strftime("%Y-%m-%d")  # More readable date format
time = now.strftime("%H:%M:%S")  # Add time in HH:MM:SS format


for exercise in exercises:
    sheets_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response_sheety = requests.post(SHEETY_ENDPOINT, json=sheets_inputs, headers=sheety_headers)
    print(response_sheety.text)
    response_sheety.raise_for_status()
    print("Workout logged successfully.")
result_sheety = response_sheety.json()
print(result_sheety)