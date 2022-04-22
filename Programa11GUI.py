from venv import create
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
from PyQt6.QtWidgets import *
import qdarktheme

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio Suma")
        self.create_layout()
        
        

    def create_layout(self):
       
        layout = QGridLayout()
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        boton = QPushButton('Ingresar', clicked=self.suma)

        etiquetas['Numero 1'] = QLabel('Numero 1')
        etiquetas['Numero 2'] = QLabel('Numero 2')
        etiquetas['Operacion'] = QLabel('Operación')
        etiquetas['AB'] = QLabel('A+B')
        self.resultado = QLabel('')
        self.campos_texto['Numero 1'] = QLineEdit()
        self.campos_texto['Numero 2'] = QLineEdit()


        layout.addWidget(etiquetas['Numero 1'], 0, 0,1,1)
        layout.addWidget(self.campos_texto['Numero 1'], 0, 1,1,1)
        layout.addWidget(etiquetas['Numero 2'], 0, 2,1,1)
        layout.addWidget(self.campos_texto['Numero 2'], 0, 3,1,1)
        layout.addWidget(etiquetas['Operacion'], 1, 0,1,1)
        layout.addWidget(etiquetas['AB'], 1, 1,1,1)
        layout.addWidget(self.resultado, 1, 2,1,1)
        
        layout.addWidget(boton,3,3,1,1)
        
    def suma(self):
        no1=int(self.campos_texto['Numero 1'].text())
        no2=int(self.campos_texto['Numero 2'].text())
        
        res=str(no1+no2)
        
        self.resultado.setText(res)
        
    





app = QApplication(sys.argv)
app.setStyleSheet(qdarktheme.load_stylesheet())




window = MainWindow()

window.show()

app.exec()