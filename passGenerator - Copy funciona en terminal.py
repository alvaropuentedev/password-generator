import string
import random
from colorama import Fore
# import tkinter as tk
# from tkinter import ttk

def passGenerate():
   
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

    random.shuffle(characters)

    password = []

    while True:
        try:
            length = int(input(Fore.WHITE + 'Tamaño del pasword(de 0 a 200): '))
        except ValueError:
            print(Fore.RED + 'ERROR intruduce un número entero')
            length = int(input(Fore.WHITE + 'Tamaño del password(de 0 a 200): '))
        if length > 0 and length <= 200:

            for i in range(length):
                password.append(random.choice(characters))
                random.shuffle(password)
            print('La contraseña es: ', end='')
            for passw in password:
                if ord(passw) >= 48 and ord(passw) <= 57:
                    numeros = Fore.CYAN + passw
                    print(numeros, end='')
                elif ord(passw)>= 65 and ord(passw) <= 90 or ord(passw)>= 97 and ord(passw) <= 122:
                    letras = Fore.WHITE + passw
                    print(letras, end='')
                else:
                    signos = Fore.MAGENTA + passw
                    print(signos, end='')
            
            print('')
            password.clear()
        else:
            break

# win = tk.Tk()
# win.title('Password Generate')
# win.geometry('300x350')

# labelLength = ttk.Label(win, text= 'Longitud del password')
# labelLength.place(x=90, y=20, width=200, height=30)

# entryLength = tk.Entry(win, width=30)
# length = int(entryLength.get())
# entryLength.place(x=50, y=50, width=200, height=30)


# buttonGenerate = ttk.Button(win, text='Generate Password',command=passGenerate)
# buttonGenerate.place(x=75, y=100, width=150, height=30)

# generateString = tk.StringVar()
# entryGenerate = tk.Label(win, width=30, textvariable=generateString)
# entryGenerate.place(x=50, y=150, width=200, height=30)

# win.mainloop()