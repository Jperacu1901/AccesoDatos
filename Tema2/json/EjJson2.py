import json

ruta_origen = "alumnos.json"
ruta_destino = "aprobados.json"

alumno_datos = [
  {"nombre": "Laura", "notas": [8.5, 9.0, 7.5]},
  {"nombre": "Carlos", "notas": [3.0, 4.5, 4.0]},
  {"nombre": "Marta", "notas": [6.0, 5.5, 7.0]}
]

with open(ruta_origen, mode="w", encoding="utf-8") as f:
    json.dump(alumno_datos, f, indent=4)

    with open(ruta_origen, mode="r", enconding="utf-8") as f_in:
        estudiantes = json.load(f_in)

    aprobados = []

    for estudiante in estudiantes:
        notas = estudiante.get("notas",[])
        if notas:
            media = sum(notas) / len(notas)
            if media >= 5.0:
                estudiante_procesado = {
                    "nombre": estudiante["nombre"],
                    "notas": notas,
                    "media": round(media, 2)
                }
                aprobados.append(estudiante_procesado)
    with open(ruta_destino, mode="w", encoding="utf-8") as f_out:
        json.dump(aprobados, f_out, indent=4, ensure_ascii=False)
    print("Proceso terminado")

