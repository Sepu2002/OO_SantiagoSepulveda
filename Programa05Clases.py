import matplotlib.pyplot as plt
import math as m
class Persona():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def actualizarInfo(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        pass
class Pelicula():
    def __init__(self, titulo, anio):
        self.titulo="Hunter Killer"
        self.anio = anio
        self.clasificacion=""
        self.genero=""
        self.pais=""
        self.duracion=0
        self.rating=[]
        self.director=""
        pass