import os, sys
from tkinter import *

root = Tk()
root.geometry("250x250")

menu = Menu(root)
root.config(menu = menu)

def teks():
    os.system("python text.py")
    os._exit(0)

def voice():
    os.system("python suara.py")

text = Button(root, text = "Text to Speech", command = teks)
text.pack()


menu.add_separator()

suara = Button(root, text = "Speech to Text", command = voice)
suara.pack()


root.mainloop()