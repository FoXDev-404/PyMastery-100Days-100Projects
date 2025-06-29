from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.in/iQOO-Snapdragon-Processor-SuperComputing-Smartphone/dp/B0F83KLGCS"
TARGET_PRICE = 30000.00

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

price_whole = soup.find('span', class_='a-price-whole')
price_fraction = soup.find('span', class_='a-price-fraction')

if price_whole and price_fraction:
    whole = price_whole.get_text().replace(",", "").replace(".", "").strip()
    fraction = price_fraction.get_text().strip()
    price_string = f"{whole}.{fraction}"
    current_price = float(price_string)
    print(f"Current price: ₹{current_price}")
else:
    print("Could not find the price on the page.")
    exit()

# Load email credentials from .env
my_email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT", my_email)

if not my_email or not password:
    print("Missing EMAIL or EMAIL_PASSWORD in .env file.")
    exit()

# Send an email alert
def send_email_notification(price):
    try:
        subject = "Price Drop Alert!"
        body = f"The price dropped to ₹{price}!\nCheck it here:\n{URL}"
        msg = f"Subject:{subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient,
                msg=msg
            )
        print("Email sent successfully.")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Check price and notify
if current_price < TARGET_PRICE:
    send_email_notification(current_price)
else:
    print("Price is still above target. No email sent.")
