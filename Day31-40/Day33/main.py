import requests
from datetime import datetime
import pytz
# import time

# response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
# response.raise_for_status()  # Raise an error for bad responses

# data = response.json()

# longitude = data["longitude"]
# latitude = data["latitude"]

# print(f"ISS Current Location:")
# print(f"Latitude: {latitude}")
# print(f"Longitude: {longitude}")
# print(f"Timestamp: {time.ctime(data['timestamp'])}")


# 🌅 Sunrise and Sunset Times in IST (Indian Standard Time)
def get_sunrise_sunset_ist(lat, lng):
    url = "https://api.sunrise-sunset.org/json"
    params = {
        "lat": lat,
        "lng": lng,
        "formatted": 0  # Get ISO 8601 format
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Get ISO 8601 strings
    sunrise_utc = data["results"]["sunrise"]
    sunset_utc = data["results"]["sunset"]

    # Convert to datetime objects (with UTC timezone)
    utc = pytz.utc
    ist = pytz.timezone("Asia/Kolkata")

    sunrise_time = datetime.fromisoformat(sunrise_utc).astimezone(ist)
    sunset_time = datetime.fromisoformat(sunset_utc).astimezone(ist)

    # Return formatted strings
    return sunrise_time.strftime("%H:%M"), sunset_time.strftime("%H:%M")


# 🎯 Example: New Delhi
latitude = 28.6419372696918
longitude = 77.20893327205839

sunrise, sunset = get_sunrise_sunset_ist(latitude, longitude)

print(f"🌅 Sunrise (IST): {sunrise}")
print(f"🌇 Sunset (IST): {sunset}")
