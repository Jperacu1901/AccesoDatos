import xml.etree.ElementTree as ET

pedidos = [
    {"id_pedido": "PED-001", "cliente": "Empresa Alfa", "total": 1250.50, "entregado": True},
    {"id_pedido": "PED-002", "cliente": "Tecnologías Beta", "total": 340.00, "entregado": False},
    {"id_pedido": "PED-003", "cliente": "Sistemas Gamma", "total": 890.25, "entregado": True}
]

raiz = ET.Element("gestion_pedidos", attrib={"fecha_exportacion": "2026-03-30"})

for item in pedidos:
    nodo_pedido = ET.SubElement(raiz, "pedido")
    
    nodo_pedido.set("id", item["id_pedido"])

    nodo_cliente = ET.SubElement(nodo_pedido, "cliente")
    nodo_cliente.text = item["cliente"]

    nodo_total = ET.SubElement(nodo_pedido, "total")
    nodo_total.text = str(item["total"])

    nodo_estado = ET.SubElement(nodo_pedido, "estado")
    nodo_estado.text = "entregado" if item["entregado"] else "pendiente"

arbol = ET.ElementTree(raiz)

arbol.write("pedidos.xml", encoding="utf-8", xml_declaration=True)
print("Creado")