# pip install matplotlib
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

class Punto2D():
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
    def __add__(self, otro_punto):
        x = self.x + otro_punto.x
        y = self.y + otro_punto.y
        return x, y
    def __sub__(self, otro_punto):
        x = self.x - otro_punto.x
        y = self.y - otro_punto.y
        return x, y
    def __mul__(self, escalar):
        x = self.x * escalar
        y = self.y * escalar
        return x, y
    def __truediv__(self, escalar):
        x = self.x / escalar
        y = self.y / escalar
        return x, y
    def ModificarPosX(self, x):
        self.x = x
    def ModificarPosY(self, y):
        self.y = y
    def CalcularMagnitud(self):
        return math.sqrt(pow(self.x,2) + pow(self.x,2))

# LimpiarConsola()
# print("Programa 01 - Puntos dentro de una recta")
# p = Punto2D(0.0, 0.0)
# q = Punto2D(0.0, 0.0)
# print("Punto P")
# p.ModificarPosX(float(input("x: ")))
# p.ModificarPosY(float(input("y: ")))
# print("")
# print("Punto Q")
# p.ModificarPosX(float(input("x: ")))
# p.ModificarPosY(float(input("y: ")))
# print("")
# total_puntos = int(input("Total de puntos: "))

# T = 1.0/(total_puntos + 1)
# lista_puntos = []

# for i in range(0,total_puntos, 1):
#     temp = Punto2D(0.0, 0.0)
#     temp.ModificarPosX(p.x * (1 - T * (i + 1)) + q.x * T * (i + 1))
#     temp.ModificarPosY(p.y * (1 - T * (i + 1)) + q.y * T * (i + 1))
#     print(f"{temp.x}, {temp.y}")
#     lista_puntos.append(temp)
# print()
# for i in range(0,len(lista_puntos), 1):
#     print(f"{lista_puntos[i].x}, {lista_puntos[i].y}")

# x = [p.x, q.x]
# y = [p.y, q.y]
# plt.plot(x,y, '-ro' ,color='#C49C48')

# for i in range(0,len(lista_puntos), 1):
#     plt.plot(lista_puntos[i].x, lista_puntos[i].y, '*', color='#5E1224')    

# plt.show()

# LimpiarConsola()
# print("Programa 02 - Grafica de f(x) = e^(-|x|) * Cos(2 * pi * x)")
# total_puntos = int(input("Total de puntos: "))
# for i in range(0, total_puntos, 1):
#     temp = Punto2D(0.0, 0.0)
#     temp.ModificarPosX(float(i))
#     temp.ModificarPosY(exp(-abs(i)) * math.cos(2 * math.pi* i))
#     plt.plot(temp.x, temp.y, 'o', color='#5E1224')    
# plt.show()

# total_puntos = int(input("Total de puntos: "))
# i = 0.0
# incremento = 4.0/total_puntos
# while(i < 4.0):
#     temp = Punto2D(0.0, 0.0)
#     temp.ModificarPosX(float(i))
#     temp.ModificarPosY(exp(-abs(i)) * math.cos(2 * math.pi* i))
#     plt.plot(temp.x, temp.y, 'o', color='#5E1224')    
#     i += incremento
# plt.show()

class Mascota():
    def __init__(self, id, nombre, tipo, raza, genero, edad):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.raza = raza
        self.genero = genero
        self.edad = edad
        self.estaAdoptado = False
    def MostrarInformacionCompleta(self):
        print(f"ID: {self.id} - Nombre: {self.nombre} \t Tipo: {self.tipo} - Raza: {self.raza}")
        print(f"Genero: {self.genero} \t Edad: {self.edad}")
        if self.estaAdoptado == False:
            print("Status: Disponible")
        else:
            print("Status: En Adopcion")
    def MostrarInformacion(self):
        print(f"ID: {self.id} - Nombre: {self.nombre} \t Tipo: {self.tipo} - Raza: {self.raza}")
    def CambiarStatus(self, status):
        self.estaAdoptado = status

class Cliente():
    def __init__(self, id, nombre, genero, edad):
        self.id = id
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.tieneAdopcion = False
    def MostrarInformacionCompleta(self):
        print(f"ID: {self.id} - Nombre: {self.nombre} \t Genero: {self.genero} \t Edad: {self.edad}")
        if self.tieneAdopcion == False:
            print("Status: Disponible")
        else:
            print("Status: Asignado")
    def MostrarInformacion(self):
        print(f"ID: {self.id} - Nombre: {self.nombre} \t Genero: {self.genero} \t Edad: {self.edad}")
    def CambiarStatus(self, status):
        self.tieneAdopcion = status


