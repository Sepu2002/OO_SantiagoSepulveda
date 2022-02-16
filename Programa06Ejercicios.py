
import matplotlib.pyplot as plt
import math
import numpy as np
import os
import platform as plat



def clear_console():
    os_name=plat.system()
    if os_name=="Windows":
        os.system('cls')
    else:
        os.system('clear')        
def programa1():
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
def programa2(): #Programa 2 resuelt con lo visto en clase
    T=int(input("ingerese el número de puntos que quiere visualizar en la gráfica: " ))
    minx, maxx = -20, 20
    dx = (maxx-minx)/T
    xs=[]
    ys=[]
        
    for i in range(T+1): xs.append(minx+dx*i)
    for i in range(T+1):
        x=xs[i]
        y=math.e**abs(-x)* math.cos(2 * math.pi * x)
        ys.append(y)
        
    N=1000
    minw, maxw = -20, 20
    dw = (maxw-minw)/N
    ws=[]
    zs=[]
    
    for i in range(N+1): ws.append(minx+dw*i)
    for i in range(N+1):
        w=ws[i]
        z=math.e**abs(-w)* math.cos(2 * math.pi * w)
        zs.append(z)


    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(xs, ys, 'o', color='blue')
    plt.plot(ws, zs, 'r', color='black')
    plt.grid()
    plt.show()
    pass
def programa3():
  class Persona():
        def __init__(self, nombre, edad, genero,id):
            self.nombre = nombre
            self.edad = edad
            self.genero = genero
            self.id=id

  class Mascota():
        def __init__(self, nombre, edad, raza,id):
            self.nombre = nombre
            self.edad = edad
            self.raza = raza
            self.id=id
 
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
  id_mascotas=0
  id_clientes=0
  id_adopcion=0

  cont=0
  while cont==0:
      
      clear_console()
      print("1-Alta de mascota")
      print("2-Alta de usuario")
      print("3-Ver mascotas en el sistema")
      print("4-Ver usuarios en el sistema")
      print("5-Realizar una adopción")
      print("6-Ver todas las adopciones")
      print("7-Salir")
      selec=int(input("Selecciona una opción: "))
      
      if selec==1: #Dar de alta una mascota
        nombre=input("Ingresa el nombre de la mascota: ")
        edad=int(input("Ingresa la edad de la mascota: "))
        raza=input("Ingresa la raza de la mascota: ")
        id_mascotas+=1
        MascotaTemporal= Mascota( nombre , edad , raza, id_mascotas)
        Mascotas.append(MascotaTemporal)  
        
        
      elif selec==2: #Dar de alta a un usuario
        nombre=input("Ingresa el nombre del cliente: ")
        edad=int(input("Ingresa la edad del cliente: "))
        genero=input("Ingresa la el genero del cliente: ")
        id_clientes+=1
        MascotaTemporal= Persona( nombre , edad , genero, id_clientes)
        Clientes.append(MascotaTemporal)
        
      elif selec==3: #ver mascotas en el sistema
          for i in range (0, len(Mascotas)):
                
                print(Mascotas[i].nombre)
                print(Mascotas[i].edad)
                print(Mascotas[i].raza)
                print(Mascotas[i].id)
                print("")
          input("presione enter")
          
      elif selec==4:
        for i in range (0, len(Clientes)):
                
                print(Clientes[i].nombre)
                print(Clientes[i].edad)
                print(Clientes[i].genero)
                print(Clientes[i].id)
                print("")
        input("presione enter")
      elif selec==5:
        id_Cliente_adoptador=int(input("Ingresa el id del cliente que desea adoptar: "))
        id_mascota_adoptada=int(input("Ingresa el id de la mascota que quiere adoptar: "))
        id_adopcion+=1
        Adopcion['ID Adopcion']=id_adopcion
        Adopcion['Dueño']=Clientes[id_Cliente_adoptador-1].nombre
        Adopcion['ID Dueño']=Clientes[id_Cliente_adoptador-1].id
        Adopcion['Mascota']=Mascotas[id_mascota_adoptada-1].nombre
        Adopcion['ID Mascota']=Mascotas[id_mascota_adoptada-1].id
        Adopciones.append(Adopcion)
        input("Adopción exitosa")
        
      elif selec==6:
         clear_console()
         for i in range (0, len(Adopciones)):
            print(Adopciones[i])
         input("presione enter para continuar") 
            
      elif selec==7:
          cont+=1

cont=0 
clear_console()
while cont==0:
    clear_console()
    print("1- Despliega puntos en una recta")
    print("2- Despliega puntos dentro de la función f(x) = e^-|x| cos(2 * PI * x)")
    print("3- Programa veterinario")
    print("4- Cerrar programa")
    selec = int(input("Selecciona una opción"))

    if selec==1:
        print("programa 1")
        programa1()
    elif selec==2:
        print("programa 2")
        programa2()
    elif selec==3:
        print("programa 3")
        programa3()
    elif selec==4:
        cont=+1
    else:
        print("Opción inválida")
clear_console()
print('''
                         ______                     
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  Finalizado:   | |             
|:______B:|      | |                | |             
|:______B:|      | |  System        | |             
|         |      | |  Shutoff.      | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:
      
      ''')

    