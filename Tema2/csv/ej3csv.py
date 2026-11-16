import csv

ruta_lectura = "Tema2/empleados.csv"
ruta_escritura = "Tema2/bonificaciones_it.csv"

try:
    with open(ruta_lectura, mode="r", encoding="utf-8", newline="") as r, \
        open(ruta_escritura, mode="w", encoding="utf-8", newline="") as w:

        lector_csv = csv.DictReader(r, delimiter=",")

        campos = lector_csv.fieldnames.copy()
        campos.append("bonificacion")

        escritor_csv = csv.DictWriter(w, fieldnames=campos, delimiter=",")

        print(f"Columnas: {campos}\n")

        escritor_csv.writeheader()

        for fila in lector_csv:
            departamento = fila["departamento"]
            salario = float(fila["salario"])

            if departamento == "IT" and salario > 2500.0:
                bonificacion = salario * 0.10

                fila["bonificacion"] = bonificacion

                nombre = fila["nombre"]
                print(f"Empleado: {nombre:<15} departamento: {departamento:<5} Salario: {salario:<8.2f} Bonificación: {bonificacion:<8.2f}")
                
                escritor_csv.writerow(fila)

except FileNotFoundError:
    print("No existe el archivo de lectura")