from abc import ABC, abstractclassmethod
class Unidimensional(ABC): # Aplico Abstracción
    def __init__(self):
        self.volumen=0
        self.masa=0
        print("Soy Unidimensional")

class Bidimensional(Unidimensional): # Aplicar Herencia
    def __init__(self): 
        super().__init__() # Llamado de constructor del padre
        print("Hola, soy un elemento bidimensional")



if(__name__ == "__main__"):
    print("Estoy en el programa principal")
    c = Bidimensional()
    print(c.volumen)