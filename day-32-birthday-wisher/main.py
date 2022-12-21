import smtplib
import ssl
import datetime as dt
import random
import pandas as pd

# enter Your mail id
MY_EMAIL = 'yogeshs15101999@gmail.com'
# enter your 16 digit password, which you can generate from your
# account->settings->privacy->app password-> select others(type "python")-> click generate
PASSWORD = "****************"

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    name = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as file:
        letter = file.read()
        wishes = letter.replace("[NAME]", name['name'])

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=name['email'],
            msg=f"Subject:Birthday Wishes\n\n{wishes}"
        )
