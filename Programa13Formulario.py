from venv import create
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
from PyQt6.QtWidgets import *
import qdarktheme

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.create_layout()
        
        

    def create_layout(self):
       
        layout = QGridLayout()
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        boton = QPushButton('Ingresar', clicked=self.validar)

        etiquetas['Usuario'] = QLabel('Usuario')
        etiquetas['Contraseña'] = QLabel('Contraseña')
        
     
        self.resultado = QLabel('')
        self.campos_texto['Usuario'] = QLineEdit()
        self.campos_texto['Contraseña'] = QLineEdit()


        layout.addWidget(etiquetas['Usuario'], 0, 0,1,1)
        layout.addWidget(self.campos_texto['Usuario'], 0, 1,1,1)
        layout.addWidget(etiquetas['Contraseña'], 1, 0,1,1)
        layout.addWidget(self.campos_texto['Contraseña'], 1, 1,1,1)
        
       
        layout.addWidget(self.resultado, 3, 0,1,1)
        
        layout.addWidget(boton,3,2,1,1)
        
    def validar(self):
        
        credusr="admin"
        credpas="123"
        usr=self.campos_texto['Usuario'].text()
        pas=self.campos_texto['Contraseña'].text()
        
        if usr==credusr and pas==credpas:
            self.resultado.setText("Sí es correcto :)")
        else:
            self.resultado.setText("Es incorrecto :(")
        

    

app = QApplication(sys.argv)
app.setStyleSheet(qdarktheme.load_stylesheet())




window = MainWindow()

window.show()

app.exec()