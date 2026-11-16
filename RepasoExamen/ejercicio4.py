import os
import shutil

zona_descargas = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\zona_descargas"
reporte =r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\reporte.pdf"
imagen = r"C:\Users\galac\Documents\DAM\2DAM\AccesoDatos\imagen.jpg"

if os.path.isdir(zona_descargas):
    print("La ruta existe, procediendo a borrarla")
    shutil.rmtree(zona_descargas)
else:
    print("Creando la ruta")
    os.makedirs(zona_descargas)

if os.path.exists(reporte):
    print("el archivo existe, procediendo a borrarla")
    os.remove("reporte.pdf")
else:
    print("Creando el reporte")
    with open(reporte, "w") as f:
        f.write("Contenido")

if os.path.exists(imagen):
    print("el archivo existe, procediendo a borrarla")
    os.remove("reporte.pdf")
else:
    print("Creando la imagen")
    with open(imagen, "w") as f:
        f.write("")

def clasificarYmover(origen, destino):
    try:
        shutil.move(origen, destino)
        print("Archivo movido")
    except FileNotFoundError:
        print("No se encontro el archivo")

def limpiar_no_deseados(ruta_archivo):
    try:
        os.remove(ruta_archivo)
        print("Archivo obsoleto, borrando")
    except FileNotFoundError:
        print("Archivo no encotrado")

