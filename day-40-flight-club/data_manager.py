import requests

SHEETY_API_URL = "https://api.sheety.co"
SHEET_URL = "/f67b10a3d7cc6477d8bac06b1ce12143/flightDeals/"
SHEETY_TOKEN = "Flightdealsapibyyogi"


class DataManager:

    def __init__(self, worksheet_name):
        self.worksheet_name = worksheet_name
        self.worksheet_url = SHEETY_API_URL + SHEET_URL + self.worksheet_name
        self.headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

    def get_sheet(self):
        """Takes a worksheet name as STR, retrieves it and returns the rows as a LIST."""
        response = requests.get(url=self.worksheet_url, headers=self.headers)
        # just raise an error, not handling exceptions for now
        response.raise_for_status()
        # to have some feedback
        print(f"Worksheet \"{self.worksheet_name}\" successfully loaded.")
        return response.json()[self.worksheet_name]

    def update_destination_codes(self, city):
        code_url = f"{self.worksheet_url}/{city['id']}"
        new_data = {
            "price": {
                "iataCode": city["iataCode"]
            }
        }
        response = requests.put(
            url=code_url,
            json=new_data,
            headers=self.headers
        )
        response.raise_for_status()
        print(f"Row {city['id']} has been updated with code {city['iataCode']}.")

    def add_user(self, first_name, last_name, email):
        """Takes the user's details as STRs and add them to the worksheet."""
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=self.worksheet_url, json=body, headers=self.headers)
        # also just raise an error
        response.raise_for_status()
        # also to have some feedback
        print(f"User {first_name} {last_name} has been added to the \"{self.worksheet_name}\" worksheet.")
