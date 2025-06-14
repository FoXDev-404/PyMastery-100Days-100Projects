import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Update the endpoint to use the airport search API instead of cities
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

# Fallback IATA codes for common cities in case API fails
COMMON_CITY_CODES = {
    "Tokyo": "NRT",  # Narita International Airport
    "Hong Kong": "HKG",
    "Kuala Lumpur": "KUL",
    "Dublin": "DUB",  # Correct code for Dublin
    "New York": "JFK",
    "London": "LHR",
    "Paris": "CDG",
    "Frankfurt": "FRA",
    "Istanbul": "IST",
    "San Francisco": "SFO",
    "Bangkok": "BKK",
    "Singapore": "SIN",
    "Dubai": "DXB",
    "Athens": "ATH",
    "Delhi": "DEL",  # Added Delhi
    "Mumbai": "BOM",  # Added Mumbai
    "Bangalore": "BLR",  # Added Bangalore
    "Chennai": "MAA",  # Added Chennai
    "Kolkata": "CCU",  # Added Kolkata
}

class FlightSearch:

    def __init__(self):
        """
        Initialize an instance of the FlightSearch class.

        This constructor performs the following tasks:
        1. Retrieves the API key and secret from the environment variables 'AMADEUS_API_KEY'
        and 'AMADEUS_SECRET' respectively.

        Instance Variables:
        _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
        _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
        _token (str): The authentication token obtained by calling the _get_new_token method.
        """
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        self._token = self._get_new_token()
        # Add retry delay to manage rate limits
        self._retry_delay = 5

    def _get_new_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.

        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.

        Returns:
            str: The new access token obtained from the API response.
        """
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.
        Falls back to a predefined list for common cities if the API fails.
        
        Parameters:
        city_name (str): The name of the city for which to find the IATA code.
        
        Returns:
        str: The IATA code of the matching city/airport if found; otherwise returns an empty string.
        """
        print(f"Getting destination code for {city_name}")
        
        # First check our hardcoded dictionary for common cities
        if city_name in COMMON_CITY_CODES:
            code = COMMON_CITY_CODES[city_name]
            print(f"Using predefined IATA code {code} for {city_name}")
            return code
            
        headers = {"Authorization": f"Bearer {self._token}"}
        
        # Try multiple search strategies to increase chances of finding a match
        search_strategies = [
            {"keyword": city_name, "subType": "CITY"},
            {"keyword": city_name, "subType": "CITY,AIRPORT"},
            {"keyword": f"{city_name} Airport", "subType": "AIRPORT"}
        ]
        
        for strategy in search_strategies:
            # Add page limit to all strategies
            strategy["page[limit]"] = 10
            
            try:
                response = requests.get(
                    url=IATA_ENDPOINT,
                    headers=headers,
                    params=strategy
                )
                
                if response.status_code == 429:  # Rate limit exceeded
                    print(f"Rate limit hit. Waiting {self._retry_delay} seconds before retry.")
                    time.sleep(self._retry_delay)
                    # Increase delay for next time
                    self._retry_delay *= 2
                    continue
                    
                if response.status_code != 200:
                    print(f"Error in API response: {response.status_code}")
                    print(f"Response: {response.text}")
                    time.sleep(1)
                    continue
                
                result_data = response.json()
                
                if "data" in result_data and result_data["data"]:
                    # First try to find a direct city match
                    for location in result_data["data"]:
                        if location["subType"] == "CITY" and "iataCode" in location:
                            code = location["iataCode"]
                            print(f"Found city IATA code {code} for {city_name}")
                            return code
                    
                    # If no city match, try to find the main airport
                    for location in result_data["data"]:
                        if location["subType"] == "AIRPORT" and "iataCode" in location:
                            code = location["iataCode"]
                            print(f"Found airport IATA code {code} for {city_name}")
                            return code
            
            except Exception as e:
                print(f"Error during IATA search for {city_name}: {e}")
                time.sleep(1)
        
        # If we've tried all strategies and found nothing, check common cities list again
        if city_name in COMMON_CITY_CODES:
            code = COMMON_CITY_CODES[city_name]
            print(f"Falling back to predefined IATA code {code} for {city_name}")
            return code
            
        # Last resort - return empty string
        print(f"No valid IATA code found for {city_name} after trying multiple search strategies")
        return ""

    def get_iata_code(self, city_name):
        """
        Alias for get_destination_code for compatibility with main.py and other code.
        """
        return self.get_destination_code(city_name)

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Searches for flight options between two cities on specified dates.
        """
        print(f"Searching flights from {origin_city_code} to {destination_city_code}")
        
        # Check if destination code is empty or invalid
        if not destination_city_code:
            print(f"Cannot search flights with empty destination code")
            return None
            
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "false",  # Changed to allow connections if needed
            "currencyCode": "INR",  # Already set to INR
            "max": 10,
        }

        # Implement retry logic with small delay to handle potential rate limiting
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(
                    url=FLIGHT_ENDPOINT,
                    headers=headers,
                    params=query,
                )
                
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 429:  # Too many requests
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"Rate limit hit. Waiting {wait_time} seconds before retry.")
                    time.sleep(wait_time)
                    continue
                else:
                    print(f"check_flights() response code: {response.status_code}")
                    print("There was a problem with the flight search.\n"
                          "For details on status codes, check the API documentation:\n"
                          "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                          "-reference")
                    print("Response body:", response.text)
                    return None
                    
            except Exception as e:
                print(f"Error during flight search: {e}")
                time.sleep(1)
                
        print("Max retries exceeded for flight search.")
        return None