from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager


ORIGIN_CODE = "BLR"


def add_new_user():
    """Adds a new user to the spreadsheet."""
    print("Welcome to the Flight Club.\nWe find the best flight deals and email you.")
    print("What is your first name?")
    first_name = get_name()
    print("What is your last name?")
    last_name = get_name()
    while True:
        print("What is your email?")
        email = get_email()
        print("Enter your email again.")
        email_check = get_email()
        if email == email_check:
            break
        print("The entered emails do not match.\nPlease try again.")
    # add the user
    users.add_user(first_name=first_name, last_name=last_name, email=email)
    print("Success!\nYour email has been added. You will receive notifications of cheap flights soon!")


def get_name():
    """Asks the user to input a name and returns it as a STR."""
    # the names might or might be from the Simpsons, some of the less naughty ones anyway
    # from https://simpsons.fandom.com/wiki/Bart%27s_prank_calls
    while True:
        name = input("> ")
        # make sure something was entered
        if name == "":
            print("Please enter a name.")
        else:
            return name


def get_email():
    """Asks the user to input an email address and returns it as a STR."""
    while True:
        email = input("> ")
        # make sure something was entered
        if email == "":
            print("Please enter an email address.")
        # check that it looks like an email address
        # just a simple validation, without using regular expressions
        elif email.find("@") == -1 or email.find(".") == -1:
            print("Please enter a valid email address.")
        else:
            return email


prices = DataManager("prices")
users = DataManager("users")
flight_search = FlightSearch()
notification_manager = NotificationManager()


sheet_data = prices.get_sheet()
users_data = users.get_sheet()

print("Enter \"y\" if you want to add a new user.")
choice = input("> ").lower()
if choice == "y":
    add_new_user()

for city in sheet_data:
    if city["iataCode"] == "":
        query_result = flight_search.get_destination_code(city["city"])
        city["iataCode"] = query_result[0]["code"]
        # update the row in the spreadsheet
        prices.update_destination_codes(city)

for city in sheet_data:
    # using the default time zone
    today = dt.datetime.now()
    tomorrow = today + dt.timedelta(days=1)
    in_six_months = today + dt.timedelta(days=(6 * 30))
    # get a flight object with the details
    flight = flight_search.find_flights(origin=ORIGIN_CODE, destination=city["iataCode"],
                                        date_from=tomorrow.strftime("%d/%m/%Y"),
                                        date_to=in_six_months.strftime("%d/%m/%Y"))
    if flight is None:
        continue

    # send an sms if price is lower than defined in the spreadsheet
    if flight.price <= city["lowestPrice"]:
        # to have some feedback
        print("Sending a notification.")
        notification_manager.send_sms(flight)
        print("Sending emails to all members.")
        notification_manager.notify_users(flight, users_data)
