import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
my_email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

# Verify credentials are available
if not my_email or not password:
    raise ValueError(
        "Email credentials not found in environment variables.\n"
        "Please set EMAIL and EMAIL_PASSWORD environment variables or create a .env file."
    )

try:
    # Connect to email server with proper error handling
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    
    # Send email
    recipient = os.environ.get("EMAIL_RECIPIENT", "recipient@example.com")
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg="Subject:Hello\n\nThis is the body of the email."
    )
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Failed to send email: {e}")
    
finally:
    # Always close the connection
    if 'connection' in locals():
        connection.close()
        print("Connection closed.")
# Note: Replace 'your_email@example.com' and 'your_password' with your actual email and password.
# Make sure to enable "Less secure app access" in your Google account settings if using Gmail.
# Also, consider using environment variables or a secure vault for storing sensitive information like email and password.
# Ensure you have the smtplib library available in your Python environment.
# Make sure to handle exceptions and errors in production code for better reliability.