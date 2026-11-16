import json

ruta_origen = "RepasoExamen2/inventario.json"
ruta_destino = "RepasoExamen2/inventario_rebajado.json"

try:
    with open(ruta_origen, mode="r", encoding="utf-8") as f_in:
        productos = json.load(f_in)

    productos_procesados = []

    for producto in productos:
        stock = producto.get("stock", 0)

        if stock > 0:
            nuevo_precio = round(producto["precio"] * 0.90, 2)
            valor_total = round(nuevo_precio * stock, 2)

            producto_actualizado = {
                "id": producto["id"],
                "producto": producto["producto"],
                "categoria": producto["categoria"],
                "precio_original": producto["precio"],
                "precio_rebajado": nuevo_precio,
                "stock": stock,
                "valor_total_stock": valor_total
            }
            productos_procesados.append(producto_actualizado)

    with open(ruta_destino, mode="w", encoding="utf-8") as f_out:
        json.dump(productos_procesados, f_out, indent=4, ensure_ascii=False)
    print("Proceso terminado")
except FileNotFoundError:
    print("Error")