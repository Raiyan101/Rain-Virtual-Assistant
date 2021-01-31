# Features:
# Google calender
# send emails ///
# Add alarms ///
# notes ///
# currency convert ///
# google maps ///
# open up desktop apps ///
# calculator ///
# Play youtube vids ///
# Play music on spotify
# check weather ///
# check time ///
# open up and search google ///
# get answers from wikipedia ///
# jokes ///


# importing the required modules


from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
import pyttsx3  # pip install pyttsx
import speech_recognition as sr  # pip install speechRecognition
import datetime
import joke_file  # File containing the jokes (not a module)
import wikipedia  # pip install wikipedia
import pywhatkit   # pip install pywhatkit
import os
import smtplib
import email_feature  # file made by us
import sys
import weather_feature
import subprocess
import alarm_feature
import google_search
import currency_converter
import webbrowser
import calculator_file
import app
import threading
import json
import random
import pytz  # Built in module


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

# Initialising pyttsx
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

# function for audio output


def speak(text):
    update("console", text)
    engine.say(text)
    print(text)
    engine.runAndWait()


def update(key, value):
    data = None
    with open('temp.json', 'r') as f:
        data = json.load(f)
        data["data"][0][key] = value

    with open('temp.json', 'w') as f:
        json.dump(data, f)


def open_file(user_input):
    os.startfile(user_input)


def weather_command():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is the name of the city of which you want to know the weather of : ")
        audio = recogniser.listen(source)
        city_name = ""
        try:
            city_name = recogniser.recognize_google(audio)
            print(city_name)
        except Exception:
            print("Sorry didn't get that, could you please repeat?")
        return city_name


def take_command():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening: ")
        audio = recogniser.listen(source)
        command = ""
        try:
            command = recogniser.recognize_google(audio)
            print(command)
        except Exception:
            print("Sorry didn't get that, could you please repeat?")
        return command


def start_assistant():
    while True:
        try:
            command = take_command()
            command = command.lower()
            update("console", command)

            # Common Questions
            if "what is your name" in command:
                speak("My name is Rain")

            elif "hi" == command:
                speak("Hi, how are you doing?")

            elif "hello" == command:
                speak("Hello, how are you doing?")

            elif "how are you" in command:
                speak("I am fine, thank you for asking, how are you?")

            elif "i am fine" in command:
                speak("Good to know")

            elif "joke" in command:
                joke = joke_file.joke_choice()
                speak(joke)

            # Time and Date
            elif "what is the time" in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak("The Current time is " + time)

            elif "what is the date" in command:
                date = datetime.datetime.now().strftime("%A,%d %B, %Y")
                speak("The date today is " + date)

            elif "what is the day" in command:
                day = datetime.datetime.now().strftime("%A")
                speak(f"The day today is {day} ")

            elif "search wikipedia" in command or "wikipedia search" in command.lower():
                if "search wikipedia" in command:

                    command = command.replace("search wikipedia", "")

                if "wikipedia search" in command:
                    command = command.replace("wikipedia search", "")

                result = wikipedia.summary(command, 1)
                speak(result)

            elif "on youtube" in command or "search youtube" in command:
                if "on youtube" in command:
                    command = command.replace("on youtube", "")
                if "search youtube" in command:
                    command = command.replace("search youtube", "")

                speak("Playing " + command)
                pywhatkit.playonyt(command)

            # Put all the code inside a try and except block
            elif "quit" == command or "goodbye" == command or "bye" == command:
                speak("Goodbye, Have a nice day")
                break

            elif "send email" in command or "send mail" in command:
                email_feature.send_email_again()

            elif "weather" in command:
                location = weather_command()
                weather_feature.weather_forecast(location)

            elif "set alarm" in command:
                speak("What hour do you want the alarm to be at: ")
                alarm_hour = take_command()
                speak("What minute do you want the alarm to be: ")
                alarm_minute = take_command()
                speak("PM or AM: ")
                am_pm = take_command()
                speak("What message do you want to recieve: ")
                message = take_command()
                try:
                    alarm_feature.start_alarm(
                        alarm_hour, alarm_minute, am_pm, message, speak)
                except Exception as e:
                    print(f"Error: {e}")

            elif "open" in command:
                command = command.replace("open", "")

                try:
                    application = command + ".exe"
                    open_file(application)
                except Exception:
                    engine.say(
                        f"Couldn't find {application}, please enter the path of the application: ")
                    engine.runAndWait()
                    path = input(
                        f"Couldn't find {application}, please enter the path of the application: ")

                    if "\\" in path:
                        path = path.replace("\\", "/")
                    open_file(path)

            elif "search google" in command:
                res = google_search.search(command)
                speak(res)

            elif "convert" in command:
                res = currency_converter.convert(command)
                speak(res)

            elif "search map" in command:
                command = command.replace("search", "")
                command = command.replace("map", "")
                webbrowser.open_new(
                    f"https://www.google.com/maps/place/{command}")
                speak(f"Here is what I found for {command} on Google Maps")

            elif "make a note" in command or "write this down" in command or "remember this" in command or "add a note" in command:
                fileName = str(datetime.date.today(
                )) + str(datetime.datetime.now().strftime("%H:%M:%S")).replace(":", "-") + ".txt"
                speak("What would you like me to write down?")

                text = take_command()
                with open(fileName, "w") as f:
                    f.write(text)
                open_file(os.getcwd() + "\\" + fileName)
                speak("I added this note for you")

            elif "x" in command or "multiplied" in command or "multiply" in command or "add" or "+" in command or "-" in command or "/" in command in command or "subtract" in command or "divide" or "divided" in command:
                result = calculator_file.calculate(command)
                result = "The answer is " + str(result)
                if result != None:
                    speak(result)

            elif "spotify" in command:

                speak(
                    "What is the name of the song/album or artist you want to search for: ")
                song = take_command()

                url = f"https://open.spotify.com/search/{song}"
                webbrowser.open_new(url)
                engine.say(
                    "This is what I found")
            command = command.lower()
            options = ["what do i have", "do i have plans", "am i busy",
                       "what event do i have", "what events do i have"]
            for option in options:
                if option in command:
                    start_calender()

            # elif "what do i have" in command or "do i have planes" in command or "am i busy" in command or "what events do i have" in command or "what event do i have " in command:
                # start_calender()
            else:
                pass

        except SystemExit:
            pass

        except Exception as e:
            print(f"Error: {e}")


def authenticate_google():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def get_events(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        speak('No upcoming events found.')
    else:
        speak(f"You have {len(events)} events on this day.")

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + "am"
            else:
                start_time = str(int(start_time.split(":")[0])-12)
                start_time = start_time + "pm"

            speak(event["summary"] + " at " + start_time)


def get_date(text):
    text = text

    text = text.lower()

    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year+1

    if month == -1 and day != -1:
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  # FIXED FROM VIDEO
        return datetime.date(month=month, day=day, year=year)


def start_calender():
    global text
    SERVICE = authenticate_google()
    print("Start")
    text = take_command()
    text = text.lower()

    CALENDAR_STRS = ["what do i have", "do i have plans",
                     "am i busy", "what events do i have", "what event do i have"]
    for phrase in CALENDAR_STRS:
        if phrase in text.lower():
            date = get_date(text)
            if date:
                get_events(date, SERVICE)
            else:
                speak("Please Try Again")


# start_assistant()


def start():
    t2 = threading.Thread(target=start_assistant)
    t2.start()
    app.start_gui()


start()
