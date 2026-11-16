import csv

ruta_lectura = "RepasoExamen2/personal.csv"
ruta_escritura = "RepasoExamen2/personal_limpio.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as f_lec, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as f_esc:

        lector_csv = csv.reader(f_lec, delimiter=",")
        escritor_csv = csv.writer(f_esc, delimiter=",")

        cabecera = next(lector_csv)
        print(f"Columnas originales: {cabecera}\n")
        escritor_csv.writerow(cabecera)

        for fila in lector_csv:
            nombre = fila[0].upper()
            cargo = fila[1].strip().title()
            ciudad = fila[2].strip()

            if not ciudad:
                ciudad = "Desconocida"

            fila_limpia = [nombre, cargo, ciudad]

            print("Terminado")

            escritor_csv.writerow(fila_limpia)

except FileNotFoundError:
    print("ERROR")