import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use environment variables instead of hardcoded values
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Check if all required environment variables are set
if not all([api_key, account_sid, auth_token]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

weather_params = {
    "lat": 28.6139,  # New Delhi latitude
    "lon": 77.2090,  # New Delhi longitude
    "appid": api_key,
    "cnt": 4,
}

try:
    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        
        if int(condition_code) < 700:
            will_rain = True
            break

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid=os.getenv("TWILIO_MESSAGING_SERVICE_SID"),
            body='☔ Weather Alert: Rain is expected today! Don\'t forget your umbrella! 🌂',
            to=os.getenv("PHONE_NUMBER")
        )
        print(f"SMS sent successfully! Status: {message.status}")
    else:
        print("No rain expected today. No SMS sent.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except Exception as e:
    print(f"Error sending SMS: {e}")