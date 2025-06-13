import requests

APP_ID = "d34cea13"
API_KEY = "a20b9a419d2503535242e9b884177b00"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": query,
    "gender": "male",  # or "female"
    "weight_kg": 72,
    "height_cm": 175,
    "age": 21
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

for exercise in result.get("exercises", []):
    print(f"Exercise: {exercise['name']}")
    print(f"Duration: {exercise['duration_min']} min")
    print(f"Calories: {exercise['nf_calories']}")
    print()