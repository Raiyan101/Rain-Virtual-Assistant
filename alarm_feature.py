import datetime
import playsound


def start_alarm(alarm_hour, alarm_minute, am_pm, message, speak):
    alarm_hour = alarm_hour
    alarm_minute = alarm_minute
    am_pm = am_pm
    am_pm = am_pm.lower()
    message = message
    alarm_hour = int(alarm_hour)
    alarm_minute = int(alarm_minute)
    if am_pm == "pm":
        alarm_hour += 12

    while True:
        if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute:
            speak(message)
            print(f"The time now is {alarm_hour}:{alarm_minute} {am_pm}")
            playsound.playsound("alarm audio.wav")
            break
