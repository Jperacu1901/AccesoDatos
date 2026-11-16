import csv

ruta_lectura = "RepasoExamen2/reservas.csv"
ruta_escritura = "RepasoExamen2/almacen.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as f_lec, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as f_esc:

        lector_csv = csv.DictReader(f_lec, delimiter=",")

        campos = lector_csv.fieldnames.copy()
        campos.append("precio_final")

        escritor_csv = csv.DictWriter(f_esc, fieldnames=campos, delimiter=",")

        print(f"columnas del nuevo archivo: {campos}\n")
        escritor_csv.writeheader()

        for fila in lector_csv:
            estado = fila["estado"]
            noches = int(fila["noches"])
            precio_noche = float(fila["precio_noche"])

            if estado == "confimada" and noches >= 3:
                precio_final = (noches * precio_noche) * 0.85

                fila["precio_final"] = f"{precio_final:.2f}"

                cliente = fila["cliente"]
                id_res = fila["id_reserva"]
                print(f"Reserva: {id_res:<5} Cliente: {cliente:<15} Noches: {noches:<3} Precio Final (-15%): {precio_final:<8.2f}€")

                escritor_csv.writerow(fila)

except FileNotFoundError:
    print("Error")