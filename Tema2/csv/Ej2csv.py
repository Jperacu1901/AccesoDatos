import csv

ruta_lec = "Tema2/productos.csv"
ruta_esc = "Tema2/inventario.csv"

try:
    with open(ruta_lec, mode="r", encoding="utf-8", newline="") as r, \
        open(ruta_esc, mode="w", encoding="utf-8", newline="") as w:

        lector_csv = csv.DictReader(r, delimiter=",")

        campos = lector_csv.fieldnames.copy()
        campos.append("valor_total")

        escritor_csv = csv.DictWriter(w, fieldnames=campos, delimiter=",")

        print(f"Columnas: {campos}\n")
        escritor_csv.writeheader()


        for fila in lector_csv:
            producto = fila["producto"]
            precio = float(fila["precio"])
            stock = int(fila["stock"])

            valor_total = precio * stock

            fila["valor_total"] = valor_total
            print(f"Producto: {producto:<15} Precio: {precio:<8} Stock: {stock:<5} Valor Total: {valor_total:<10}")
            escritor_csv.writerow(fila)

except FileNotFoundError:
    print("Error")