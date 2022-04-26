from venv import create
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
from PyQt6.QtWidgets import *
import qdarktheme
import sys
import csv


     
usuarios=[]
contraseñas=[]
roles=[]
usuario_actual=[0]

class InicioSesion(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Inicio de sesión")
        self.setWindowIcon(QIcon('./key.png'))
        self.create_layout()
        
    def create_layout(self):
        layout = QGridLayout()
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        boton = QPushButton('Ingresar', clicked=self.validar)
        boton.setIcon(QIcon('./check.png'))

        etiquetas['Usuario'] = QLabel('Usuario')
        etiquetas['Contraseña'] = QLabel('Contraseña')
        
        self.actual=QLabel('')
        
     
        self.resultado = QLabel('')
        self.campos_texto['Usuario'] = QLineEdit()
        self.campos_texto['Contraseña'] = QLineEdit()


        layout.addWidget(etiquetas['Usuario'], 0, 0,1,1)
        layout.addWidget(self.campos_texto['Usuario'], 0, 1,1,1)
        layout.addWidget(etiquetas['Contraseña'], 1, 0,1,1)
        layout.addWidget(self.campos_texto['Contraseña'], 1, 1,1,1)
        
       
        layout.addWidget(self.resultado, 3, 0,1,1)
        layout.addWidget(self.actual, 4, 0,1,1)
        layout.addWidget(boton,3,2,1,1)
        
    def validar(self):            
        usr=self.campos_texto['Usuario'].text()
        pas=self.campos_texto['Contraseña'].text()
        
        self.sacarDatos()
        
        if usr in usuarios:
            for i in range(0,len(usuarios)):
               if usr==usuarios[i] and pas==contraseñas[i] and roles[i]=="Admin":
                   usuario_actual[0]=i
                   self.sub_ventana=VentanaAdmin()
                   self.sub_ventana.show()
                   self.hide()
                   
               elif usr==usuarios[i] and pas==contraseñas[i] and roles[i]=="User":
                   usuario_actual[0]=(i)
                   self.sub_ventana=VentanaUser()
                   self.sub_ventana.show()
                   self.hide()
               elif usr==usuarios[i] and pas!=contraseñas[i]:
                   self.resultado.setText("Contraseña incorrecta")
               else:
                   pass
               
               
                    
           
        else:
            self.resultado.setText("Usuario inválido")
            
    def sacarDatos(self):
        with open('Usuarios.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            datos=list(csv_reader)
            #print(datos)
            for i in range(0,len(datos)):
                if datos[i][1] not in usuarios:
                    usuarios.append(datos[i][1])
                    contraseñas.append(datos[i][2])
                    roles.append(datos[i][3])
            csv_file.close()
     
class VentanaAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Admin")
        self.setWindowIcon(QIcon('./AdminImg.png'))
        self.setMinimumSize(300, 100)
        self.create_layout()
        
        

    def create_layout(self):
       
        layout = QGridLayout()
        
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        AddUsr = QPushButton('Agregar Usuario',clicked=self.AU)
        AddUsr.setIcon(QIcon('./add.png'))
        SeeUsr = QPushButton('Ver Usuarios', clicked=self.VU)
        SeeUsr.setIcon(QIcon('./search.png'))
        Info = QPushButton('Ver Información', clicked=self.In)
        Info.setIcon(QIcon('./info.png'))
        Exit = QPushButton('Salir', clicked=self.salir)
        Exit.setIcon(QIcon('./exit.png'))
        

        
        layout.addWidget(AddUsr,0,2,1,1)
        layout.addWidget(SeeUsr,1,2,1,1)
        layout.addWidget(Info,2,2,1,1)
        layout.addWidget(Exit,3,2,1,1)
        
    def AU(self):
        self.sub_ventana=AgregarUsuario()
        self.sub_ventana.show()
        self.hide()
    
    def VU(self):
        self.sub_ventana=VerUsuarios()
        self.sub_ventana.show()
        self.hide()
        
    def In(self):
        self.sub_ventana=VerInfo()
        self.sub_ventana.show()
        self.hide()
        
    def salir(self):
        self.sub_ventana=InicioSesion()
        self.sub_ventana.show()
        self.hide()
               
class VentanaUser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana User")
        self.setWindowIcon(QIcon('./users.png'))
        self.setMinimumSize(300, 100)
        self.create_layout()
        
        

    def create_layout(self):
       
        layout = QGridLayout()
        
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        
        SeeInf = QPushButton('Ver Información',clicked=self.SI)
        SeeInf.setIcon(QIcon('./info.png'))
        Exit = QPushButton('Salir', clicked=self.salir)
        Exit.setIcon(QIcon('./exit.png'))
        

        
        layout.addWidget(SeeInf,1,2,1,1)
        layout.addWidget(Exit,2,2,1,1)
        
    def SI(self):
        self.sub_ventana=VerInfo()
        self.sub_ventana.show()
        self.hide()
        
    def salir(self):
        self.sub_ventana=InicioSesion()
        self.sub_ventana.show()
        self.hide()
        
class AgregarUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agregar Usuario")
        self.setMinimumSize(300, 100)
        self.create_layout()
        
        

    def create_layout(self):
       
        layout = QGridLayout()
        
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        AddUsr = QPushButton('Agregar Usuario',clicked=self.GuardarUsuario)
        AddUsr.setIcon(QIcon('./check.png'))
        Exit = QPushButton('Salir', clicked=self.salir)
        Exit.setIcon(QIcon('./exit.png'))
        etiquetas['Usuario']=QLabel('Usuario')
        etiquetas['Contraseña']=QLabel('Contraseña')
        self.mensaje=QLabel('')
        
        self.combobox1 = QComboBox()
        self.combobox1.addItem('Admin')
        self.combobox1.addItem('User')
        
        self.campos_texto['Usuario']=QLineEdit()
        self.campos_texto['Contraseña']=QLineEdit()

        layout.addWidget(etiquetas['Usuario'], 0,0,1,1) 
        layout.addWidget(etiquetas['Contraseña'], 1,0,1,1)
        layout.addWidget(self.campos_texto['Usuario'], 0,1,1,1)
        layout.addWidget(self.campos_texto['Contraseña'], 1,1,1,1)
        layout.addWidget(self.combobox1,2,1,1,2) 
        layout.addWidget(self.mensaje,3,1,1,2)
        layout.addWidget(AddUsr,4,1,1,1)
        layout.addWidget(Exit,4,0,1,1)
        
    def salir(self):
        self.sub_ventana=VentanaAdmin()
        self.sub_ventana.show()
        self.hide()
        
    def GuardarUsuario(self):
        usr=self.campos_texto['Usuario'].text()
        pas=self.campos_texto['Contraseña'].text()
        rol=self.combobox1.currentText()
        
        if usr not in usuarios:
            
            usuarios.append(usr)
            contraseñas.append(pas)
            roles.append(rol)

            with open('Usuarios.csv', mode='w', newline='') as user_file:
                user_writer = csv.writer(user_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                for i in range(0,len(usuarios)):
                    user_writer.writerow([i, usuarios[i], contraseñas[i], roles[i]])

                user_file.close()
            self.mensaje.setText('Usuario agregado exitosamente')
        else:
            self.mensaje.setText('Usuario ya en uso')
    
class VerUsuarios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ver Usuarios")
        self.setMinimumSize(200, 100)
        self.create_layout()  

    def create_layout(self):
           
        layout = QGridLayout()
        
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        
        Exit = QPushButton('Salir', clicked=self.salir)
        Exit.setIcon(QIcon('./exit.png'))
        
        etiquetas['Info']=QLabel('')
        
        
        table = QTableWidget()
        
        table.setRowCount(len(usuarios))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Usuario", "Rol"])
        table.setVerticalHeaderLabels(["%d" %i for i in range(0,len(usuarios))])
        
        for i in range(0,len(usuarios)):
            
            #ID = QTableWidgetItem(str(i))
            usuario = QTableWidgetItem(usuarios[i])
            #contraseña = QTableWidgetItem(contraseñas[i])
            rol = QTableWidgetItem(roles[i])
            #table.setItem(i,0, ID)
            table.setItem(i,0, usuario)
            #table.setItem(i,2, contraseña)
            table.setItem(i,1, rol)
        
        layout.addWidget(table,0,0,1,1)
        layout.addWidget(Exit,1,0,1,1)
             
    def salir(self):
        self.sub_ventana=VentanaAdmin()
        self.sub_ventana.show()
        self.hide()

class VerInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ver Información")
        self.setMinimumSize(500, 100)
        self.create_layout()  

    def create_layout(self):
           
        layout = QGridLayout()
        
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        
        self.campos_texto['Contraseña']=QLineEdit(contraseñas[usuario_actual[0]])
        
        etiquetas['Usuariot']=QLabel('Usuario: ')
        etiquetas['Usuario']=QLabel(usuarios[usuario_actual[0]])
        etiquetas['Contraseñat']=QLabel('Contraseña: ')
        etiquetas['Header']=QLabel('Datos del usuario: ')
        self.Estado=QLabel('')
        
        Exit = QPushButton('Salir', clicked=self.salir)
        Exit.setIcon(QIcon('./exit.png'))
        Actualizar = QPushButton('Actualizar Contraseña', clicked=self.actPass)
        Actualizar.setIcon(QIcon('./check.png'))

        layout.addWidget(etiquetas['Header'], 0,0,1,1)
        layout.addWidget(etiquetas['Usuariot'], 1,0,1,1)
        layout.addWidget(etiquetas['Usuario'], 1,1,1,1)
        layout.addWidget(etiquetas['Contraseñat'], 2,0,1,1)
        layout.addWidget(self.campos_texto['Contraseña'], 2,1,1,1)
        layout.addWidget(self.Estado, 3,0,1,1)
        layout.addWidget(Exit,4,0,1,1)
        layout.addWidget(Actualizar,4,1,1,1)
         
    def actPass(self):
        contraseñas[usuario_actual[0]]=self.campos_texto['Contraseña'].text()
        self.Estado.setText("Contraseña Actualizada")
        
        with open('Usuarios.csv', mode='w', newline='') as user_file:
            user_writer = csv.writer(user_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            for i in range(0,len(usuarios)):
                user_writer.writerow([i, usuarios[i], contraseñas[i], roles[i]])
                
            user_file.close()
        
        
            
        
    def salir(self):
        if roles[usuario_actual[0]]=='User':
            self.sub_ventana=VentanaUser()
            self.sub_ventana.show()
            self.hide()
        else:
            self.sub_ventana=VentanaAdmin()
            self.sub_ventana.show()
            self.hide()


app = QApplication(sys.argv)
app.setStyleSheet(qdarktheme.load_stylesheet())

start = InicioSesion()
start.show()


app.exec()
