from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import smtplib
import ssl

TWILIO_SID = "AC0a94f226912db29d1087ab9fe278634f"
TWILIO_TOKEN = "2f1a87856d36637f11e32946b9de5b72"


class NotificationManager:
    def __init__(self):

        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.sender = "Flight Club"
        self.my_email = "yogeshs15101999@gmail.com"
        self.password = "whptbcumuoafzwkj"

    def send_sms(self, flight):
        """Takes a flight object and sends the details as an SMS to the defined number."""
        message = f"Low Price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.leave_date} to {flight.return_date}."
        # re-using the code from Day 36, with minor changes
        if flight.stopovers > 0:
            # only expecting max. 1 stopover
            message += f"\nThe flight has {flight.stopovers} stop over, via {flight.via_city}."
            # re-using the code from Day 36, with minor changes
        print(message)
        try:
            message = self.client.messages.create(body=message, from_="+16206986017", to="+919080114615")
        except TwilioRestException as ex:
            # a generic error message that will get displayed with each failed attempt
            print(ex)
            print("Make sure the TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER and TARGET_NUMBER are set properly in ")
        else:
            print(message.status)

    def notify_users(self, flight, users):
        for user in users:
            receiver = f"{user['firstName']} {user['lastName']} <{user['email']}>"
            message = f"Subject: Low Price Alert from {self.sender}\nTo: {receiver}\n\n" \
                      f"Low Price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                      f" to {flight.destination_city}-{flight.destination_airport}, " \
                      f"from {flight.leave_date} to {flight.return_date}.\n\n" \
                      f"https://www.google.co.uk/flights?hl=en#flt=" \
                      f"{flight.origin_airport}.{flight.destination_airport}.{flight.leave_date}*" \
                      f"{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}".encode('utf-8')
            self.send_email(self.my_email, self.password, receiver, message)

    def send_email(self, sender, password, receiver, message):
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
                connection.login(user=sender, password=password)
                connection.sendmail(
                    from_addr=sender,
                    to_addrs=receiver,
                    msg=message
                )
        except smtplib.SMTPServerDisconnected:
            print("ERROR: Could not connect to the SMTP server. "
                  "Make sure the SMTP_LOGIN and SMTP_PASS credentials have been set correctly.")
        except smtplib.SMTPDataError:
            # in case too many emails are being sent in a short time
            # handling this properly is really not in the scope of this project
            print(f"ERROR: Too many emails per second. The message to {receiver} was not sent.")
        else:
            # just to have some feedback
            print(f"The message to {receiver} was sent.")

