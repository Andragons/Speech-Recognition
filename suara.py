import speech_recognition as sr
import os
from tkinter import *

def suara():
    engine = sr.Recognizer()
    mic = sr.Microphone()
    hasil = ""

    with mic as source:
        label = Label(root, text = "Silahkan Bicara")
        label.pack()
        rekaman = engine.listen(source)
        time = Label(root, text = "Waktu Habis")
        time.pack()
            
        try:
            hasil = engine.recognize_google(rekaman, language =  "id-ID")
            result = Label(root, text = hasil)
            result.pack()
        except engine.UnknownValueError:
            warning = Label(root, text = "Maaf tidak dideteksi, mohon coba lagi")
            warning.pack()
        except Exception as e:
            ex = Label(root, text = e)
            ex.pack()


root = Tk()
root.geometry("250x250")

tombol = Button(root, text = "Jalankan", command=suara)
tombol.pack()

menu = Menu(root)
root.config(menu = menu)
root.mainloop()