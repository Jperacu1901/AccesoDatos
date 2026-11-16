import os
import shutil

#Ejercicio 1

# origen = "reporte_borrador.docx"
# destino = "reporte_final.docx"

# if os.path.exists(origen):
#     if os.path.exists(destino):
#         print("El archivo destino ya existe")

#     else:
#         try:
#             os.rename(origen, destino)
#             print("Se renombro el archivo")
#         except FileExistsError:
#             print("Error")
#         except Exception as e:
#             print("Error")
# else:
#     print("El archivo ya existe")

#Ejercicio 2

# def respaldar_documento(ruta_archivo, carpeta_destino):
#     if not os.path.isfile(ruta_archivo):
#         print("El archivo no existe")
#         return None
    
#     os.makedirs(carpeta_destino)
#     ruta_copia = shutil.copy2(ruta_archivo, carpeta_destino)
#     return ruta_copia

# resultado = respaldar_documento("Ejemplo.txt", "prueba")
# if resultado:
#     print("Archivo respaldado")

#Ejercicio 3

# origen = "plantillas"
# destino = os.path.join("backups","plantillas_backup")

# if os.path.exist(origen) and os.path.isdir(origen):
#     try:
#         shutil.copytree(origen) and os.path.isdir(origen)
#         print("Copia de seguridad completada")
#     except PermissionError:
#         print("Error")
# else:
#     print("No existe el directorio")

#Ejercicio 4

# def clasificar_fichero(ruta_fichero, carpeta_destino):
#     if not os.path.isfile(ruta_fichero):
#         print("El fichero no existe")
#         return
#     if not os.path.exists(carpeta_destino):
#         os.makedirs(carpeta_destino)
#         print("Carpeta creada")

#     try:
#         shutil.move(ruta_fichero, carpeta_destino)
#         print("Fichero movido")
#     except Exception as e:
#         print("Error")

# clasificar_fichero("texto.txt", "data")

#Ejercicio 5

def organizar_descargas(directorio_origen="descargas"):
    if not os.path.exists(directorio_origen):
        print("La carpeta no existe")
        return

    carpeta_imagenes = os.path.join(directorio_origen, "Imagenes")
    carpeta_auditoria = os.path.join(directorio_origen, "auditoria")

    try:
        for elemento in os.listdir(directorio_origen):
            ruta_elemento = os.path.join(directorio_origen, elemento)

            if os.path.isfile(ruta_elemento):
                print(f"Procesando: {elemento}")

                if elemento.endswith((".jpg", ".png")):
                    os.makedirs(carpeta_imagenes, exist_ok=True)
                    shutil.move(ruta_elemento, carpeta_imagenes)
                    print("Elemento movido a las imagenes")

                elif elemento.endswith(".log"):
                    os.makedirs(carpeta_auditoria, exist_ok=True)
                    shutil.copy2(ruta_elemento, carpeta_auditoria)
                    print("Elemento copiado a la auditoria")

    except Exception as e:
        print(f"Error: {e}")


organizar_descargas()