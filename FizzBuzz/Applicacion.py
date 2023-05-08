from tkinter import *
from FizzBuzz import fizzBuzz

def Applicacion(mainWindow):
    labelElementos = Label(mainWindow,text="Presione Iniciar:")
    labelElementos.grid(row=5,column=0)

    def iniciarPrograma():
        labelElementos.config(text=fizzBuzz(int(entradaCantidad.get())))
        labelElementos.grid(row=12,column=0)
  

    txtCantidad = Label(mainWindow, text="Cuantos mostrarar:" )
    txtCantidad.grid(row=0, column=0)

    entradaCantidad = Entry( )
    entradaCantidad.grid(row=1,column=0)

    

    botonIniciar = Button(mainWindow, text="iniciar", command= iniciarPrograma)
    botonIniciar.grid(row=1,column=1)

    
    

