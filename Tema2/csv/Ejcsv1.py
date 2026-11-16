import csv

ruta_lectura = "Tema2/alumnos.csv"
ruta_escritura = "Tema2/aprobados.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as f_lec, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as f_esc:
        
        lector_csv = csv.reader(f_lec, delimiter=",")
        escritor_csv = csv.writer(f_esc, delimiter=",")

        cabecera = next(lector_csv)
        print(f"Columnas: {cabecera}\n")

        escritor_csv.writerow(cabecera)

        for fila in lector_csv:
            nombre = fila[0]
            asignatura = fila[1]
            nota = float(fila[2])

            if nota >= 5.0:
                print(f"Aprobado -> Nombre: {nombre:<15} Asignatura: {asignatura:<15} Nota: {nota:<5}")
                escritor_csv.writerow(fila)

except FileNotFoundError:
    print("No existe el archivo")