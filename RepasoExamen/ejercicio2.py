import os


def crear_directorio(ruta):

    try:
        os.mkdir(ruta)
        print("Ruta creada")
    except FileExistsError:
        print("La ruta ya existe")
    except PermissionError:
        print("No tienes permisos")

def renombrar_registro(ruta_origen, ruta_destino):
    try:
        os.rename(ruta_origen, ruta_destino)
        print("Archivos renombrados")
    except FileExistsError:
        print("El archivo ya existe")
    except PermissionError:
        print("No tienes permisos")

def eliminar_registros(ruta):
    try:
        os.remove(ruta)
        print("Ruta eliminada")
    except FileNotFoundError:
        print("La ruta no existe")
    except PermissionError:
        print("No tienes permisos")
    except IsADirectoryError:
        print("Estas intentando borrar un directorio")

def main():
    dir_logs = "logs_sistema"
    log_antiguo = os.path.join(dir_logs, "app_old.log")
    log_nuevo = os.path.join(dir_logs, "app_2026.log")
    log_tmp = os.path.join(dir_logs, "cache.tmp")

    crear_directorio(dir_logs)

    with open(log_antiguo, "w") as f:
        f.write("Logs viejos")
    with open(log_nuevo, "w") as f:
        f.write("Logs nuevos")
    with open(log_tmp, "w") as f:
        f.write("Logs temporales")

    renombrar_registro(log_antiguo, log_nuevo)
    eliminar_registros(log_tmp)

main()