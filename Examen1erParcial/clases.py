import math
class Punto2D():
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
    def __add__(self, otro_punto):
        x = self.x + otro_punto.x
        y = self.y + otro_punto.y
        return x, y
    def __sub__(self, otro_punto):
        x = self.x - otro_punto.x
        y = self.y - otro_punto.y
        return x, y
    def __mul__(self, escalar):
        x = self.x * escalar
        y = self.y * escalar
        return x, y
    def __truediv__(self, escalar):
        x = self.x / escalar
        y = self.y / escalar
        return x, y
    def ModificarPosX(self, x):
        self.x = x
    def ModificarPosY(self, y):
        self.y = y
    def CalcularMagnitud(self):
        return math.sqrt(pow(self.x,2) + pow(self.x,2))
    
class Usuario():
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id=id
        self.status=True
        
class Pelicula():
    def __init__(self, id, nombre, duracion):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion
        self.usuarios=[]
        self.rating = []

        


            
