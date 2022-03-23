# 1- Punto = A(1-T)+BT
#El usuario introduce 2 puntos inicialmente y tira una recta, posteriormente introduce un 3o y verifica si el punto se encuentra en la recta

# 2- El usuario de 4 puntos inicialmente, qeu equivalen a las esquinas de un cuadrilátero, posteriormente se ingresa un 5o y se verifica si el punto se encuentra dentro del área del cuadilatero


# 3-Programa de películas. 
# 1-Alta Usuario
# 2-Baja de usuario (desactivar)
# 3-Ver lista de usuarios activos
# 4-Ver lista de usuarios inactivos
# 5-Alta película
# 6-Baja de película (eliminar)
# 7-Ver películas
# 8
# 9
# 10-Salir

from clases import Usuario
from clases import Pelicula
from clases import Punto2D
import matplotlib.pyplot as plt
import math
import os
import platform

def LimpiarConsola():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')
               
def Programa1():
    LimpiarConsola()
    pt1 = Punto2D(float(input("Introduce el componente en X del primer punto")), float(input("Introduce el componente en Y del primer punto")))
    pt2 = Punto2D(float(input("Introduce el componente en X del segundo punto")), float(input("Introduce el componente en Y del segundo punto")))
    pt3 = Punto2D(float(input("Introduce el componente en X del tercer punto")), float(input("Introduce el componente en Y del tercer punto")))
    
    resul = check_en_entre(pt1,pt2,pt3)
    rectax=[pt1.x, pt2.x]
    rectay=[pt1.y, pt2.y]
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    plt.plot(rectax,rectay, 'r', color='white')
    plt.plot(rectax,rectay, 'o', color='blue')
    
    print(resul)
    
    if resul==True:
        ax.set_title("El punto está entre los puntos y en la recta")
        plt.plot(pt3.x, pt3.y,'o', color='limegreen')
    else:
        ax.set_title("El punto NO está entre los puntos y en la recta")
        plt.plot(pt3.x, pt3.y, 'o', color='red')
    plt.grid()
    plt.show()
    
    pass   

def check_en_entre(pt1,pt2,pt3):
        pend = (pt2.y - pt1.y) / (pt2.x - pt1.x)
        pt3_en = (pt3.y - pt1.y) == pend * (pt3.x - pt1.x)
        pt3_entre = (min(pt1.x, pt2.x) <= pt3.x <= max(pt1.x, pt2.x)) and (min(pt1.y, pt2.y) <= pt3.y <= max(pt1.y, pt2.y))
        en_y_entre = pt3_entre and pt3_en
        return en_y_entre
    
def Programa2():
    LimpiarConsola()
    
    pt1=Punto2D(0.0,0.0)
    pt2=Punto2D(-3.535534,3.533334)
    pt3=Punto2D(1.414214, 8.485281)
    pt4=Punto2D(4.949748, 4.949748)
    pt5=Punto2D(float(input("Ingrese X del punto a checar")),float(input("Ingrese Y del punto a checar")))
    
    recta1x=[pt1.x, pt4.x]
    recta1y=[pt1.y, pt4.y]
    
    recta2x=[pt4.x, pt3.x]
    recta2y=[pt4.y, pt3.y]
    
    recta3x=[pt3.x, pt2.x]
    recta3y=[pt3.y, pt2.y]
    
    recta4x=[pt2.x, pt1.x]
    recta4y=[pt2.y, pt1.y]
    
    plt.plot(recta1x,recta1y, 'r', color='red')
    plt.plot(recta2x,recta2y, 'r', color='red')
    plt.plot(recta3x,recta3y, 'r', color='red')
    plt.plot(recta4x,recta4y, 'r', color='red')

    base=math.sqrt(((pt4.x-pt1.x)**2)+((pt4.y-pt1.y)**2))
    altura=math.sqrt(((pt2.x-pt1.x)**2)+((pt2.y-pt1.y)**2))
    areaRect=round(base*altura,3)

    areaT1=abs(((pt1.x*pt2.y)+(pt2.x*pt5.y)+(pt5.x*pt1.y)-(pt1.y*pt2.x)-(pt2.y*pt5.x)-(pt5.y*pt1.x))/2)
    areaT2=abs(((pt2.x*pt3.y)+(pt3.x*pt5.y)+(pt5.x*pt2.y)-(pt2.y*pt3.x)-(pt3.y*pt5.x)-(pt5.y*pt2.x))/2)
    areaT3=abs(((pt3.x*pt4.y)+(pt4.x*pt5.y)+(pt5.x*pt3.y)-(pt3.y*pt4.x)-(pt4.y*pt5.x)-(pt5.y*pt3.x))/2)
    areaT4=abs(((pt4.x*pt1.y)+(pt1.x*pt5.y)+(pt5.x*pt4.y)-(pt4.y*pt1.x)-(pt1.y*pt5.x)-(pt5.y*pt4.x))/2)
    #1 y 2
    #2 y 3
    #3 y 4
    #4 y 1
    areaT=areaT1+areaT2+areaT3+areaT4
    
    resul=(areaT-areaRect)<1
    
    #print(areaT)
    #print(areaRect)
   
    
    
   
    if resul==True:
        plt.gca().set_title("El punto está dentro del rectángulo")
        plt.plot(pt5.x, pt5.y,'o', color='limegreen')
        
        
    else:
        plt.gca().set_title("El punto NO está dentro del rectángulo")
        plt.plot(pt5.x, pt5.y, 'o', color='red')
        
    plt.style.use('dark_background')  
    plt.grid() 
    plt.show()

