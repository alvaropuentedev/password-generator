import string
import random
import tkinter as tk
from tkinter import CENTER, END, Frame, PhotoImage, ttk

def passGenerate():
    #Variable con todos los caracteres que puede conterner el password
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

    #Mezcla los caracteres
    random.shuffle(characters)

    #Variable para el password
    password = []

    #Limpia el text del password
    textGenerate.delete(1.0, END)

    #Genera el password y mezcla los caracteres
    for i in range(pw_length.get()):
        password.append(random.choice(characters))
        random.shuffle(password)

    #Dependiendo el tipo del caracter lo muestra en un color       
    for passw in password:
        if ord(passw) >= 48 and ord(passw) <= 57:
            textGenerate.tag_config('red',justify=CENTER, foreground="magenta")
            textGenerate.insert('end', passw, 'red')
                    
        elif ord(passw)>= 65 and ord(passw) <= 90 or ord(passw)>= 97 and ord(passw) <= 122:
            textGenerate.tag_config('black',justify=CENTER, foreground="black")
            textGenerate.insert('end', passw, 'black')
                
        else:
            textGenerate.tag_config('blue',justify=CENTER, foreground="blue")
            textGenerate.insert('end', passw, 'blue')
                    
    #Limpia la longitud del password       
    # pw_length.set(value=0)

#Función para copiar el password
def copy():
    win.clipboard_clear()
    
    win.clipboard_append(textGenerate.get(1.0, END))

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

#Interfaz
win = tk.Tk()
win.title('PASSWORD GENERATOR')
win.geometry('300x350')
win.eval('tk::PlaceWindow . center')#Al iniciar la app se centra en mitad de la pantalla
# win.config(bg=rgb_hack((255, 0, 122)))

frame = Frame(win)
frame.pack(pady=50)

#Label
labelLength = ttk.Label(frame, text= 'Longitud del password', font=('Source Code pro', 10))
# labelLength.place(x=64, y=20, width=200, height=30)
labelLength.place(relx=0, rely=0, width=300, height=350)
img = PhotoImage(file=r"D:\alvaro\Pictures\output-onlinepngtools (1).PNG")
labelLength.image = img
labelLength.configure(image=img)
# labelLength.pack(pady=10)

#Entry donde indicamos longitud del password
pw_length = tk.IntVar()
entryLength = tk.Entry(frame, width=30, textvariable=pw_length)
entryLength.place(x=50, y=50, width=200, height=30)
entryLength.configure(justify='center')
entryLength.configure(relief="flat")
entryLength.pack()

#Botón que genera el password
buttonGenerate = ttk.Button(frame, text='Generate Password',command=passGenerate)
buttonGenerate.place(x=75, y=100, width=150, height=30)
buttonGenerate.pack(pady=10)

#Botón para copiar el password
buttonCopy = ttk.Button(frame, text='Copy Password',command=copy)
buttonCopy.place(x=75, y=200, width=150, height=30)
buttonCopy.pack()

#Text donde se escribe el password generado
textGenerate = tk.Text(frame,font=('Source Code pro', 16),borderwidth=0, background='SystemButtonFace')
textGenerate.pack(pady=10)

# textGenerate.place(x=50, y=150, width=200, height=30)

#Inicio interfaz
win.mainloop()