class Adopcion():
    def __init__(self, id):
        self.id = id
        self.status = "Vigente"
    def AsignarCliente(self, cliente):
        self.cliente = cliente
    def AsignarMascota(self, mascota):
        self.mascota = mascota
    def MostrarInformacion(self):
        print(f"No. Adopcion: {self.id}")
        self.cliente.MostrarInformacion()
        self.mascota.MostrarInformacion()
    

class Veterinaria():
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_mascotas = []
        self.lista_clientes = []
        self.lista_adopcion = []
    def AgregarMascota(self, mascota):
        self.lista_mascotas.append(mascota)
    def AgregarCliente(self, cliente):
        self.lista_clientes.append(cliente)
    def EliminarMascota(self, id):
        existaMascota = False
        for i in range(0, len(self.lista_mascotas), 1):
            if self.lista_mascotas[i].id == id:
                existaMascota = True
                self.lista_mascotas.pop(i)
                break
        if existaMascota == True:
            return True
        else:
            return False
    def EliminarCliente(self, id):
        existeCliente = False
        for i in range(0, len(self.lista_clientes), 1):
            if self.lista_clientes[i].id == id:
                existeCliente = True
                self.lista_clientes.pop(i)
                break
        if existeCliente == True:
            return True
        else:
            return False
    def VerMascota(self, id):
        existaMascota = False
        for i in range(0, len(self.lista_mascotas), 1):
            if self.lista_mascotas[i].id == id:
                existaMascota = True
                self.lista_mascotas[i].MostrarInformacionCompleta()
                break
        if existaMascota == True:
            return True
        else:
            return False
    def VerCliente(self, id):
        existeCliente = False
        for i in range(0, len(self.lista_clientes), 1):
            if self.lista_clientes[i].id == id:
                existeCliente = True
                self.lista_clientes[i].MostrarInformacionCompleta()
                break
        if existeCliente == True:
            return True
        else:
            return False
    def VerMascotas(self):
        for i in range(0, len(self.lista_mascotas), 1):
            self.lista_mascotas[i].MostrarInformacion()
    def VerClientes(self):
        for i in range(0, len(self.lista_clientes), 1):
            self.lista_clientes[i].MostrarInformacion()
    def GenerarAdopcion(self, id_mascota, id_cliente, id):
        temp = Adopcion(id)
        temp.AsignarMascota(self.lista_mascotas[id_mascota])
        self.lista_mascotas[id_mascota].CambiarStatus(True)
        temp.AsignarCliente(self.lista_clientes[id_cliente])
        self.lista_clientes[id_cliente].CambiarStatus(True)
        self.lista_adopcion.append(temp)
    def VerAdopciones(self):
        for i in range(0, len(self.lista_adopcion), 1):
            self.lista_adopcion[i].MostrarInformacion()
            print("")
    def ExisteMascota(self, id):
        existaMascota = False
        index = 0
        for i in range(0, len(self.lista_mascotas), 1):
            if self.lista_mascotas[i].id == id:
                existaMascota = True
                index = i
                break
        if existaMascota == True:
            return True, index
        else:
            return False, index
    def ExisteCliente(self, id):
        existeCliente = False
        index = 0
        for i in range(0, len(self.lista_clientes), 1):
            if self.lista_clientes[i].id == id:
                existeCliente = True
                index = i
                break
        if existeCliente == True:
            return True, index
        else:
            return False, index
    def ExisteAdopcion(self, id):
        existeAdopcion = False
        index = 0
        for i in range(0, len(self.lista_adopcion), 1):
            if self.lista_adopcion[i].id == id:
                existeAdopcion = True
                index = i
                break
        if existeAdopcion == True:
            return True, index
        else:
            return False, index
    
def ImprimirMenu():
    print("Menu")
    print("1) Alta de Mascota")
    print("2) Baja de Mascota")
    print("3) Ver de Mascota")
    print("4) Ver Lista de Mascotas\n")

    print("5) Alta de Cliente")
    print("6) Baja de Cliente")
    print("7) Ver de Cliente")
    print("8) Ver Lista de Clientes\n")

    print("9) Generar Adopcion")
    print("10) Ver Lista de adopciones\n")

    print("11) Salir")
    
