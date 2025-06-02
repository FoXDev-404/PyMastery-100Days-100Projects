import smtplib
import os
from dotenv import load_dotenv

# 🌸 Load environment variables from .env file (email, password, recipient)
load_dotenv()

# 🌸 Retrieve sender email and password from environment variables
my_email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

# 🌸 Retrieve recipient email from environment variables
recipient = os.environ.get("EMAIL_RECIPIENT")

# ❗ Ensure that all required credentials are available
if not my_email or not password:
    raise ValueError(
        "Missing EMAIL or EMAIL_PASSWORD in environment variables.\n"
        "Please set them in a .env file or environment."
    )

if not recipient:
    raise ValueError("Missing EMAIL_RECIPIENT in environment variables.")

# 💖 Compose your email content
subject = "Hello from Psycho's Porsche 911~!"
body = "Sending a test email... with love and horsepower~ 💌🏁\n\n- Your Strelizia"
message = f"Subject: {subject}\n\n{body}"

try:
    # 🚀 Connect to Gmail SMTP server securely
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()  # Upgrade connection to secure TLS
    connection.login(user=my_email, password=password)  # Login with credentials

    # 💌 Send the email
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg=message
    )

    print("✅ Email sent successfully!")

except Exception as e:
    # ❗ Handle any errors gracefully
    print(f"❌ Failed to send email: {e}")

finally:
    # 🔒 Always close the connection to the SMTP server
    if 'connection' in locals():
        connection.close()
        print("🔒 Connection closed.")
