from gtts import gTTS
import os
from tkinter import *


# def isi():
#     e = Entry(root)
#     e.pack()

# Text ke Suara
def text():
    result = isi.get()
    file = gTTS(text = result, lang="id")
    file.save("hallo.mp3")
    os.system("start hallo.mp3 ")

root = Tk()
root.geometry("250x250")
root.title("Text to Speech")

label = Label(root, text = "Masukan Text")
label.pack()
isi = Entry(root)
isi.pack()

tombol = Button(root, text= "Jalankan", command=text)
tombol.pack()

menu = Menu(root)
root.config(menu = menu)
root.mainloop()