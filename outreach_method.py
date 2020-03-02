import json
import requests

# Get data from API
url = "http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&APPID=09110e603c1d5c272f94f64305c09436"
response = requests.get(url)
data = json.loads(response.text)

# Grab the weather information
for measurement in data["list"]:
    dt = measurement["dt"]
    temp = measurement["main"]["temp"]
    weather = measurement["weather"][0]["main"]
    sunny = True if weather == "Clear" else False
    rainy = True if weather == "Rain" else False
    print(dt, temp, sunny, rainy)
