import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    return os.getenv('OPENWEATHERMAP_API_KEY')

def get_forecast(lat, lon, amount=3):
    api_key = get_api_key()
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + api_key + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cnt=" + str(amount)
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == "200":
        forecast_list = data["list"]
        forecast = []
        for item in forecast_list:
            timestamp = item["dt_txt"]
            main = item["main"]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            weather_description = item["weather"][0]["description"]
            forecast.append({
                "timestamp": timestamp,
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity,
                "description": weather_description
            })
        return forecast
    else:
        return None


forecast_data = get_forecast(os.getenv('lat'), os.getenv('lon') )

if forecast_data is not None:
    for item in forecast_data:
        print("Timestamp : " + item["timestamp"])
        print("Temperature : " + str(item["temperature"]) + "\n" +
              "Atmospheric pressure : " + str(item["pressure"]) + "\n" +
              "Humidity : " + str(item["humidity"]) + "\n" +
              "Description : " + str(item["description"]) + "\n")
else:
    print("Location Not Found ")
