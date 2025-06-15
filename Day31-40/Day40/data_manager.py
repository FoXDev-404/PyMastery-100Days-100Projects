import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):

        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        # Save your Sheety endpoints an environment variables
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        # Destination and Customer fields data start out empty
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.prices_endpoint)
        data = response.json()
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data

