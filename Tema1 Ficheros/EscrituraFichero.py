#EJERCICIO 1

f = open("estado.txt", "w")
f.write("ESTADO: INACTIVO\n")
f.close()

f = open("estado.txt", "r+")
f.seek(8)
f.write("activo ")
f.seek(0)
print(f.read())
f.close()

#EJERCICIO 2

f = open("codigo.txt", "w")
f.write("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
f.close()

f = open("codigo.txt", "r+")
print(f.read(5))
f.seek(15)
f.write("EDITADO")
f.seek(0)
print(f.read())
f.close()

#EJERCICIO 3

f = open("registro.txt", "w")
f.writelines(["primero\n", "segundo\n", "tercero\n"])
f.close()

f = open("registro.txt", "r+")
x = f.readlines() 
f.write("--- COPIA DE SEGURIDAD ---\n")
f.writelines(x)
f.seek(0)
print(f.read())
f.close()

#EJERCICIO 4

f = open("lineas.txt", "w")
f.writelines(["Fila1: AAA\n", "Fila2: BBB\n", "Fila3: CCC\n"])
f.close()

f = open("lineas.txt", "r+")
f.readline()
f.write("Fila2: MODIFICADO\n")
f.seek(0, 1)
print(f.read())
f.close()

#EJERCICIO 5

f = open("Cabecera.txt", "w")
f.write("VERSION_1.0\nDATOS_DEL_SISTEMA\n")
f.close()

f = open("lineas.txt", "r+")
f.readline(7)
f.seek(8)
f.write("2.0")
f.seek(0)
print(f.read())
f.close()