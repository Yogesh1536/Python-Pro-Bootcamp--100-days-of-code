import requests
from datetime import datetime

TOKEN = "asdfghjkl;'456321" #use your Token
USER_NAME = "yogesh1536"
GRAPH_ID = "graph1"
pixel_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixel_endpoint, json=user_params)  To create a Account on pixela
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USER_NAME}/graphs"  # This endpoint is used to create a graph on which activity you want to track by giving graph id
graph_param = {
    "id": GRAPH_ID,
    "name": "learning",
    "unit": "minutes",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

data_endpoint = f"{pixel_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime(year=2022, month=11, day=21)
data_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "100",
}
# response = requests.post(url=data_endpoint, json=data_params, headers=headers) To enter data into the graph1
# print(response.text)

update_date = datetime.now()
formated_date = update_date.strftime("%Y%m%d")
update_endpoint = f"{pixel_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formated_date}"
update_params = {
    "quantity": "300"
}
response = requests.put(url=update_endpoint, json=update_params, headers=headers) #To update the activity on mentioned date
print(response.text)