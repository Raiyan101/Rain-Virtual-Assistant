import smtplib
import pyttsx3
from getpass import getpass
import stdiomask

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


done = 0


def send_email():
    global done, senders_email, receivers_email, message, email_password
    done += 1
    try:
        print("**You will need to type the details regarding the email so no issues/mishearing occur**")
        print("")
        print("**You need to enable allow less secure apps in gmail for this to work**")
        speak("You need to enable allow less secure apps in gmail for this to work")
        print(" ")
        speak("Please enter the senders email address")
        senders_email = input("Please enter the senders email address: ")
        while "@" and "." not in senders_email:
            senders_email = input(
                "Please enter a valid senders email address: ")
        print(" ")

        speak("Please enter the recievers email address: ")
        receivers_email = input("Please enter the recievers email address: ")
        while "@" and "." not in receivers_email:
            receivers_email = input(
                "Please enter a valid receivers email address: ")
        print(" ")

        speak(
            f"Please enter your password for the email you want to send with(senders email)")
        email_password = stdiomask.getpass(
            "Please enter your password for the email you want to send with(senders email): ")
        print(" ")

        speak(
            f"Please enter the message you would like to send to {receivers_email}: ")
        message = input(
            f"Please enter the message you would like to send to {receivers_email}: ")
        print(" ")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(senders_email, email_password)
        print("Successfully logged in.")
        server.sendmail(senders_email, receivers_email, message)
        print(f"Email has been sent to {receivers_email}")
    except Exception as e:
        print(f"Error: {e} ")


def send_email_again():

    if done < 1:
        send_email()
    elif done >= 1:
        same_info = input(
            "Do you want to use the same information for the email as the last time?(y/n): ")
        speak("Do you want to use the same information for the email as the last time?")
        if same_info.lower() == "y" or "yes":
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(senders_email, email_password)
                print("Successfully logged in.")
                server.sendmail(senders_email, receivers_email, message)
                print(f"Email has been sent to {receivers_email}")
            except Exception as e:
                print(f"Error: {e} ")
        elif same_info.lower() == "n" or "no":
            send_email()

        else:
            send_email()
