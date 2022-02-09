class Persona():
    def __init__(self, nombre, edadP, genero):
        self.nombre= nombre
        self.edadP= edadP
        self.genero= genero
    def Saludo(self):
        print(f"Hola, soy {self.nombre}")
class Ingeniero(Persona):
    def __init__(self, nombre, edadP, genero, area_ingenieria):
        super().__init__(nombre, edadP, genero)
        self.area=area_ingenieria
    def Saludo(self):
        print(f"Hola, soy {self.nombre}")
        print(f"Soy de {self.area}")
        
class Punto2D():
    def __init__(self, posX, posY):
        self.x=posX
        self.y=posY
    def __add__(self, otro_punto):
        #__mul__
        #__sub__
        #__div__
        #__truediv__
        x = self.x + otro_punto.x
        y = self.y + otro_punto.y
        return x, y
        
        
persona_1 = Persona("Santiago",19,"Masculino")
print(persona_1.nombre)
print(persona_1.edadP)
print(persona_1.genero)
persona_1.Saludo()

mi_inge = Ingeniero("Paco", 53, "Masculino", "Ingeniería Civil")
print(mi_inge.nombre)
print(mi_inge.edadP)
print(mi_inge.genero)
print(mi_inge.area)
mi_inge.Saludo()

p = Punto2D(5.0, 1.0)
q = Punto2D(6.4, 3.6)

print(p+q)
