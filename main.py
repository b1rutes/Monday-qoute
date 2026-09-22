import smtplib
import os
from random import choice
import datetime as dt

def monday_email():
    email = os.environ['SENDER_EMAIL']
    password = os.environ['PASSWORD']
    now = dt.datetime.now()

    if now.weekday() == 0:
        with open("quotes.txt") as file:
            quotes = file.readlines()
            quote = choice(quotes)
            message = f"Subject:Monday Quote\n\n{quote}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr= email,
                to_addrs= email,
                msg= message)


if __name__ == "__main__":
    monday_email()
             
    


