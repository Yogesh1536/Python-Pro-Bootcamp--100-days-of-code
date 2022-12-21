import requests
import flight_data as fd

LOCALE = "en-US"
NIGHTS_FROM = 7
NIGHTS_TO = 28
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "wHPg0Aw2ngTFWRVQBGpQKqpAIBg-REj5"
CURRENCY = "INR"
MAX_STOPOVERS = 1


class FlightSearch:
    def __init__(self):
        self.api_url = TEQUILA_ENDPOINT
        self.locale = LOCALE
        self.headers = {
            'apikey': TEQUILA_API_KEY
        }

    def get_destination_code(self, city_name):
        query_url = f"{self.api_url}/locations/query"
        params = {
            "term": city_name,
            "locale": self.locale,
            "location_types": "city",
            "active_only": True
        }
        response = requests.get(url=query_url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()["locations"]

    def find_flights(self, origin, destination, date_from, date_to):
        """Takes flight details as STRs and returns a flight_data object."""
        search_url = f"{self.api_url}/v2/search"
        params = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": NIGHTS_FROM,
            "nights_in_dst_to": NIGHTS_TO,
            "flight_type": "round",
            "curr": CURRENCY,
            "one_for_city": 1,
            "max_stopovers": MAX_STOPOVERS
        }
        response = requests.get(url=search_url, params=params, headers=self.headers)
        # also just raise an error, this will returns a "HTTPError" if credentials are not set properly
        response.raise_for_status()
        # only use the first result, if any

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight = fd.FlightData(
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            leave_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            price=data["price"]
        )
        # to have some feedback
        print(f"Found a flight to {flight.destination_city} for {flight.price} {CURRENCY}.")
        return flight
