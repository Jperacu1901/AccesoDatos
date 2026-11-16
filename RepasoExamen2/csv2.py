import csv

ruta_lectura = "RepasoExamen/envios.csv"
ruta_escritura = "envios_calculados.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as f_lec, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as f_esc:

        lector_csv = csv.DictReader(f_lec, delimiter=",")

        campos = lector_csv.fieldnames.copy()
        campos.append("coste_total")

        escritor_csv = csv.DictWriter(f_esc, fieldnames=campos, delimiter=",")

        print(f"Columnas del nuevo archivo: {campos}\n")
        escritor_csv.writeheader()

        for fila in lector_csv:
            id_envio = fila["id_envio"]
            destino = fila["destino"]
            peso_kg = float(fila["peso_kg"])
            precio_por_kg = float(fila["precio_por_kg"])

            coste_total = peso_kg * precio_por_kg

            fila["coste_total"] = coste_total

            print(f"Envío: {id_envio:<6} Destino: {destino:<12} Peso: {peso_kg:<5.1f}kg Coste Total: {coste_total:<8.2f}€")

            escritor_csv.writerow(fila)

except FileNotFoundError:
    print("ERROR")