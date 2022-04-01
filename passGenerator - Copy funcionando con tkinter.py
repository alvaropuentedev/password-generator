import string
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk

def passGenerate():
    #Variable con todos los caracteres que puede conterner el password
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
    #Mezcla los caracteres
    random.shuffle(characters)
    #Variable para el password
    password = []
    #Limpia el box del password
    entryGenerate.delete(0, END)       
    #Genera el password y mezcla los caracteres
    for i in range(pw_length.get()):
        password.append(random.choice(characters))
        random.shuffle(password)

    #Dependiendo el tipo del caracter lo muestra en un color       
    for passw in password:
        if ord(passw) >= 48 and ord(passw) <= 57:
            entryGenerate.insert(0, passw)
                    
        elif ord(passw)>= 65 and ord(passw) <= 90 or ord(passw)>= 97 and ord(passw) <= 122:
            entryGenerate.insert(0, passw)
                
        else:
            entryGenerate.insert(0, passw)
                    
    #Limpia la longitud del password       
    pw_length.set(value=0)

#Función para copiar el password
def copy():
    win.clipboard_clear()
    
    win.clipboard_append(entryGenerate.get())

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

#Interfaz
win = tk.Tk()
win.title('Password Generate')
win.geometry('300x350')
# win.config(bg=rgb_hack((255, 0, 122)))
txt = tk.Text(win)
#Label
labelLength = ttk.Label(win, text= 'Longitud del password', font=('Source Code pro', 10))
labelLength.place(x=64, y=20, width=200, height=30)

#Entry donde indicamos longitud del password
pw_length = tk.IntVar()
entryLength = tk.Entry(win, width=30, textvariable=pw_length)
entryLength.place(x=50, y=50, width=200, height=30)

#Botón que genera el password
buttonGenerate = ttk.Button(win, text='Generate Password',command=passGenerate)
buttonGenerate.place(x=75, y=100, width=150, height=30)

#Botón para copiar el password
buttonCopy = ttk.Button(win, text='Copy Password',command=copy)
buttonCopy.place(x=75, y=200, width=150, height=30)

#Label donde se escribe el password generado
# generateString = tk.StringVar()
entryGenerate = tk.Entry(win, text='', font=('Source Code pro', 16), bd=0, bg='systembuttonface')
entryGenerate.pack(pady=20)
entryGenerate.place(x=50, y=150, width=200, height=30)

#Inicio interfaz
win.mainloop()