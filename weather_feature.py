import requests
from datetime import datetime
import pyttsx3
import json

engine = pyttsx3.init()


# Info to show: Temperature, Humidity, Wind speed, weather description

def update(key, value):
    data = None
    with open('temp.json', 'r') as f:
        data = json.load(f)
        data["data"][0][key] = value

    with open('temp.json', 'w') as f:
        json.dump(data, f)

def weather_forecast(city):
    try:
        user_api = "da7e8fa5805bffca5b90637d45bf32bd"
        location = city

        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
            location + "&appid="+user_api

        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data["cod"] == "404":
            print(f"{location} is an invalid, city name please try again")
        else:
            temperature = ((api_data["main"]["temp"])-273.15)
            weather_description = api_data["weather"][0]["description"]
            wind_speed = api_data["wind"]["speed"]
            humidity = api_data["main"]["humidity"]
            pressure = api_data["main"]["pressure"]
            date_time = datetime.now().strftime("%d %B %Y ||  %I:%M:%S %p")
            
        update("console", 
        f"""---------------------------------------------------------
            Information/Stats on Weather of {location}. Time: {date_time}
            ---------------------------------------------------------
            The Current Temperature is {temperature}°C
            The Current Weather condition is {weather_description}
            The Current Humidty is {humidity}%
            The Current Wind Speed is {wind_speed} kmph
            The Current Atmospheric pressure is {pressure}(in hPa unit)""")

        print("---------------------------------------------------------")
        print(
            f"Information/Stats on Weather of {location}. Time: {date_time} ")
        print("---------------------------------------------------------")

        print(f"The Current Temperature is {temperature}°C")
        print(f"The Current Weather condition is {weather_description}")
        print(f"The Current Humidty is {humidity}%")
        print(f"The Current Wind Speed is {wind_speed} kmph")
        print(f"The Current Atmospheric pressure is {pressure}(in hPa unit) ")
        engine.say(
            f"The current weather condition in {location} is {weather_description} with a temperature of {temperature} degree celsius, humidity of {humidity} and wind speed of {wind_speed} kilometres per hour. The pressure is {pressure}")
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {e}")
