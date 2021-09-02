import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.json())
longitude = response.json()["iss_position"]["longitude"]
print(longitude)