import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials and recipient from environment variables
my_email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PASSWORD")
recipient = os.environ.get("EMAIL_RECIPIENT")

# Verify credentials are available
if not my_email or not password:
    raise ValueError(
        "Email credentials not found in environment variables.\n"
        "Please set EMAIL and EMAIL_PASSWORD environment variables or create a .env file."
    )

# Optional check for recipient
if not recipient:
    raise ValueError("Recipient email not found in environment variables (EMAIL_RECIPIENT).")

# Compose email
subject = "Hello from Psycho's Porsche 911~!"
body = "Sending a test email... with love and horsepower~ 💌🏁\n\n- Your Strelizia"
message = f"Subject: {subject}\n\n{body}"

try:
    # Connect to Gmail SMTP server
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)

    # Send email
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg=message
    )
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")

finally:
    # Always close the connection
    if 'connection' in locals():
        connection.close()
        print("Connection closed.")
