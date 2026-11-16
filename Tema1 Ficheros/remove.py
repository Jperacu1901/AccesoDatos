import os
import shutil

# Ejercicio 1

# archivo = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data\texto.txt"

# if os.path.isfile(archivo):
#     try:
#         os.remove(archivo)
#         print("Archivo borrado")
#     except PermissionError:
#         print("No tienes permisos")
# else:
#     print("El archivo no existe")

# Ejercicio 2

# def eliminar_carpeta_vacia(ruta):
#     try:
#         os.rmdir(ruta)
#         print("El directorio ha sido borrado")
#     except FileNotFoundError:
#         print("El archivo no existe")
#     except OSError as e:
#         print("No se puede borrar la carpeta")

# ruta = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data"

# eliminar_carpeta_vacia(ruta)

# Ejercicio 3

# directorio = os.path.join (r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\sistema")

# if os.path.exists(directorio) and os.path.isdir(directorio):
#     try:
#         shutil.rmtree(directorio)
#         print("Directorio borrado")
#     except PermissionError:
#         print("No tienes permisos")
#     except OSError as e:
#         print("No se pudo borrar el direcotio")
# else:
#     print("El directorio no existe")

# Ejercicio 4

# def limpiar_archivos_por_extension(directorio, extension):
#     if not os.path.isdir(directorio):
#         print("No existe el directorio")
#         return
#     for elemento in os.listdir(directorio):
#         ruta_completa = os.path.join(directorio, elemento)
#         if os.path.isfile(ruta_completa) and elemento.endswith(extension):
#             try:
#                 os.remove(ruta_completa)
#                 print("Archivo eliminado")
#             except PermissionError:
#                 print("No tiene permisos")
#             except OSError:
#                 print("No se pudo borrar")
#     try:
#         os.rmdir(directorio)
#         print("Se elimino el directorio")
#     except OSError:
#         print("No se pudo borrar el direcotio")

# ruta_carpeta = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data\temporal"
# limpiar_archivos_por_extension(ruta_carpeta, ".txt")

# Ejercicio 5

def purgar_directorio_trabajo(ruta_carpeta):
    if not os.path.exists(ruta_carpeta) or not os.path.isdir(ruta_carpeta):
        print("No existe la ruta o no es un directorio")
        return

    extensiones_temporales = ('.bak', '.tmp')
    archivos_eliminados = 0
    archivos_omitidos = 0

    for elemento in os.listdir(ruta_carpeta):
        ruta_completa = os.path.join(ruta_carpeta, elemento)

        if os.path.isfile(ruta_completa):
            if elemento.lower().endswith(extensiones_temporales):
                try:
                    os.remove(ruta_completa)
                    archivos_eliminados += 1
                    print(f"Eliminado: {elemento}")
                except PermissionError:
                    print(f"No se pudo eliminar por permisos: {elemento}")
            else:
                archivos_omitidos += 1
                print(f"Elemento importante omitido: {elemento}")

    if archivos_eliminados > 0:
        print(f"\nPurga completada. Se eliminaron {archivos_eliminados} archivo(s).")
    elif archivos_omitidos > 0 and archivos_eliminados == 0:
        print("\nNo se encontraron archivos temporales para eliminar.")
    else:
        print("\nLa ruta está vacía.")

ruta_trabajo = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\Data\temporal_trabajo"
purgar_directorio_trabajo(ruta_trabajo)