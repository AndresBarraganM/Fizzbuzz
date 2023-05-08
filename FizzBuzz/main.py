#Principal
import tkinter as Tkint
from Applicacion import *
from tkinter import *


global mainWindow
mainWindow = Tk()
mainWindow.title("customFizzBuzz")
mainWindow.geometry("700x500")

Applicacion(mainWindow)





mainWindow.mainloop()