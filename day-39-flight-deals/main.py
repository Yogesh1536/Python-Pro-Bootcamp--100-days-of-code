from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CODE = "BLR"


sheet_data = data_manager.get_destination_data()

for city in sheet_data:
    if city["iataCode"] == "":
        query_result = flight_search.get_destination_code(city["city"])
        city["iataCode"] = query_result[0]["code"]
        # update the row in the spreadsheet
        data_manager.update_destination_codes(city)

for city in sheet_data:
    # using the default time zone
    today = dt.datetime.now()
    tomorrow = today + dt.timedelta(days=1)
    in_six_months = today + dt.timedelta(days=(6 * 30))
    # get a flight object with the details
    flight = flight_search.find_flights(origin=ORIGIN_CODE, destination=city["iataCode"],
                                        date_from=tomorrow.strftime("%d/%m/%Y"),
                                        date_to=in_six_months.strftime("%d/%m/%Y"))

    # send an sms if price is lower than defined in the spreadsheet
    if flight.price <= city["lowestPrice"]:
        # to have some feedback
        print("Sending a notification.")
        notification_manager.send_sms(flight)
