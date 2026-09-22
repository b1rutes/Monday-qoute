import smtplib
from random import choice
import datetime as dt

def monday_email():
    password = "vivs wjtf wmrc dnpe"
    to_address = "williamsbirute@gmail.com"
    senders_email = "williamsmugisha17@gmail.com"
    now = dt.datetime.now()

    if now.weekday() == 1:
        with open("quotes.txt") as file:
            quotes = file.readlines()
            quote = choice(quotes)
            message = f"Subject:Monday Quote\n\n{quote}"
        senders_email = "williamsmugisha17@gmail.com"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=senders_email, password=password)
            connection.sendmail(
                from_addr= senders_email,
                to_addrs= to_address,
                msg= message)


if __name__ == "__main__":
    monday_email()
             
    


