class Palabra():
    #Variables que usare
    interbalo = 0 
    texto = "ERROR"

    def __init__(self,interbalo,texto):
        self.interbalo = interbalo
        self.texto = texto

    def __str__(self):
        return str(self.interbalo)+ ' '+ self.texto



