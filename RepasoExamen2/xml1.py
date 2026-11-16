import xml.etree.ElementTree as ET

productos = [
    {"sku": "PROD-101", "denominacion": "Monitor 27 Pulgadas", "precio": 249.99, "disponible": True},
    {"sku": "PROD-102", "denominacion": "Teclado Mecánico RGB", "precio": 79.50, "disponible": True},
    {"sku": "PROD-103", "denominacion": "Ratón Inalámbrico", "precio": 29.90, "disponible": False}
]

raiz = ET.Element("Inventario", attrib={"tienda": "central", "actualizado": "2026-11-03"})

for producto in productos:
    nodo_producto = ET.SubElement(raiz, "producto")
    nodo_producto.set("sku", producto["sku"])

    nodo_denominacion = ET.SubElement(nodo_producto, "denominacion")
    nodo_denominacion.text = producto["denominacion"]

    nodo_precio = ET.SubElement(nodo_producto, "precio")
    nodo_precio.text = str(producto["precio"])

    nodo_disponibilidad = ET.SubElement(nodo_producto, "disponibilidad")
    nodo_disponibilidad.text = "Stock" if producto["disponible"] else "Agotado"

arbol = ET.ElementTree(raiz)
arbol.write("inventario.xml", encoding="utf-8", xml_declaration=True)

print("Archivo generado correctamente")