import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "622e688f87a8e2d7afbe773c1da311d3"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
# Make a GET request to the API
response = requests.get("https://official-joke-api.appspot.com/jokes/random")

joke = response.json()
print("Random Joke:")
print(joke['setup'], joke['punchline'], "\n")

def main():
    temp = get_weather("London")
    temp_kelvin = temp['main']['temp']
    temp_fahrenheit = round(((temp_kelvin - 273.15) * 9/5 + 32), 2)
    print("Temp in London (Fahrenheit):")
    print(temp_fahrenheit, "degrees")

if __name__ == "__main__":
    main()
