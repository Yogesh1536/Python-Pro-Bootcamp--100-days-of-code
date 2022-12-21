import smtplib
import ssl
import datetime as dt
import random

my_email = 'yogeshs15101999@gmail.com'
password = "whptbcumuoafzwkj"
email_receiver = "yogeshs1536@gmail.com"

context = ssl.create_default_context()

now = dt.datetime.now()
today = now.weekday()

if today == 0:
    with open("quotes.txt", "r") as text:
        quotes = text.read()
        lists = quotes.split('\n')
        quotes = random.choice(lists)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_receiver,
            msg=f"Subject:Hello,Yogesh\n\n{quotes}"
        )
