import os
import shutil


def vaciar_subcarpeta(ruta):
    try:
        shutil.rmtree(ruta)
        print(f"subcarpeta {ruta} borrada correctamente")
    except FileNotFoundError:
        print("Subcarpeta no encontrada")
    except PermissionError:
        print("No tienes permisos")

def borrar_archivo(ruta):
    try:
        os.remove(ruta)
        print(f"Archivo {ruta} borrado")
    except FileNotFoundError:
        print("El archivo no existe")

def borrar_carpeta_vacia(ruta):
    try:
        os.rmdir(ruta)
        print("Directorio eliminado")
    except OSError:
        print("Error del sistema")
    except FileNotFoundError:
        print("No existe el directorio")

def main():
    dir_principal = "respaldos_2025"
    subcarpeta = os.path.join(dir_principal, "cache")
    archivo_db = os.path.join(dir_principal, "datos_antiguos.db")

    os.makedirs(subcarpeta)
    with open(archivo_db, "w") as f:
        f.write("Datos obsoletos")
    with open(os.path.join(subcarpeta, "temp.log"), "w") as f:
        f.write("Log temporal")

    print("Estructura creada\n")

    print("\n1. Probando os.rmdir() en carpeta con archivos:")
    borrar_carpeta_vacia(dir_principal)


    print("\n2. Limpiando el contenido interno:")
    vaciar_subcarpeta(subcarpeta)
    borrar_archivo(archivo_db)

    print("\n3. Eliminando la carpeta principal vacía:")
    borrar_carpeta_vacia(dir_principal)

main()