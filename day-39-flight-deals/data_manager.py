import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f67b10a3d7cc6477d8bac06b1ce12143/flightDeals/prices"
SHEETY_TOKEN = "Flightdealsapibyyogi"

class DataManager:

    def __init__(self):

        self.headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        response.raise_for_status()

        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return response.json()["prices"]

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self, city):
        code_url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
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
