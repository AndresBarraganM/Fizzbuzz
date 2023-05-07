from tkinter import *
from FizzBuzz import fizzBuzz

def Applicacion(mainWindow):
    
    txtCantidad = Label(mainWindow, text="Cuantos mostrarar:" )

    entradaCantidad = Entry( )

    def iniciarPrograma():
        labelElementos = Label(mainWindow, text=fizzBuzz(int(entradaCantidad.get())) )
        labelElementos.pack()

    botonIniciar = Button(mainWindow, text="iniciar", command= iniciarPrograma)
    #botonIniciar.grid(row=3,column=2)

    #txtDefineInterbalo1.grid(row=0, column=0)
    #entradaInterbalo1.grid(row=1,column=0)

    txtCantidad.pack()
    entradaCantidad.pack()
    botonIniciar.pack()