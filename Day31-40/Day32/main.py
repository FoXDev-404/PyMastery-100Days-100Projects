import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()  # Secure your journey with encryption
    connection.login(user=EMAIL, password=EMAIL_PASSWORD)
    msg = "Subject:Hello from ZeroTwo 💕\n\nThis is the body of the email. Stay sweet, Psycho~"
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL_RECIPIENT,
        msg=msg.encode('utf-8')
    )
print("Email sent successfully! 💌")