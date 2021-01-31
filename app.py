import tkinter as tk
import threading
import json
import pyttsx3
import sys

def update(key, value):
    data = None
    with open('temp.json', 'r') as f:
        data = json.load(f)
        data["data"][0][key] = value

    with open('temp.json', 'w') as f:
        json.dump(data, f)

def after():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    update("console", "Hi, How can I help you?")
    engine.say("Hi, How can i help you?")

    if engine._inLoop:
        engine.endLoop()

root = tk.Tk()

root.title("Rain Virtual Assistant")
root.geometry("500x500")
root.resizable(False,False)
root.configure(background="white")


settingsIconCanvas = tk.Canvas(root, bg="white", width=500, bd=0, highlightthickness=0)
settingsIconCanvas.grid(row=0, column=0, pady=20, padx=20, sticky="W")


infoIcon = tk.Button(settingsIconCanvas, state=tk.DISABLED, text=(" " * 128), bd=0, bg="white", fg="white", highlightthickness=0)
infoIcon.grid(row=0, column=1, sticky="W")

settingsIconCanvas1 = tk.Canvas(root, bg="white", width=500, bd=0, highlightthickness=0)
settingsIconCanvas1.grid(row=2, column=0, pady=30, padx=20, sticky="N")
img1 = tk.PhotoImage(file="icons/sound.gif")
settingsIcon1 = tk.Button(settingsIconCanvas1,image=img1, bd=0, highlightthickness=0)
settingsIcon1.grid(row=0, column=0)


def hideIcon():
    settingsIcon1.grid_forget()

def showIcon():
    settingsIcon1.grid(row=0, column=0)

img = tk.PhotoImage(file="icons/settings.gif")
settingsIcon = tk.Button(settingsIconCanvas,image=img, bd=0, highlightthickness=0)
settingsIcon.grid(row=0, column=0, sticky="W")

img2 = tk.PhotoImage(file="icons/info.gif")
infoIcon = tk.Button(settingsIconCanvas,image=img2, bd=0, highlightthickness=0)
infoIcon.grid(row=0, column=2, sticky="W")

welcome_text = tk.Label(root, fg="#1c2434", bg="white", text="Hi, How can I help you?", font=("Helvetica", "20"))
welcome_text.grid(row=1, column=0, pady=10, padx=104)

console_text = tk.Text(root, bg="#1c2434", padx=20, pady=25, fg="#FFD800", font=("Helvetica", "10", "bold"), width=66, height=10)
console_text.grid(row=3, column=0)


def on_closing():
    print("[CLOSING] Please Wait .... ")
    with open("close.txt", "w") as f:
        f.write("CLOSE_FILE")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def start_gui():
    root.mainloop()

def updateUI():
    with open('temp.json', 'w') as f:
        f.write("{\"data\" : [{\"console\" : \"\"}]}")
    
    while True:
        try:
            with open('temp.json', 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
        except:
            pass
        try:

            if data["data"][0]["console"] != console_text.get("1.0", 'end-1c'):
                console_text.delete("1.0", "end-1c")
                console_txt = data["data"][0]["console"]
                console_text.insert(tk.END, console_txt)

            else:
                pass
        except:
            pass

t = threading.Thread(target=updateUI)
t.start()
