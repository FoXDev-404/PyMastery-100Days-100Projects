import requests
import time

response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
response.raise_for_status()  # Raise an error for bad responses

data = response.json()

longitude = data["longitude"]
latitude = data["latitude"]

print(f"ISS Current Location:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print(f"Timestamp: {time.ctime(data['timestamp'])}")
