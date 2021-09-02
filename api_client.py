import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.json())
longitude = response.json()["iss_position"]["longitude"]
print(longitude)


parameters = {
    "lat": 4.710989,
    "log": -74.072090
}
response_sunrise = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response_sunrise.json())