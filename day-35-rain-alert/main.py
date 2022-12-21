import requests
from twilio.rest import Client

API_KEY = 'df66c64960a184a3314f0b17eca5eb7e'
MY_LAT = 9.925201
MY_LON = 78.119774
account_sid = "AC0a94f226912db29d1087ab9fe278634f"
auth_token = "2f1a87856d36637f11e32946b9de5b72"

parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
hourly_dict = weather_data["hourly"][0:12]

will_rain = False
for hourly_weather in hourly_dict:
    weather_id = hourly_weather["weather"][0]["id"]
    if int(weather_id) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today, Don't forget to take your umbrella☔",
        from_='+16206986017',
        to='+919080114615'
    )
print(message.status)