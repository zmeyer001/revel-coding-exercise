import json
import requests

# Get data from API
url = "http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&APPID=09110e603c1d5c272f94f64305c09436"
response = requests.get(url)
data = json.loads(response.text)

# Grab the weather information
daily_measures = {}     # keys: date, values: (temp, sunny, rainy)
for measurement in data["list"]:
    # If we've already grabbed info about this date, move on
    date = measurement["dt_txt"].split(" ")[0]
    if date in daily_measures:
        continue

    # If the time isn't noon, move on
    time = measurement["dt_txt"].split(" ")[1]
    if time != "12:00:00":
        continue

    # Grab the temperature and sunshine/rain conditions
    temp = measurement["main"]["temp"]
    weather = measurement["weather"][0]["main"]
    sunny = True if weather == "Clear" else False
    rainy = True if weather == "Rain" else False
    if date not in daily_measures:
        daily_measures[date] = (temp, sunny, rainy)

for day in daily_measures:
    print(day, daily_measures[day])
