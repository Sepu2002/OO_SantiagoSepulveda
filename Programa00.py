import math as m
import calendar as cal
import os
import platform as plat

def clear_console():
    os_name=plat.system()
    if os_name=="Windows":
        os.system('cls')
    else:
        os.system('clear')
        
name=input("Ingresa tu nombre: ")
matr=input("Ingresa tu ID: ")
age=input("Ingresa tu edad: ")
while True:
    clear_console()
    print("Hola "+ name+", tu matrícula es "+ matr +". Seleciona una opción:")
    print("1. Obten el perímetro y el área de un rectángulo")
    print("2. Encuentra el Seno y Coseno de un número")
    print("3. Ingresa un número y obten los 5 números consecutivos siguientes")
    print("4. Encontrar el mayor de 2 números")
    print("5. Checar si un año es bisiesto")
    print("6. Checar si un número es par")
    selec=int(input("Ingrese una opción "))
    
    if selec==1:
        clear_console()
        bas=int(input("Introduce una la base del rectángulo (cm): "))
        hal=int(input("Introduce la altura del rectángulo (cm): "))
        per=(bas*2)+(hal*2)
        area=bas*hal
        print(str(area) +"cm cuadrados")
        input()
        
    elif selec==2:
        clear_console()
        ang=float(input("Introduzaca un ángulo "))
        print("el Coseno es: "+str(m.cos(m.radians(ang))))
        print("el Seno es: "+str(m.sin(m.radians(ang))))
        input()
        
    elif selec==3:
        clear_console()
        num=int(input("Introduce un número "))
        print("Los 5 siguientes números son:")
        for n in 4:
            print(str(num))
            num=num+1
        input()  
          
    elif selec==4:
        clear_console()
        prim=int(input("introduce el primer número "))
        sec=int(input("Introduce el 2o número "))
        if prim > sec:
            print(str(prim) + " es el número más grande")
        if sec > prim:
            print(str(sec) + " es el número más grande")
        if sec == prim:
            print("Los números son iguales")
        input()   
         
    elif selec==5:
       clear_console()
       year=int(input("Introduce un año para verificar si es bisiesto "))
       check=cal.isleap(year)
       if check==True:
           print(year, "Es un año bisiesto")
       else:
           print(year, "NO es año bisiesto")
       input()   
        
    elif selec==6:
        clear_console()
        num=int(input("Escribe un número para saber si es par o non "))
        if num%2==0:
            print(num, "Es par")
        else:
            print(num, "No es par")
        input()
        
    else:
        print("opción inválida")
        input()
       