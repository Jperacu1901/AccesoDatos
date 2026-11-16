import json

ruta_archivo = "RepasoExamen2/pedidos.json"

try:
    with open(ruta_archivo, mode="r", encoding="utf-8") as f:
        pedidos = json.load(f)

    id_buscar = int(input("Introduce el id:"))

    encontrado = False

    for pedido in pedidos:
        if pedido["id_pedido"] == id_buscar:
            encontrado = True
            if not pedido["entregado"]:
                pedido["entregado"] = True
                print("Pedido entregado")
            else:
                print("Pedido ya entregado previamente")
            break
        if not encontrado:
            print(f"Error pedido {id_buscar} no encontrado")
        if encontrado:
            with open(ruta_archivo, mode="w", encoding="utf-8") as f:
                json.dump(pedidos, f , indent=4, ensure_ascii=False)
            print("Archivo actualizado")
except FileNotFoundError:
    print("Error")