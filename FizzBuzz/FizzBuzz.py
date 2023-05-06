# Variables que ocupo
# --Multiplos para fizz
# --Multiplos npara Buzz
# --Nombre de fizz
# --Nombre de buzz
# --Elementos a imprimir

from clasePalabra import Palabra
from elemento import Elemento

#----------------------- Parametros -------------------------#
elementosAImprimir = 30

#lista que guarda las palabras a usar
listaPalabras=[]
listaPalabras.append(Palabra(3,"FIZZ"))
listaPalabras.append(Palabra(5,"BUZZ"))

elemento = Elemento(listaPalabras)

#---------------------- Codigo ------------------------------#
for i in range(elementosAImprimir): #por cada elemento que quiero hacer
    print(elemento.generarTexto(i+1))
    #print(listaPalabras[i])

