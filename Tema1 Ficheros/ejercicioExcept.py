
#Ejercicio 1
with open("notas.txt", "w") as f:
    f.write("Primera linea\n")
    f.write("Segunda linea\n")

try:
    with open("notas_antiguas.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("ERROR")

#Ejercicio 2

with open("mensaje.txt", "w") as f:
    f.write("Python es genial\n")

try:
    with open("mensaje.txt", "r") as f:
        print ("posicion: ", f.tell())
        texto_6 = f.read(6)
        print("posicion tras leer: ", f.tell())
        texto_resto = f.readline()
        print("texto leido")

except FileNotFoundError:
    print("ERROR")

#Ejercicio 3

with open("ajustes.txt", "w") as f:
    f.write("CLAVE=1234\nESTADO=DESACT")

try:
    with open("ajustes.txt", "r+") as f:
        linea = f.readline()
        f.read(7)
        f.seek(f.tell())
        loc = f.tell()
        print("Posicion:", loc)
        f.write("ACTIVO")

        f.seek(0)
        print(f.read())

except Exception as error:
    print("ERROR")

#Ejercicio 4

try:
    with open("diario.txt","r+") as f:
        f.seek(0,2)
        f.write("nueva entrada")
        loc = f.tell()
        print("Localizacion:", loc)

except FileNotFoundError:
    print("No existe el diario: ")
    with open("diario.txt", "w") as f:
        f.write("--- DIARIO PERSONAL ---\n")
        print("Diario Creado")

except PermissionError:
    print("No tiene permisos")

#Ejercicio 5

with open("agenda.txt", "w") as f:
    f.write("Contacto 1: Juan - 600111222\n")
    f.write("Contacto 2: PENDING - 000000000\n")
    f.write("Contacto 3: Pedro - 600333444")

try:
    with open("agenda.txt", "r+") as f:
        pos_inicio = f.tell()
        f.readline()
        pos_inicio = f.tell()
        f.readline()
        f.seek(pos_inicio)
        f.write("Contacto 2: Francis - 600999888\n")
        pos_inicio = f.tell()
        f.readline()
        f.seek(0)
        print(f.read())

except FileNotFoundError:
    print("Error")