import json
import urllib.request


def kelvinToC(gradosKelvin):
    celsius = gradosKelvin - 273.15
    return celsius

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = "d1b8030cd2ec2ac8c624f99b69c166f6"
CITY = "Piedras%20Negras"
#CITY = "New%20Mexico"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
print("URL: ", url)

openWeb = urllib.request.urlopen(url)
response = json.load(openWeb)

print(response)

temp = response['main']['temp']
humidity = response['main']['humidity']
windSpeed = response['wind']['speed']

print("Temperatura en celsius: ", kelvinToC(temp))
print("Humedad: ", humidity)
print("Viento: ", windSpeed)























