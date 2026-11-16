import xml.etree.ElementTree as ET

servidores = [
    {"ip": "192.168.1.10", "hostname": "srv-db-01", "ram_gb": 32, "activo": True},
    {"ip": "192.168.1.20", "hostname": "srv-web-01", "ram_gb": 16, "activo": True},
    {"ip": "192.168.1.30", "hostname": "srv-bk-01", "ram_gb": 8, "activo": False}
]

raiz = ET.Element("infraestructura", attrib={"entorno": "Produccion", "zona": "eu-west-1"})


for srv in servidores:
    # Crear etiqueta <servidor ip="...">
    nodo_srv = ET.SubElement(raiz, "servidor")
    nodo_srv.set("ip", srv["ip"])

    nodo_host = ET.SubElement(nodo_srv, "hostname")
    nodo_host.text = srv["hostname"]

    nodo_ram = ET.SubElement(nodo_srv, "ram_gb")
    nodo_ram.text = str(srv["ram_gb"])

    nodo_estado = ET.SubElement(nodo_srv, "estado")
    nodo_estado.text = "ONLINE" if srv["activo"] else "OFFLINE"

arbol = ET.ElementTree(raiz)
arbol.write("servidores.xml", encoding="utf-8", xml_declaration=True)

print("Archivo 'servidores.xml' generado correctamente.")