import os
import requests
import datetime

# Load sensitive data from environment variables
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
EXERCISE_ENDPOINT = os.getenv("EXERCISE_ENDPOINT")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
GENDER = os.getenv("GENDER", "male")
WEIGHT_KG = float(os.getenv("WEIGHT_KG", 72))
HEIGHT_CM = float(os.getenv("HEIGHT_CM", 175))
AGE = int(os.getenv("AGE", 21))

query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

sheety_headers = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json"
}

for exercise in result.get("exercises", []):
    print(f"Exercise: {exercise['name']}")
    print(f"Duration: {exercise['duration_min']} min")
    print(f"Calories: {exercise['nf_calories']}")
    print()

    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
    print(sheety_response.text)