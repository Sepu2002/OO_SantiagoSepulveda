
#from PyQt6.QtWidgets import QApplication, QWidget
#import sys
#
#app=QApplication(sys.argv)
#
#window= QWidget()
#window.show()
#
#app.exec()

#from PyQt6.QtWidgets import QApplication, QPushButton
#import sys
#
#app=QApplication(sys.argv)
#
#window= QPushButton("Picame")
#window.show()
#
#app.exec()

#from PyQt6.QtWidgets import QApplication, QMainWindow
#import sys
#
#app=QApplication(sys.argv)
#
#window= QMainWindow
#window.show()
#
#app.exec()
from PyQt6.QtCore import * 
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi preimera ventana")
        boton = QPushButton("Presioname")
        self.setCentraWidget(boton)

app=QApplication(sys.argv)

window= MainWindow()
window.show()

app.exec()