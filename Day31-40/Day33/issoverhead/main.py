import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv

# Load environment variables if present
try:
    load_dotenv()
except ImportError:
    pass

MY_LAT = 28.6419372696918 # Your latitude
MY_LONG = 77.20893327205839 # Your longitude

def is_iss_overhead():
    try:
        # Using alternative API that's more reliable
        response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["latitude"])
        iss_longitude = float(data["longitude"])

        # Your position is within +5 or -5 degrees of the ISS position.
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True
        return False
    except Exception as e:
        print(f"Error checking ISS location: {e}")
        return False
    
def is_night():
    try:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now().hour

        if time_now >= sunset or time_now <= sunrise:
            return True
        return False
    except Exception as e:
        print(f"Error checking if it's night: {e}")
        return False

# Complete the email sending functionality
def send_email_notification():
    try:
        my_email = os.getenv("EMAIL")
        password = os.getenv("EMAIL_PASSWORD")
        recipient = os.getenv("EMAIL_RECIPIENT", my_email)
        
        if not my_email or not password:
            print("Email credentials not found in environment variables")
            return False
            
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient,
                msg="Subject:ISS Overhead Alert!\n\nThe ISS is above you in the sky. Look up! 🛰️"
            )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Run the main logic
def check_iss():
    if is_iss_overhead() and is_night():
        print("ISS is overhead and it's dark! Sending notification...")
        send_email_notification()
    else:
        print("ISS is not in view or it's daytime. No notification needed.")

# If run directly, check once and exit
if __name__ == "__main__":
    check_iss()
    
    # Uncomment to run periodically
    # while True:
    #     check_iss()
    #     print("Waiting 60 seconds before checking again...")
    #     time.sleep(60)


