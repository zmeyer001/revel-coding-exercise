import json
import requests

# Get data from API
url = "http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&APPID=09110e603c1d5c272f94f64305c09436"
response = requests.get(url)

data = json.loads(response.text)
print(json.dumps(data, indent=4))
