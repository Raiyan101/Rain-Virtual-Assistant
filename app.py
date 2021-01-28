import os


def open_file():
    try:
        os.startfile(
            "C:/Users/ADMIN/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad.lnk")
    except Exception:
        print("couldn't open")


# "C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk"
open_file()
