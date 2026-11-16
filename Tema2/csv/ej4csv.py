import csv

ruta_lectura = "Tema2/clientes.csv"
ruta_escritura = "Tema2/clientes_limpios.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as r, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as w:

        lector_csv = csv.reader(r, delimiter=",")
        escritor_csv = csv.writer(w, delimiter=",")

        cabecera = next(lector_csv)
        print(f"Columnas: {cabecera}\n")
        escritor_csv.writerow(cabecera)

        for fila in lector_csv:
            nombre = fila[0].title()
            email = fila[1].title().lower()
            telefono = fila[2].strip()

            if not telefono:
                telefono = "N/A"

        fila_limpia = [nombre, email, telefono]

        print(f"Cliente: {nombre:<20} Email: {email:<25} Teléfono: {telefono:<12}")
            
        escritor_csv.writerow(fila_limpia)

except FileNotFoundError:
    print("Error")