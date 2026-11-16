import xml.etree.ElementTree as ET

facturas = [
    {"codigo": "FAC-2026-01", "cliente": "Talleres Hermanos Sánchez", "importe": 1450.00, "estado": "PAGADA", "recargo_equivalencia": False},
    {"codigo": "FAC-2026-02", "cliente": "Construcciones Norte SL", "importe": 3200.80, "estado": "PENDIENTE", "recargo_equivalencia": True},
    {"codigo": "FAC-2026-03", "cliente": "Imprenta Rápida", "importe": 410.50, "estado": "PAGADA", "recargo_equivalencia": True},
    {"codigo": "FAC-2026-04", "cliente": "Modas Elena", "importe": 890.00, "estado": "CANCELADA", "recargo_equivalencia": False}
]

raiz = ET.Element("inventario", attrib={"ejercicios":"2026", "modulo":"Facturacion"})

for factura in facturas:
    if factura["estado"] == "PAGADA":
        nodo_factura = ET.SubElement(raiz, "factura")
        nodo_factura.set("codigo", factura["codigo"])

        nodo_cliente = ET.SubElement(nodo_factura, "cliente")
        nodo_cliente.text = factura["cliente"]

        nodo_importe_total = ET.SubElement(nodo_factura, "importe_total")
        nodo_importe_total.text = str(factura["importe"])

        nodo_recargo = ET.SubElement(nodo_factura, "recargo")
        nodo_recargo.text = "SI" if factura["recargo_equivalencia"] else "NO"

arbol = ET.ElementTree(raiz)
arbol.write("facturas_pagadas.xml", encoding="utf-8", xml_declaration=True)
print("Archivo generado")
