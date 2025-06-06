import pandas as pd
import datetime as dt
import random
import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 💖 Load your secret email magic
load_dotenv()
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# 💕 Make sure secrets are safe
if not EMAIL or not EMAIL_PASSWORD:
    raise ValueError("Missing EMAIL or EMAIL_PASSWORD in environment variables!")

# 🎉 Optional: Create a sample birthdays.csv file (only if it doesn't exist)
sample_birthdays = [
    {"name": "John Doe", "email": "john@example.com", "year": 1990, "month": 5, "day": 12},
    {"name": "Jane Smith", "email": "jane@example.com", "year": 1985, "month": 7, "day": 24},
    {"name": "Bob Johnson", "email": "bob@example.com", "year": 1995, "month": 3, "day": 8},
    {"name": "Alice Brown", "email": "alice@example.com", "year": 1988, "month": 11, "day": 17},
    {"name": "Test", "email": "test@email.com", "year": 1961, "month": 6, "day": 4}
]

if not os.path.exists("birthdays.csv"):
    pd.DataFrame(sample_birthdays).to_csv("birthdays.csv", index=False)
    print("📅 Created sample birthdays.csv!")
else:
    print("📅 birthdays.csv already exists, skipping creation.")

# 🌸 Today's date
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# 🥰 Read the birthday list
birthdays_df = pd.read_csv("birthdays.csv")
today_birthdays = birthdays_df[(birthdays_df["month"] == today_month) & (birthdays_df["day"] == today_day)]

# 💌 Check for birthdays
if today_birthdays.empty:
    print("🌼 No birthdays today.")
else:
    print(f"🎈 Found {len(today_birthdays)} birthday(s) today!")

    # 💌 Setup email connection
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)

        # 🎀 Template folder
        template_dir = "letter_templates"
        template_files = [f for f in os.listdir(template_dir) if f.startswith("letter_")]

        if not template_files:
            print("❌ No letter templates found!")
        else:
            for _, row in today_birthdays.iterrows():
                # 🍬 Choose a random letter template
                selected_template = random.choice(template_files)
                with open(os.path.join(template_dir, selected_template)) as letter_file:
                    content = letter_file.read()

                # ✨ Personalize
                personalized_content = content.replace("[NAME]", row["name"])

                # 🕊 Compose the email
                message = MIMEMultipart()
                message["From"] = EMAIL
                message["To"] = row["email"]
                message["Subject"] = "🎂 Happy Birthday!"

                message.attach(MIMEText(personalized_content, "plain"))

                # 💫 Send the email
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=row["email"],
                    msg=message.as_string()
                )
                print(f"📨 Sent birthday email to {row['name']} ({row['email']})!")
