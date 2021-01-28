# Features:
# Add Items to google calender and check for remainders ///
# read and send emails ///
# Add remainders and alarms ///
# notes ///
# currency convert ///
# google maps ///
# open up desktop apps
# calculator
# Play yt vids ///
# Play music on spotify or youtube
# check weather ///
# check time ///
# open up and search google ///
# get answers from wikipedia ///
# jokes ///
# news///

# importing the required modules
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

# Initialising pyttsx
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

# function for audio output


def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


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

            # Common Questions
            if "what is your name" in command:
                speak("My name is Rain")

            elif "hi" == command:
                speak("Hi, how are you doing?")

            elif "hello" == command:
                speak("Hello, how are you doing?")

            elif "how are you" in command:
                speak("I am fine, thank you for asking, how are you?")

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

            elif "search wikipedia" in command:
                command = command.replace("wikipedia", "")
                result = wikipedia.summary(command, 1)
                speak(result)

            elif "on youtube" in command:
                command = command.replace("on youtube", "")
                speak("Playing " + command)
                pywhatkit.playonyt(command)

            # Put all the code inside a try and except block
            elif "quit" == command or "goodbye" == command or "bye" == command:
                speak("Goodbye, Have a nice day")
                break

            elif "send email" in command:
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

            else:
                pass

        except SystemExit:
            pass

        except Exception as e:
            print(f"Error: {e}")


start_assistant()
