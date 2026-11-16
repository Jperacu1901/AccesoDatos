import os

# #Ejercicio 1
# Ruta = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data"

# if os.path.exists(Ruta):
#     if os.path.isfile(Ruta):
#         print("La ruta existe y es un archivo")

#     elif os.path.isdir(Ruta):
#         print("La ruta existe y es un directorio")
#     else:
#         print("La ruta existe pero no es un archivo o directorio")
# else:
#     print("La ruta no existe")

# #Ejercicio 2

# carpeta_raiz = "proyectos"
# subcarpeta = "python/datos"
# fichero = "usuario.csv"

# ruta_relativa = os.path.join(carpeta_raiz, subcarpeta, fichero)

# ruta_absoluta = os.path.abspath(ruta_relativa)

# print("Ruta relativa:", ruta_relativa)
# print("Ruta absoluta:", ruta_absoluta)

#Ejercicio 3

# def es_archivo_txt(ruta):
#     if os.path.exists(ruta):
#         if os.path.isfile(ruta):
#             nombre_sin_ext, extension = os.path.sliptext(ruta)
#             print("La ruta existe y contiene archivo:", nombre_sin_ext)
#             if extension.lower() == ".txt":
#                 print("Es un archivo txt")
#             else:
#                 print("No es un archivo txt")
#         else:
#             print("La ruta no existe")

# es_archivo_txt = (r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data\texto.txt")

#Ejercico 4

# ruta = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data\texto.txt"

# if os.path.exists(ruta):
#     print(os.path.dirname(ruta))
#     print(os.path.basename(ruta))
#     print(f"{os.path.getsize(ruta) / 1024:.2f} KB")
# else:
#     print("La ruta no existe")

#Ejercico 5

rutas = [
    r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data\texto.txt",
    r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data",
    r"C:\Ruta\Inexistente\archivo_falso.txt",
    "fichero_inexistente.csv"
]

for ruta in rutas:
    if os.path.isdir(ruta):
        prit(f"{ruta}: Directorio")
    elif os.path.isfile(ruta):
        tamaño = os.path.getsize(ruta)
        print(f"{ruta}: Archivo({tamaño} bytes)")
    else:
        print(f"{ruta}. No encontrado")