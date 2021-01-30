import tkinter as tk
import threading
import json

root = tk.Tk()

root.title("Rain Virtual Assistant")
root.geometry("500x500")
root.resizable(False,False)
root.configure(background="white")

settingsIconCanvas = tk.Canvas(root, width=40, height=40, bg="white", bd=0, highlightthickness=0)
settingsIconCanvas.grid(row=0, column=0, pady=20, sticky="w", padx=20)
settingsIcon = tk.PhotoImage(master= settingsIconCanvas,file="Rain-Virtual-Assistant/icons/settings-icon-png-1-original.gif")
settingsIconCanvas.create_image(0, 0, anchor=tk.NW, image=settingsIcon)

welcome_text = tk.Label(root, fg="#1c2434", bg="white", text="Hi, How can I help you?", font=("Helvetica", "20"))
welcome_text.grid(row=1, column=0, pady=70, padx=104)

console_text = tk.Entry(root, bg="#1c2434", fg="#FFD800", justify="center", font=("Helvetica", "10", "bold"))
console_text.grid(row=2, column=0, ipadx=160, ipady=50, pady=100)

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
            if data["data"][0]["console"] != console_text.get():
                console_text.delete(0, tk.END)
                console_txt = data["data"][0]["console"]
                console_text.insert(0, console_txt)
            else:
                pass
        except:
            pass

t = threading.Thread(target=updateUI)
t.start()
