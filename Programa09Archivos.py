#archivo= open("datos.txt","a")
#archivo.write("Hola\n")
#archivo.close()
archivo_lectura=open("datos.txt","r")
for linea in archivo_lectura:
    linea_actual=linea.split(",")
    print(f"{linea_actual[0]}-{linea_actual[1]}")