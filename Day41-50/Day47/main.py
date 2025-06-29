from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


URL = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 100.00

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the price
price_element = soup.find('span', class_='aok-offscreen')
if price_element:
    price_text = price_element.get_text()
    current_price = float(price_text.replace("$", ""))
    print(f"Current price: ${current_price}")
else:
    print("Price element not found.")
    exit()

# Load credentials
my_email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT", my_email)

# Send email if price is below target
def send_email_notification(price):
    try:
        subject = "Price Drop Alert!"
        body = (
            f"The price dropped to ${price}!\n\n"
            f"Check it here: {URL}"
        )
        msg = f"Subject:{subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=msg)
        print("Email sent successfully.")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Check and notify
if current_price < TARGET_PRICE:
    send_email_notification(current_price)
else:
    print("📈 Price is still too high. No email sent.")