LimpiarConsola()
print("Programa 03 - Sistema Veterinaria")
id_global_mascota = 0
id_global_cliente = 0
id_global_adopcion = 0
mi_veterinaria = Veterinaria("PetCo")
correrPrograma = True
while correrPrograma:
    ImprimirMenu()
    opcion = int(input("Ingrese la opcion deseada: "))
    LimpiarConsola()
    if opcion == 1:
        nombre = input("Ingrese el nombre de la mascota: ")
        tipo = input("Ingrese el tipo de la mascota: ")
        raza = input("Ingrese la raza de la mascota: ")
        genero = input("Ingrese el genero de la mascota: ")
        edad = int(input("Ingrese la edad de la mascota: "))
        mascota_temp = Mascota(id_global_mascota, nombre, tipo, raza, genero, edad)
        mi_veterinaria.AgregarMascota(mascota_temp)
        id_global_mascota += 1
        input("\nMascota agregada. Presione Enter para continuar...")
        LimpiarConsola()
    elif opcion == 2:
        id = int(input("Ingrese el ID de la mascota: "))
        if mi_veterinaria.EliminarMascota(id) == False:
            input("\nNo existe mascota. Presione Enter para continuar...")
            LimpiarConsola()
        else:
            input("\nMascota eliminada correctamente. Presione Enter para continuar...")
            LimpiarConsola()
    elif opcion == 3:
        id = int(input("Ingrese el ID de la mascota: "))
        if mi_veterinaria.VerMascota(id) == False:
            input("\nNo existe mascota. Presione Enter para continuar...")
            LimpiarConsola()
        else:
            input("\nPresione Enter para continuar...")
            LimpiarConsola()
    elif opcion == 4:
        mi_veterinaria.VerMascotas()
        input("\nPresione Enter para continuar...")
        LimpiarConsola()
    elif opcion == 5:
        nombre = input("Ingrese el nombre del cliente: ")
        genero = input("Ingrese el genero del cliente: ")
        edad = int(input("Ingrese la edad del cliente: "))
        cliente_temp = Cliente(id_global_cliente, nombre, genero, edad)
        mi_veterinaria.AgregarCliente(cliente_temp)
        id_global_cliente += 1
        input("\nCliente agregado. Presione Enter para continuar...")
        LimpiarConsola()
    elif opcion == 6:
        id = int(input("Ingrese el ID del cliente: "))
        if mi_veterinaria.EliminarCliente(id) == False:
            input("\nNo existe cliente. Presione Enter para continuar...")
            LimpiarConsola()
        else:
            input("\nCliente eliminado correctamente. Presione Enter para continuar...")
            LimpiarConsola()
    elif opcion == 7:
        id = int(input("Ingrese el ID del cliente: "))
        if mi_veterinaria.VerCliente(id) == False:
            input("\nNo existe cliente. Presione Enter para continuar...")
            LimpiarConsola()
        else:
            input("\nPresione Enter para continuar...")
            LimpiarConsola()
    elif opcion == 8:
        mi_veterinaria.VerClientes()
        input("\nPresione Enter para continuar...")
        LimpiarConsola()
    elif opcion == 9:
        id_m = int(input("Ingrese el ID de la mascota: "))
        id_c = int(input("Ingrese el ID del cliente: "))
        existe_m, index_m = mi_veterinaria.ExisteMascota(id_m)
        existe_c, index_c = mi_veterinaria.ExisteCliente(id_c)
        if existe_m and existe_c and mi_veterinaria.lista_clientes[index_c].tieneAdopcion == False and mi_veterinaria.lista_mascotas[index_m].estaAdoptado == False:
            mi_veterinaria.GenerarAdopcion(index_m, index_c, id_global_adopcion)
            id_global_adopcion += 1
            input("\nAdopcion exitosa. Presione Enter para continuar...")
            LimpiarConsola()
        else:
            print("\nEl cliente o la mascota no existe o el cliente o la mascota no esta disponible para adopcion. Presione Enter para continuar...")
            input("Presione Enter para continuar...")
            LimpiarConsola()
    elif opcion == 10:
        mi_veterinaria.VerAdopciones()
        input("Presione Enter para continuar...")
    elif opcion == 11:
        correrPrograma = False
        input("Finalizando el programa. Presione Enter para continuar...")
    else:
        input("Opcion no valida. Presione Enter para continuar...")
