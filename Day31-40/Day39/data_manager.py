import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "https://api.sheety.co/8ad57fafd49791bb02680d4a2866169c/flightDeals/prices")

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)

    def update_lowest_price(self, city_id, new_price):
        """
        Updates the lowest price for a destination in the sheet.
        
        Parameters:
        city_id (int): The ID of the city record in the sheet
        new_price (float): The new lowest price for the destination
        
        Returns:
        bool: True if update was successful, False otherwise
        """
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        
        try:
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city_id}",
                json=new_data,
                auth=self._authorization
            )
            if response.status_code in [200, 201, 204]:
                print(f"Successfully updated lowest price to {new_price} for city ID {city_id}")
                return True
            else:
                print(f"Failed to update price: {response.text}")
                return False
        except Exception as e:
            print(f"Error updating price: {e}")
            return False