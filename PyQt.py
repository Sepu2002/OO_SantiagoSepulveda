## Clases y Subclases (Herencia)
# class Persona():
#     def __init__(self, nombre, edad):
#         self.name = nombre
#         self.age = edad

# class Ingeniero(Persona):
#     def __init__(self, nombre, edad, carrera):
#         super().__init__(nombre, edad)
#         self.bachelor = carrera

# mi_persona = Persona("Claudio", 18)
# mi_ingeniero = Ingeniero("Claudio", 18, "Mecatronica")

# print(mi_ingeniero.bachelor)

## Mi primera ventana
# from PyQt6.QtWidgets import QApplication, QWidget
# import sys

# app = QApplication(sys.argv)

# window = QWidget()
# window.show()

# app.exec()

# # Creacion de un boton
# from PyQt6.QtWidgets import QApplication, QPushButton
# import sys

# app = QApplication(sys.argv)

# window = QPushButton("Push Me!")
# window.show()

# app.exec()

## Creacion de una Main Window
# from PyQt6.QtWidgets import QApplication, QMainWindow
# import sys

# app = QApplication(sys.argv)

# window = QMainWindow()
# window.show()

# app.exec()

## Creacion de nuestra clase MainWindow
from venv import create
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
from PyQt6.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana")
        self.setWindowIcon(QIcon('./logo.png'))
        self.setFixedSize(1280,720)
        self.create_layout()
        self.setCentralWidget(self.wid)
        #boton = QPushButton("Presioname!")

    def create_layout(self):
        self.wid = QWidget()
        layout = QGridLayout()
        self.wid.setLayout(layout)

        etiquetas = {}
        self.campos_texto = {}
        boton = QPushButton('Ingresar')

        etiquetas['Usuario'] = QLabel('Nombre de Usuario')
        etiquetas['Contrasenia'] = QLabel('Contraseña')
        self.campos_texto['Usuario'] = QLineEdit()
        self.campos_texto['Contrasenia'] = QLineEdit()


        layout.addWidget(etiquetas['Usuario'], 0, 0, 1, 1)
        layout.addWidget(self.campos_texto['Usuario'], 0, 2, 1, 2)
        layout.addWidget(etiquetas['Contrasenia'], 1, 0, 1, 1)
        layout.addWidget(self.campos_texto['Contrasenia'], 1, 1, 1, 3)
        layout.addWidget(boton,3,3,1,1)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()