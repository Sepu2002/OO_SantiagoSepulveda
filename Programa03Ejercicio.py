import os
import platform
def clear_console():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    else: # macOS o Linux
        os.system('clear')
def selecinfo(lib):
    print("1-Nombre del libro")
    print("2-Autor")
    print("3-Edición")
    print("4-Editorial")
    infoselec=int(input("Selecciona la información que deseas cambiar"))
    if infoselec==1:
        lib['Nombre']=input("Ingrese Nombre del libro: ")
    if infoselec==2:
        lib['Autor']=input("Ingrese Autor del libro: ")
    if infoselec==3:
        lib['Edición']=input("Ingrese Edición del libro: ")
    if infoselec==4:
        lib['Editorial']=input("Ingrese Editorial del libro: ")
def armstrong():
    lim=int(input("Ingrese un número: "))
    print("Los números Armstrong entre 1 y " + str(lim) + " son: ")
    for num in range(2, lim+1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num, end=',')
    print("")   
def libros(): 
    libone = {
        'Nombre':'Magnus Chase',
        'Autor':'Rick Riordan',
        'Edición': '1',
        'Editorial':'Hachette Books',
        'Inventario':'1'
    }
    libtwo = {
        'Nombre':'Inkheart',
        'Autor':'Cornelia Funke',
        'Edición': '4',
        'Editorial':'Scholastic',
        'Inventario':'5'
    }
    libthree = {
        'Nombre':'100 años de soledad',
        'Autor':'Gabriel García Marquez',
        'Edición': '50',
        'Editorial':'Scholastic',
        'Inventario':'5'
    }
    libfour = {
        'Nombre':'',
        'Autor':'',
        'Edición':'',
        'Editorial':'',
        'Inventario':''
    }
    correr_prog= True
    while correr_prog==True:
        clear_console()
        print("1-Modificar inventario de un libro")
        print("2-Cambiar información de un libro")
        print("3-Ver información de un libro")
        print("4-Agregar un libro")
        print("5-Salir")
        selec = int(input("Selecciona una opción: "))
        clear_console()
        if selec==1:
            print("1-Libro 1")
            print("2-Libro 2")
            print("3-Libro 3")
            print("4-Libro 4") 
            selecb=int(input("Selecciona un libro para cambiar su cantidad en inventario: "))
            if selecb==1:
                lib=libone
                lib["Inventario"]=input("Itroduzca la cantidad de este libro en inventario: ")
            elif selecb==2:
                lib=libtwo
                lib["Inventario"]=input("Itroduzca la cantidad de este libro en inventario: ")
            elif selecb==3:
                lib=libthree
                lib["Inventario"]=input("Itroduzca la cantidad de este libro en inventario: ")
            elif selec==4:
                lib=libfour
                lib["Inventario"]=input("Itroduzca la cantidad de este libro en inventario: ")
            else:
                lib=libfour
                lib["Inventario"]=input("Itroduzca la cantidad de este libro en inventario: ")       
        elif selec==2:
            print("1-Libro 1")
            print("2-Libro 2")
            print("3-Libro 3")
            print("4-Libro 4") 
            selecb=int(input("Selecciona un libro para cambiar su información: "))
            if selecb==1:
                lib=libone
                selecinfo(lib)
            elif selecb==2:
                lib=libtwo
                selecinfo(lib)
            elif selecb==3:
                lib=libthree
                selecinfo(lib)
            elif selec==4:
                lib=libfour
                selecinfo(lib)
            else:
                lib=libfour
                selecinfo(lib)
        elif selec==3:
            print("1-Libro 1")
            print("2-Libro 2")
            print("3-Libro 3")
            print("4-Libro 4") 
            selecb=int(input("Selecciona un libro para ver su información: "))
            if selecb==1:
                print(libone)
                input("Presione enter")
            elif selecb==2:
                print(libtwo)
                input("Presione enter")
            elif selecb==3:
                print(libthree)
                input("Presione enter")
            elif selec==4:
               print(libfour)
               input("Presione enter")
        
            else:
               print(libfour)
               input("Presione enter")

        elif selec==4:
             libfour["Nombre"]=input("Ingrese Nombre del libro: ")
             libfour["Autor"]=input("Ingrese Autor del libro: ")
             libfour["Edición"]=int(input("Ingrese Edición del libro(int): "))
             libfour["Editorial"]=input("Ingrese Editorial del libro: ")
        elif selec==5:
                correr_prog=False     
             
             
def datos_a_mostrar(numCli, nomCli, cantEn):
    print(f"El numero de cliente es              : {numCli}")
    print(f"El nombre del cliente es             : {nomCli}")
    print(f"El consumo de energía fue            : {cantEn}")
def calculo_tarifa(cantEn):
    if (cantEn <= 199 and cantEn >= 100): #CONSUMO MAYOR A 100 MENOR A 199
        precio = cantEn * 1.20
        print(f"Total por consumo @Rs. 1.2 por unidad: {precio}")
        print("Total por sobrecarga                 : 0")
        print(f"Total a pagar                        : {precio}")
    elif (cantEn >= 200 and cantEn < 400):#MAYOR A 200 Y MENOR A 400, SI ES MAYOR A 300 COMIENZA A COBRAR UN RECARGO
        if cantEn > 300:
            precio = cantEn * 1.50
            print(f"Total por consumo @Rs. 1.50 por unidad: {precio}")
            excedente(precio) #HACE EL CÁLCULO DEL RECARGO
        else:
            precio = cantEn * 1.50
            print(f"Total por consumo @Rs. 1.50 por unidad: {precio}")
            print("Total por sobrecarga                  : 0")
            print(f"Total a pagar                         : {precio}")
    elif (cantEn >= 400 and cantEn < 600): #MAYOR A 400 Y MENOR A 600
        precio = cantEn * 1.80
        print(f"Total por consumo @Rs. 1.80 por unidad: {precio}")
        excedente(precio)
    elif (cantEn >= 600): #MAYOR A 600
        precio = cantEn * 2.00
        print(f"Total por consumo @Rs. 2.00 por unidad: {precio}")
        excedente(precio)
    elif (cantEn < 100): #SI ES MENOR A 100 SE COBRAN 100 POR LA TARIFA, QUE ES 1.20
        precio = cantEn * 1.2
        print(f"Total por consumo @Rs. 1.20 por unidad: {precio}")
        print("Total por sobrecarga                  : 0")
        print(f"Total a pagar                         : {precio}")
def excedente(precio):
        sobrecarga = precio * 0.15
        recargo = precio + sobrecarga
        print(f"Total por sobrecarga                 : {sobrecarga}")
        print(f"Total a pagar                        : {recargo}")
def recibluz():
    numCli = input("Ingresa tu número de cliente:  ")
    nomCli = input("Ingresa tu nombre:  ")
    cantEn = float(input("Ingresa la cantidad de energia:  "))
    print("**********************************************")
    datos_a_mostrar(numCli, nomCli, cantEn)
    calculo_tarifa(cantEn)
    
    
salir = 0
while salir == 0:
    print("1-Armstrong")
    print("2-Libros")
    print("3-Recibo Luz")
    print("4-Cerrar")
    progsel=int(input("Selecciona un programa: "))
    if progsel==1:
        clear_console()
        armstrong()
    elif progsel==2:
        clear_console()
        libros()
    elif progsel==3:
        clear_console()
        recibluz()
    elif progsel==4:
        salir=salir+1
