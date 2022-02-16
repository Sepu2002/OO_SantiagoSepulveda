from ast import Pass
import matplotlib.pyplot as plt
import numpy as np
import math
from msilib.schema import Class
import os
import platform
from tkinter import Menu

def clear_console():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')

def Imprimir_Menu():
    print("Ejercicios tipo examen")
    print("Menu:")
    print("1) Programa 1 ")
    print("2) Programa 2 ")
    print("3) Programa 3 ")
    print("4) Salir")

def Ejecutar_Opcion():
    CorrerPrograma=True
    while CorrerPrograma:
        clear_console()
        Imprimir_Menu()
        opcion=int(input("Ingrese la opcion del programa que desea visitar: "))
        if opcion==1:  # Programa 1
            Programa01()
        elif opcion==2:  # Programa 2
            Programa02()
        elif opcion==3:  # Programa 3
            Programa03()
        elif opcion==4:  # Salir
                input("Gracias por utilizar el programa :) ")
                CorrerPrograma=False
        else:            
            input(print("Esta no es una alternativa... "))

# La ecuacion de la recta parametrica se define como: 
# Res(x,y) = A(1 - T) * BT, donde A y B son dos puntos con coordenadas 'x' y 'y', y T 
# un intervalo en el tiempo entre 0 <= T <= 1. Realice un programa donde el usuario ingresa 
# la cantidad de puntos que desea ver dentro de la linea y realizar el calculo de los puntos 
# y desplegarlos en una grafica.

def Programa01():
    clear_console()
    T=int(input("Ingerese el número de puntos que quiere visualizar en la gráfica: " ))
    minx, maxx = 0, 20 #Terminas los límites de la gráfica
    dx = (maxx-minx)/T #Calculas las subdivisiones en la gráfica
    xs=[] #Declaras los arreglos vacíos para todos los valores en x y y de los puntos
    ys=[]
    
    A=[0,0] #Pones tus puntos A y B de la recta con sus respectivos valores
    B=[20,20]
    
    ws=[A[0],B[0]] #Generas arreglos para que pyplot los grafique como una función
    zs=[A[1],B[1]]
        
    for i in range(T+1): 
        xs.append(minx+dx*i) #Agregas al arreglo de puntos en x todos los valores en x dependiendo de las divisiones que pide el usuario
        
    for i in range(T+1):
        x=xs[i]
        y=x #Generas una función en la que y depende de cada uno de los valores de x.
        ys.append(y) #vas agregando los valores de y al arreglo de las ys.
    
    plt.plot(ws, zs, 'r', color='black')
    plt.plot(xs, ys, 'o', color='blue')
    plt.grid()
    plt.show()
    pass

# Realice la grafica de la siguiente funcion f(x) = e^|-x| cos(2 * PI * x), 
# El usuario debe ingresar cuantos puntos desea generar y se debe de mostrar en pantalla
#  la grafica resultante
def Programa02():
    clear_console()
    t=int(input("Ingrese el número de puntos que aparezcan en la gráfica: "))

    x=np.linspace(-10,10,1000)
    y=math.e**abs(-x) *np.cos(2 * math.pi * x)

    z=np.linspace(-10,10,t)
    w=math.e**abs(-z) *np.cos(2 * math.pi * z)

    plt.plot(x,y,'r')
    plt.plot(z,w,'ro', color='black')
    plt.show()
    pass
   



# Realice un programa de una veterinaria con las siguientes opciones: 
    # Alta de Mascota
    # Alta de usuario
    # Ver Mascostas en Sistema
    # Ver Usuarios en Sistema
    # Realizar una adopcion
    # Ver adopciones
    # Salir

