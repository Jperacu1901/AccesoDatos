import csv

ruta_lectura = "RepasoExamen2/ventas.csv"
ruta_escritura = "ventas_grandes.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as f_lec, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as f_esc:

        lector_csv = csv.reader(f_lec, delimiter=",")
        escritor_csv = csv.writer(f_esc, delimiter=",")

        cabecera = next(lector_csv)
        escritor_csv.writerow(cabecera)

        for fila in lector_csv:
            id_venta = fila[0]
            vendedor = fila[1]
            importe = float(fila[2])

            if importe >= 500.0:
                print(f"Venta filtrada -> ID: {id_venta:<5} Vendedor: {vendedor:<15} Importe: {importe:<8.2f}")

except FileNotFoundError:
    print("ERROR")