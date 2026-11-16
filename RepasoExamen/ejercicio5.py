import os
import shutil

def crear_carpeta_diaria(base, fecha):
    ruta_completa = os.path.join(base, fecha)
    try:
        os.makeirs(ruta_completa)
        print(f"Ruta {ruta_completa}")
        return ruta_completa
    except PermissionError:
        print("No cuenta con permisos")

def procesar_y_consolidar(directorio_origen, archivo_informe):
    try:
        with open(ruta_informe, "w") as f:
            f.write("Resumen del dia")

            for elemento in os.listdir(directorio_origen):
                if elemento.endswith(".txt"):
                    ruta_archivo = os.path.join(directorio_origen)
                    with open(ruta_archivo, "r"):
                        f.read().strip()
                        f.write(f"[Elemento]")

        print("Informe consolidado")
    except FileNotFoundError:
        print("Archivo no encontrado")

def archivar_y_limpiar(dir_origen, dir_destino, archivo_log):
    for elemento in os.listdir(dir_origen):
        if elemento.endswith("txt"):
            ruta_origen = os.path.join(dir_origen, elemento)
            try:
                shutil.move(ruta_origen, dir_destino)
                print(f"[Archivado] {elemento}")
            except Exception as e:
                print("Error")

    try:
        os.remove(archivo_log)
        print(f"[Eliminado] {archivo_log}")
    except FileNotFoundError:
        print("Error")

    try:
        os.rmdir(dir_origen)
        print(f"[OK] bandeja de salida vacia")
    except OSError:
        print("Error")
        
