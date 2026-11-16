import os

#Ejercicio 1

directorio = "proyectos"
fichero_borrador = os.path.join(directorio, "borrado_v1.txt")
fichero_final = os.path.join(directorio, "documento_final.txt")
fichero_tmp = os.path.join(directorio, "archivo_obsoleto.tmp")

if not os.path.exists(directorio):
    os.mkdir(directorio)
    print("Directorio creado con exito")
else:
    print("El directorio ya existe")

with open(fichero_borrador, "w") as f:
    f.write("Borrador inicial")

with open(fichero_tmp, "w") as f:
    f.write("Este archivo sera eliminado")

print("Archivos iniciales creados")

if os.path.exists(fichero_borrador):
    os.rename(fichero_borrador, fichero_final)
    print("Ficheros renombrados")

if os.path.exists(fichero_tmp):
    os.remove(fichero_tmp)
    print(f"archivo {fichero_tmp} eliminado")

