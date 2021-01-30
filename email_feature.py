import smtplib
import pyttsx3
from getpass import getpass
import stdiomask
import tkinter as tk
from tkinter import messagebox
import json

engine = pyttsx3.init()

state = {"done" : 0}

def speak(text):
    engine.say(text)
    engine.runAndWait()

user_details = {
    
        "senders_email" : None,
        "senders_password" : None,
        "receiver_email" : None,
        "message" : None

    }

def saveDetails(email, password, emailR, message, root):
    if "@" not in email or ".com" not in email:
        messagebox.showerror("Error", "Please enter a correct Email Adress")
        state["done"] = 0
    elif "@" not in emailR or ".com" not in emailR:
        messagebox.showerror("Error", "Please enter a correct Email Adress")
        state["done"] = 0
    else:
        root.destroy()
    user_details["senders_email"] = email
    user_details["senders_password"] = password
    user_details["receiver_email"] = emailR
    user_details["message"] = message



def update(key, value):
    data = None
    with open('temp.json', 'r') as f:
        data = json.load(f)
        data["data"][0][key] = value

    with open('temp.json', 'w') as f:
        json.dump(data, f)

def start_gui():
    root = tk.Tk()
    root.geometry("500x700")
    root.resizable(False,False)
    root.title("Send Email - Rain Virtual Assistant")
    root.configure(background="white")

    pad = tk.Label(root, text="",fg="white", bg="white").grid(row=0, column=0, pady=20)

    emailEntryLabel = tk.Label(root, text="Sender's Email Adress", font=("Helvetica", "12"), bg="white", fg="#818181").grid(row=2, column=0, pady=0)
    emailEntry = tk.Entry(root,bd=0, font=("Helvetica", "12"), justify="center", bg="#E1E1E1")
    emailEntry.grid(row=3, column=0, ipadx=100, ipady=10, pady=20, padx=55)
    
    passwordEntryLabel = tk.Label(root, text="Sender's Password", font=("Helvetica", "12"), bg="white", fg="#818181").grid(row=4, column=0, pady=0)
    passwordEntry = tk.Entry(root,bd=0, show="*",font=("Helvetica", "12"), justify="center", bg="#E1E1E1")
    passwordEntry.grid(row=5, column=0, ipadx=100, ipady=10, pady=20)
    
    emailREntryLabel = tk.Label(root, text="Reciever's Email Adress", font=("Helvetica", "12"), bg="white", fg="#818181").grid(row=6, column=0, pady=0)
    emailREntry = tk.Entry(root,bd=0, font=("Helvetica", "12"), justify="center", bg="#E1E1E1")
    emailREntry.grid(row=7, column=0, ipadx=100, ipady=10, pady=20)

    messageEntryLabel = tk.Label(root, text="Message", font=("Helvetica", "12"), bg="white", fg="#818181").grid(row=8, column=0, pady=0)
    messageEntry = tk.Text(root,bd=0, font=("Helvetica", "12"), padx=20, pady=10, width=16, height=5, bg="#E1E1E1")
    messageEntry.grid(row=9, column=0, ipadx=100, ipady=10, pady=20)
    
    saveDetailsLambda = lambda: saveDetails(emailEntry.get(), passwordEntry.get(), emailREntry.get(), messageEntry.get("1.0",'end-1c'), root)

    sendBtn = tk.Button(root,bd=0, font=("Helvetica", "12", "bold"), text="Send", bg="#1c2434", fg="#FFD800", width=16, padx=20, command=saveDetailsLambda).grid(column=0, row=10, ipadx=90, ipady=10, pady=0)
    root.mainloop()

def send_email():
    global senders_email, receivers_email, message, email_password
    messagebox.showinfo("Note", "You need to enable allow less secure apps in gmail for this to work")
    update("console", "You need to enable allow less secure apps in gmail for this to work")
    start_gui()
    state["done"] += 1
    try:
        senders_email = user_details["senders_email"]
        receivers_email = user_details["receiver_email"]
        email_password = user_details["senders_password"]
        message = user_details["message"]

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(senders_email, email_password)
        print("Successfully logged in.")
        update("console", "Successfully logged in.")
        server.sendmail(senders_email, receivers_email, message)
        print(f"Email has been sent to {receivers_email}")
        update("console",  f"Email has been sent to {receivers_email}")
        messagebox.showinfo("Success", f"Email has been sent to {receivers_email}")
    except Exception as e:
        print(f"Error: {e} ")
        state["done"] = 0
        messagebox.showerror("Error", "Wrong account details")
        update("console", "Wrong account details")


def send_email_again():
    
    if state["done"] < 1:
        send_email()
    elif state["done"] >= 1:
        msgbox = messagebox.askquestion(title='Note', message="Do you want to use the same information for the email as the last time?")

        if msgbox == "yes":
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(senders_email, email_password)
                print("Successfully logged in.")
                update("console", "Successfully logged in.")
                server.sendmail(senders_email, receivers_email, message)
                print(f"Email has been sent to {receivers_email}")
                messagebox.showinfo("Success", f"Email has been sent to {receivers_email}")
                update("console", f"Email has been sent to {receivers_email}")
            except Exception as e:
                print(f"Error: {e} ")
                state["done"] = 0
                messagebox.showerror("Error", "Wrong account details")
                update("console", "Wrong account details")

        elif msgbox == "no":
            send_email()

        else:
            send_email()