def Programa03():

    class Persona():
        def _init_(self, nombre, edad, genero,id):
            self.nombre = nombre
            self.edad = edad
            self.genero = genero
            self.id=id
        def Saludo(self):
            print(f"Hola soy {self.nombre}") 

    class Mascota():
        def _init_(self, nombre, edad, raza,id):
            self.nombre = nombre
            self.edad = edad
            self.raza = raza
            self.id=id
        def Saludo(self):
            print(f"Hola soy {self.nombre}") 

    # class Adopcion():
    #     def _init_(self, adoptador,adoptado) :
    #         self.adopador=adoptador
    #         self.adoptado=adoptado

    Mascotas=[]
    Clientes=[]
    Adopciones=[]

    Adopcion={
        'ID Adopcion' : 0,
        'Dueño' : "",
        'ID Dueño' : "",
        'Mascota' : "",
        'ID Mascota' : 0,
    }

    # Adopciones=[]

    def Imprimir_Menu_Vet():
        print("Programa 03")
        print("Menu:")
        print("1) Alta mascota ")
        print("2) Alta usuario ")
        print("3) Ver mascotas en el sistema ")
        print("4) Ver usarios en el sistema ")
        print("5) Realizar Adopcion ")
        print("6) Ver Adopciones: ")
        print("7) Salir")

    def Ejecutar_Opcion():
        CorrerPrograma=True
        id_mascotas=0
        id_clientes=0
        id_adopcion=0
        while CorrerPrograma:
            clear_console()
            Imprimir_Menu_Vet()
            opcion=int(input("Ingrese la opcion del programa que desea visitar: "))
            if opcion==1:  # Alta de Mascota
                clear_console()
                nombre=input("Ingresa el nombre de la mascota: ")
                edad=int(input("Ingresa la edad de la mascota: "))
                raza=input("Ingresa la raza de la mascota: ")
                id_mascotas+=1
                MascotaTemporal= Mascota( nombre , edad , raza, id_mascotas)
                Mascotas.append(MascotaTemporal)
                input("Mascota agregada exitosamente")

            elif opcion==2:  # Alta de usuario
                clear_console()
                nombre=input("Ingresa el nombre del cliente: ")
                edad=int(input("Ingresa la edad del cliente: "))
                genero=input("Ingresa la el genero del cliente: ")
                id_clientes+=1
                MascotaTemporal= Persona( nombre , edad , genero, id_clientes)
                Clientes.append(MascotaTemporal)
                input("Cliente agregado exitosamente")

            elif opcion==3:  # Ver Mascostas en Sistema
                clear_console()
                for i in range (0, len(Mascotas)):
                    print(f"{Mascotas[i].nombre} tiene {Mascotas[i].edad} años es un {Mascotas[i].raza} y su id es {Mascotas[i].id}")
                input("presione enter para continuar...")

            elif opcion==4:  # Ver Usuarios en Sistema
                clear_console()
                for i in range (0, len(Mascotas)):
                    print(f"{Clientes[i].nombre} tiene {Clientes[i].edad} años su género es {Clientes[i].genero} y su id es {Clientes[i].id}")
                input("presione enter para continuar...")

            elif opcion==5:  # Realizar una adopcion
                clear_console()
                id_Cliente_adoptador=int(input("Ingresa el id del cliente que desea adoptar: "))
                id_mascota_adoptada=int(input("Ingresa el id de la mascota que quiere adoptar: "))
                
                for i in range(0,len(Clientes)):
                    if(id_Cliente_adoptador==Clientes[i].id):
                        Cliente_Encontrado=True
                        x_cliente=i
                    else:
                        input("Cliente no encontrado...")
                
                for i in range(0,len(Mascotas)):
                    if(id_mascota_adoptada==Mascotas[i].id):
                        Mascota_Encontrada=True
                        x_mascota=i
                    else:
                        input("Mascota no encontrada...")

                if Cliente_Encontrado and Mascota_Encontrada:
                        Mascota_y_Cliente_encontrado=True

                
                if Mascota_y_Cliente_encontrado:
                        id_adopcion+=1
                        Adopcion['ID Adopcion']=id_adopcion
                        Adopcion['Dueño']=Clientes[x_cliente].nombre
                        Adopcion['ID Dueño']=Clientes[x_cliente].id
                        Adopcion['Mascota']=Mascotas[x_mascota].nombre
                        Adopcion['ID Mascota']=Mascotas[x_mascota].id
                        Adopciones.append(Adopcion)
                        input("Adopción exitosa :)")
                    

            elif opcion==6:  # Ver adopciones
                clear_console()
                for i in range (0, len(Adopciones)):
                    print(Adopciones[i])
                input("presione enter para continuar...")

            elif opcion==7:  # Salir
                clear_console()
                input("Gracias por utilizar el programa de adopción de perros :) ")
                CorrerPrograma=False
                
            else: 
                input(print("Esta no es una alternativa... "))    
    
    Ejecutar_Opcion()       
            


Ejecutar_Opcion()