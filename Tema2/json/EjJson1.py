import json

#Ejercicio 1

ruta_json = "Tema2/json/configuracion.json"

try:
    with open(ruta_json,mode="r", encoding="utf-8") as f:
        configuracion = json.load(f)

        configuracion["modo_debug"] = True
        configuracion["modulos_activos"].append("ficheros")

    with open(ruta_json,mode="w", encoding="utf-8") as f:
        json.dump(configuracion, f, indent=4, ensure_ascii=False)
    print(f"archivo {ruta_json} creado")
except FileNotFoundError:
    print("Error")

