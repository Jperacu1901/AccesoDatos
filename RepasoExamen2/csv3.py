import csv

ruta_lectura = "RepasoExamen2/almacen.csv"
ruta_escritura = "RepasoExamen2/reposicion_alimentacion.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as f_lec, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as f_esc:

        lector_csv = csv.DictReader(f_lec, delimiter=",")
        campos = lector_csv.fieldnames.copy()
        campos.append("pedido_sugerido")

        escritor_csv = csv.DictWriter(f_esc, fieldnames=campos, delimiter=",")

        print(f"Columnas: {campos}\n")
        escritor_csv.writeheader()

        for fila in lector_csv:
            categoria = fila["categoria"]
            stock = int(fila["stock"])

            if categoria == "Alimentación" and stock < 15:
                pedido_sugerido = 50 - stock

                fila["pedido_sugerido"] = pedido_sugerido
                codigo = fila["codigo"]
                producto = fila["producto"]
                print(f"Reposición -> Código: {codigo:<6} Producto: {producto:<12} Stock actual: {stock:<4} Pedir: {pedido_sugerido:<4}")

                escritor_csv.writerow(fila)
except FileNotFoundError:
    print("Error")