def Programa3():
    cont=True
    Peliculas=[]
    Usuarios=[]
    id_usuarios = 0
    id_peliculas = 0
    while cont:
        LimpiarConsola()
        imprimeMenu()
        
        
        selec=int(input("Selecciona una opción: "))
        if selec==1:
            LimpiarConsola()
            print("Alta Usuario:")
            nombre=input("Ingresa el nombre del usuario: ")
            UsuarioTemporal= Usuario(nombre, id_usuarios)
            Usuarios.append(UsuarioTemporal)
            id_usuarios+=1
            input("Usuario agregado exitosamente")

            pass
        elif selec==2:
            LimpiarConsola()
            print("Desactiva Usuario:")
            id=int(input("Ingresa el id del cliente que busca desactivar: "))
            ClienteExiste=False
            for i in range (0, len(Usuarios),1):
                if id==Usuarios[i].id:
                    ClienteExiste=True
                    x_usuario=i

            if ClienteExiste==True:
                Usuarios[x_usuario].status=False
                input("Usuasio desactivado exitosamente")
            else:
                input("Usuario no encontrado...")
            pass
        elif selec==3:
            LimpiarConsola()
            print("Restablecer Usuario:")
            id=int(input("Ingresa el id del cliente que busca restablecer: "))
            ClienteExiste=False
            for i in range (0, len(Usuarios),1):
                if id==Usuarios[i].id:
                    ClienteExiste=True
                    x_usuario=i

            if ClienteExiste==True:
                Usuarios[x_usuario].status=True
                input("Usuasio restablecido exitosamente")
            else:
                input("Usuario no encontrado...")
            pass
        
        elif selec==4:
            LimpiarConsola()
            print("Lista Usuarios Activos:")
            print(f"Nombre:  \t ID:  ")
            for i in range (0, len(Usuarios),1):
                if Usuarios[i].status:
                    print(f"{Usuarios[i].nombre} \t  {Usuarios[i].id} ")
                    
            input("presione enter para continuar...")
            pass
        
        elif selec==5:
            LimpiarConsola()
            print("Lista Usuarios Inctivos:")
            print(f"Nombre:  \t ID:  ")
            for i in range (0, len(Usuarios),1):
                if Usuarios[i].status==False:
                    print(f"{Usuarios[i].nombre} \t  {Usuarios[i].id} ")

            input("presione enter para continuar...")
            pass
        
        elif selec==6:
            LimpiarConsola()
            print("Alta pelicula: ")
            nombre=input("Ingresa el nombre de la pelicula: ")
            duracion=input("Ingresa la duracion de la pelicula: ")
            PeliculaTemporal= Pelicula( id_peliculas,nombre , duracion)
            Peliculas.append(PeliculaTemporal)
            id_peliculas+=1
            input("Pelicula agregada exitosamente")
            pass
        
        elif selec==7:
            LimpiarConsola()
            print("Baja pelicula: ")
            id=int(input("Ingresa el id de la pelicula que desea eliminar: "))
            PeliExiste=False
            for i in range (0, len(Peliculas),1):
                if id==Peliculas[i].id:
                    PeliExiste=True
                    x_peli=i

            if PeliExiste==True:
                Peliculas.pop(x_peli)
                input("Pelicula eliminada exitosamente")
            else:
                input("Pelicula no encontrada...")

            pass
        elif selec==8:
            LimpiarConsola()
            id=int(input("Ingresa el id de la pelicula que desea calificar: "))
            id_usuario_busca=int(input("Ingresa el id del usuario que va a calificar: "))
            PeliExiste=False
            UsuarioExiste=False
            for i in range (0, len(Peliculas),1):
                if id==Peliculas[i].id:
                    PeliExiste=True
                    x_peli=i
                else:
                    input("Pelicula no encontrado...")


            for i in range (0, len(Usuarios),1):
                if id_usuario_busca==Peliculas[i].id:
                    UsuarioExiste=True
                    x_usuario=i 
                else:
                    input("Usuario no encontrado...")       

            if PeliExiste==True and UsuarioExiste==True:
                print(f"{Peliculas[x_peli].nombre} \t ID: {Peliculas[x_peli].id} :")
                calificacion=input(f"{Usuarios[x_usuario].nombre} inserte la calificacion que desea darle a la pelicula del 1-5 en * : ")
                Peliculas[x_peli].rating.append(calificacion)
                Peliculas[x_peli].usuarios.append(Usuarios[x_usuario].nombre)
                input("Calificacion guardada exitosamente...")
                      
            pass
        
        elif selec==9:
            LimpiarConsola()
            id=int(input("Ingresa el id de la pelicula que desea  modificar calificacion: "))
            id_usuario_busca=int(input("Ingresa el id del usuario que va modificar calificacion: "))
            PeliExiste=False
            UsuarioExiste=False
            Calificacion_Existe=False
            for i in range (0, len(Peliculas),1):
                if id==Peliculas[i].id:
                    PeliExiste=True
                    x_peli=i
                else:
                    input("Pelicula no encontrado...")


            for i in range (0, len(Usuarios),1):
                if id_usuario_busca==Usuarios[i].id:
                    UsuarioExiste=True
                    x_usuario=i 
                else:
                    input("Usuario no encontrado...")    

            if i in range (0, len(Peliculas[x_peli].usuarios),1):
                if Usuarios[x_usuario].nombre==Peliculas[x_peli].usuarios[i]:
                    Calificacion_Existe=True
                    calif_index=i
                else:
                    print("Claificacion no encontrada...")

            if PeliExiste==True and UsuarioExiste==True and Calificacion_Existe==True:
                print(f"{Peliculas[x_peli].nombre} \t ID: {Peliculas[x_peli].id} :")
                calificacion=input(f"{Usuarios[x_usuario].nombre} inserte la nueva calificacion que desea darle a la pelicula del 1-5 en * : ")
                Peliculas[x_peli].rating[calif_index]=calificacion
                  
                input("Calificacion guardada exitosamente...")   
            pass
        
        elif selec==10:
            Peliculas()
            id=int(input("Ingresa el id de la pelicula que desea ver el rating: "))
            PeliExiste=False
            
            for i in range (0, len(Peliculas)):
                if id==Peliculas[i].id:
                    PeliExiste=True
                    x_peli=i

            if PeliExiste==True:
                print(f"{Peliculas[x_peli].nombre} \t ID: {Peliculas[x_peli].id} :")
                for i in range (0, len(Peliculas[x_peli].rating),1):
                    if Peliculas[x_peli].rating[i] !=0:
                        print(Peliculas[x_peli].rating[i])
                    
            else:
                input("Pelicula no encontrado...")
            pass
        
        elif selec==11:
            LimpiarConsola()
            input("Gracias por utilizar el programa vuelva pronto")
            cont = False
        pass
    pass

def imprimeMenu():
    print("1-Alta Usuario")
    print("2-Baja de usuario (desactivar)")
    print("3-Restablecer usuario")
    print("4-Ver lista de usuarios activos")
    print("5-Ver lista de usuarios inactivos")
    print("6-Alta de película")
    print("7-Baja de película (eliminar)")
    print("8-Calificar película")
    print("9-Modificar calificación de usuario a pelicula")
    print("10-Ver calificación de película")
    print("11-Salir")

correr=True

while correr:   
    print("Santiago Sepúlveda Landeros")
    print("Ingeniería Mecatrónica")
    print("0212496")
    print("")
    print("")
    print("1- Punto en linea")
    print("2- Punto en área")
    print("3- IMDB")
    print("4- Cerrar programa")

    opt=int(input("Ingrese una opción"))

    if opt==1:
        Programa1()
    elif opt==2:
        Programa2()
    elif opt==3:
        Programa3()
    elif opt==4:
        input("Vuelva pronto")
        correr=False
        pass
    

