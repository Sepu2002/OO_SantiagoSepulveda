from venv import create
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
from PyQt6.QtWidgets import *
import qdarktheme

import matplotlib.pyplot as plt
import math
import numpy as np
import os
import platform as plat

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio Graficar puntos")
        self.create_layout()
        
        

    def create_layout(self):
       
        layout = QGridLayout()
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        
        botonsum = QPushButton('Sumar', clicked=self.suma)
        botonrest = QPushButton('Restar', clicked=self.resta)
        botonesc = QPushButton('P * a', clicked=self.esc)

        etiquetas['Px'] = QLabel('Px')
        etiquetas['Py'] = QLabel('Py')
        etiquetas['Qx'] = QLabel('Qx')
        etiquetas['Qy'] = QLabel('Qy')
        etiquetas['a'] = QLabel('a')
        etiquetas['Resultado'] = QLabel('Resultado')
        etiquetas['Operacion'] = QLabel('Operación')
        
        self.resultado = QLabel('')
        self.campos_texto['Px'] = QLineEdit()
        self.campos_texto['Py'] = QLineEdit()
        self.campos_texto['Qx'] = QLineEdit()
        self.campos_texto['Qy'] = QLineEdit()
        self.campos_texto['a'] = QLineEdit()



        layout.addWidget(etiquetas['Px'], 0, 0,1,1)
        layout.addWidget(self.campos_texto['Px'], 0, 1,1,1)
        layout.addWidget(etiquetas['Qx'], 0, 2,1,1)
        layout.addWidget(self.campos_texto['Qx'], 0, 3,1,1)
        layout.addWidget(etiquetas['Py'], 1, 0,1,1)
        layout.addWidget(self.campos_texto['Py'], 1, 1,1,1)
        layout.addWidget(etiquetas['Qy'], 1, 2,1,1)
        layout.addWidget(self.campos_texto['Qy'], 1, 3,1,1)
        
        layout.addWidget(etiquetas['a'], 2, 0,1,1)
        layout.addWidget(self.campos_texto['a'], 2, 1,1,1)
        
        layout.addWidget(etiquetas['Resultado'], 2, 2,1,1)
        layout.addWidget(self.resultado, 2, 3,1,1)
        
        layout.addWidget(botonsum,4,1,1,1)
        layout.addWidget(botonrest,4,2,1,1)
        layout.addWidget(botonesc,4,3,1,1)
        
        
    def suma(self):
        Px=int(self.campos_texto['Px'].text())
        Py=int(self.campos_texto['Py'].text())
        Qx=int(self.campos_texto['Qx'].text())
        Qy=int(self.campos_texto['Qy'].text())
        
        resx=(Px+Qx)
        resy=(Py+Qy)
        resxs=str(Px+Qx)
        resys=str(Py+Qy)
        
        res=resxs+', '+resys
        self.resultado.setText(res)
        
        plt.plot(Px, Py, 'o', color='black')
        plt.plot(Qx, Qy, 'o', color='black')
        plt.text(Px,Py,'P', color='red')
        plt.text(Qx,Qy,'Q', color='red')
        plt.plot(resx, resy, 'o', color='blue')
        plt.grid()
        plt.show()
    

    def resta(self):
        Px=int(self.campos_texto['Px'].text())
        Py=int(self.campos_texto['Py'].text())
        Qx=int(self.campos_texto['Qx'].text())
        Qy=int(self.campos_texto['Qy'].text())
        
        resx=(Px-Qx)
        resy=(Py-Qy)
        
        resxs=str(Px-Qx)
        resys=str(Py-Qy)
        
        res=resxs+', '+resys
        self.resultado.setText(res)
        
        plt.plot(Px, Py, 'o', color='black')
        plt.plot(Qx, Qy, 'o', color='black')
        plt.text(Px,Py,'P', color='red')
        plt.text(Qx,Qy,'Q', color='red')
        plt.plot(resx, resy, 'o', color='blue')
        plt.grid()
        plt.show()
    
        
    
    def esc(self):
        Px=int(self.campos_texto['Px'].text())
        Py=int(self.campos_texto['Py'].text())
        a=int(self.campos_texto['a'].text())
        resx=(Px*a)
        resy=(Py*a)
        resxs=str(Px*a)
        resys=str(Py*a)
        res=resxs+', '+resys
        self.resultado.setText(res)
        
        plt.plot(Px, Py, 'o', color='black')
        plt.plot(resx, resy, 'o', color='blue')
        plt.text(Px,Py,'P', color='red')
        plt.grid()
        plt.show()
        
    





app = QApplication(sys.argv)
app.setStyleSheet(qdarktheme.load_stylesheet())




window = MainWindow()

window.show()

app.exec()