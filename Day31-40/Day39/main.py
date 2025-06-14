import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "DEL"  # Changed from "LON" to "DEL" (Delhi, India)

# ==================== Update the Airport Codes in Google Sheet ====================

# Manual fix for Dublin's incorrect IATA code
for row in sheet_data:
    if row["city"] == "Dublin" and row["iataCode"] == "DBN":
        print("Fixing incorrect IATA code for Dublin (DBN → DUB)")
        row["iataCode"] = "DUB"

for row in sheet_data:
    # Update any empty IATA codes
    if row["iataCode"] == "":
        print(f"Searching for IATA code for {row['city']}")
        new_code = flight_search.get_destination_code(row["city"])
        # Update code if we got a valid result
        row["iataCode"] = new_code
        # Add a delay between API calls to prevent rate limiting
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")

# Update the spreadsheet with new IATA codes
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination}")
    # Skip destinations with empty IATA codes
    if not destination["iataCode"]:
        print(f"Skipping {destination['city']} due to missing IATA code")
        continue
        
    # Add a delay between flight searches to prevent rate limiting
    time.sleep(2)
    
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    
    if flights is None:
        print(f"No flights found for {destination['city']}")
        continue
        
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        message = (f"Low price alert! Only ₹{cheapest_flight.price} to fly "
                 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
                 
        # Choose one notification method based on your preference
        notification_manager.send_sms(message_body=message)
        # notification_manager.send_whatsapp(message_body=message)
        
        # Update the lowest price in the sheet
        update_result = data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        if update_result:
            print(f"Updated lowest price for {destination['city']} in sheet to ₹{cheapest_flight.price}")
        else:
            print(f"Failed to update lowest price for {destination['city']} in sheet")
    else:
        print(f"No cheaper flights found for {destination['city']}")