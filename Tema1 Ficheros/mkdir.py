import os

# Ejercicio 1

# nombre_carpeta = "backups"

# try:
#     os.mkdir(nombre_carpeta)
#     print("Se ha creado la carpeta")

# except FileExistsError:
#     print("El fichero no existe")

# except Exception:
#     print("Error")

# Ejercicio 2

# ruta_relativa ="sistema/reportes/2026/mensual"

# os.makedirs(ruta_relativa, exist_ok=true)
# ruta_absoluta = os.path.abspath(ruta_relativa)

# print("Ruta creada")

# Ejercicio 3

# directorio_a_listar = "Data"

# try:
#     elementos = os.listdir(directorio_a_listar)
#     print(f"Contenido del directorio '{directorio_a_listar}':")

#     for elemento in elementos:
#         ruta_completa = os.path.join(directorio_a_listar, elemento)

#         if os.path.isfile(ruta_completa):
#             tamano_bytes = os.path.getsize(ruta_completa)
#             print(f"- {elemento}: {tamano_bytes} bytes")

# except FileNotFoundError:
#     print(f"El directorio '{directorio_a_listar}' no existe.")
# except Exception as e:
#     print(f"Error inesperado: {e}")

# Ejercicio 4

# def contar_elementos(ruta_directorio):
#     try:
#         elementos = os.listdir(ruta_directorio)

#         total_archivos = 0
#         total_carpetas = 0

#         for elemento in elementos:
#             ruta_completa = os.path.join(ruta_directorio, elemento)

#             if os.path.isfile(ruta_completa):
#                 total_archivos += 1
#             elif os.path.isdir(ruta_completa):
#                 total_carpetas += 1

#         return (total_archivos, total_carpetas)

#     except FileNotFoundError:
#         return (0, 0)

# resultado = contar_elementos('.')

# print(resultado)

# Ejercicio 5

def generar_estructura_proyecto(nombre_proyecto, lista_modulos):
    if not os.path.exists(nombre_proyecto):
        os.makedirs(nombre_proyecto)
        print("Carpeta {nombre_proyecto} creado")
    else:
        print("La carpeta ya existe")

    for modulo in lista_modulos:
        ruta_subcarpeta = os.path.join(nombre_proyecto, modulo)
        if os.path.exists(ruta_subcarpeta):
            print("La subcarpeta ya existe")
        else:
            os.makedirs(ruta_subcarpeta)
            print("Subcarpeta {modulo} creada")

modulos = ["datos", "interfaces", "servicios"]
generar_estructura_proyecto(r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\ejemplo", modulos)