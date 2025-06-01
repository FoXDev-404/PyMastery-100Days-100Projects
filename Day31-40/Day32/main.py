import smtplib

my_email = "your_email@example.com"
password = "your_password"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="recipient@example.com",
    msg="Subject:Hello\n\nThis is the body of the email."
)

connection.close()
# Note: Replace 'your_email@example.com' and 'your_password' with your actual email and password.
# Make sure to enable "Less secure app access" in your Google account settings if using Gmail.
# Also, consider using environment variables or a secure vault for storing sensitive information like email and password.
# Ensure you have the smtplib library available in your Python environment.# Make sure to handle exceptions and errors in production code for better reliability.