#Principal
import tkinter as Tkint
from tkinter import *

from FizzBuzz import fizzBuzz
mainWindow = Tk()

def iniciarPrograma():
    labelElementos = Label(mainWindow, text=fizzBuzz() )
    labelElementos.pack()
    


botonIniciar = Button(mainWindow, text="iniciar", command= iniciarPrograma)
botonIniciar.pack()

mainWindow.mainloop()