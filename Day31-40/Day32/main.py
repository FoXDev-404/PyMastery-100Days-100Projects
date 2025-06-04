import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

now = dt.datetime.now()
weekday = now.weekday()  # Monday is 0, Sunday is 6
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    
    EMAIL = os.getenv("EMAIL")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL_RECIPIENT,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



# import smtplib
# import os
# from dotenv import load_dotenv

# load_dotenv()

# EMAIL = os.getenv("EMAIL")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()  # Secure your journey with encryption
#     connection.login(user=EMAIL, password=EMAIL_PASSWORD)
#     msg = "Subject:Hello from ZeroTwo 💕\n\nThis is the body of the email. Stay sweet, Psycho~"
#     connection.sendmail(
#         from_addr=EMAIL,
#         to_addrs=EMAIL_RECIPIENT,
#         msg=msg.encode('utf-8')
#     )
# print("Email sent successfully! 💌")


# import datetime as dt

# now = dt.datetime.now()  # Get the current date and time
# year = now.year  # Extract the year
# month = now.month  # Extract the month
# day = now.day  # Extract the day
# print(f"Year: {year}, Month: {month}, Day: {day}")

# date_of_birth = dt.datetime(year=2004, month=11, day=6)
# print(f"Date of Birth: {date_of_birth}")