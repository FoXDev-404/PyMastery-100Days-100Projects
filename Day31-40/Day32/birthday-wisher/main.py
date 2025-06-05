import pandas as pd

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
birthdays_data = [
    {"name": "John Doe", "email": "john@example.com", "year": 1990, "month": 5, "day": 12},
    {"name": "Jane Smith", "email": "jane@example.com", "year": 1985, "month": 7, "day": 24},
    {"name": "Bob Johnson", "email": "bob@example.com", "year": 1995, "month": 3, "day": 8},
    {"name": "Alice Brown", "email": "alice@example.com", "year": 1988, "month": 11, "day": 17},
    {"name": "Test", "email": "test@email.com", "year": 1961, "month": 12, "day": 21}
]

# Create DataFrame and save to CSV
birthdays_df = pd.DataFrame(birthdays_data)
birthdays_df.to_csv("birthdays.csv", index=False)

print("Birthdays CSV file has been updated successfully!")

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




