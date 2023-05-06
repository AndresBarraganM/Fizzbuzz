#Es cada elemento que se muestra en pantalla

class Elemento():
    listaPalabra=[]
    def __init__(self,listaPalabra):
        self.listaPalabra = listaPalabra

    def generarTexto(self,indice):
        string =""
        fueAlterado= False

        for palabra in self.listaPalabra:
            if ((indice%palabra.interbalo)==0): #es entero?
                string += palabra.texto
                fueAlterado = True

        if(fueAlterado):
            return string
        else:
            return indice
        
