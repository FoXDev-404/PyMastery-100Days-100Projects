import requests

# Use the free OpenWeatherMap API endpoint instead of the pro version
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key

weather_params = {
    "lat": 28.6419372696918,  # Replace with your latitude
    "lon": 77.20893327205839,  # Replace with your longitude
    "appid": api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()  # Raise an error for bad responses
weather_data = response.json()
print(weather_data)  
