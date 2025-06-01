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