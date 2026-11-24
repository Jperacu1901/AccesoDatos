import mysql.connector
from mysql.connector import Error

try:

  conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="techcorp_db"
  )

  if conexion.is_connected():
    cursor = conexion.cursor()

    # Consulta 1

    # sql = """
    #   SELECT nombre, apellidos, puesto, salario
    #   FROM empleados 
    #   ORDER BY salario DESC
    # """
    # cursor.execute(sql)
    # empleados = cursor.fetchall()

    # print("--- LISTADO DE EMPLEADOS (POR SALARIO) ---")
    # for emp in empleados:
    #   print(f"Nombre: {emp[0]} {emp[1]} | Puesto: {emp[2]} | Salario: {emp[3]} €")

    # Consulta 2
    # sql = """
    #   SELECT nombre, apellidos, salario
    #   FROM empleados
    #   WHERE activo = 1 AND salario > 35000
    # """
    # cursor.execute(sql)
    # empleados = cursor.fetchall()

    # print("---EMPLEADOS ACTIVOS CON SALARIO SUPERIOR A 35000---")
    # for emp in empleados:
    #   print(f"Nombre: {emp[0]} {emp[1]} | Salario: {emp[2]} €")

    # Consulta 3
    # sql = """
    #   Select nombre, presupuesto, estado
    #   FROM proyectos
    #   WHERE presupuesto BETWEEN 40000 AND 95000
    # """
    # cursor.execute(sql)
    # proyectos = cursor.fetchall()

    # print("---PROYECTOS CON SALARIO ENTRE 40000 y 95000---")
    # for pro in proyectos:
    #   print(f"Proyecto: {pro[0]} | Presupuesto: {pro[1]}€ | Estado: {pro[2]}")
    
    # Consulta 4
    # sql = """
    #   SELECT nombre, apellidos, email
    #   FROM empleados
    #   WHERE email NOT LIKE '%@techcorp.es' OR apellidos LIKE '%ez %'
    # """
    # cursor.execute(sql)
    # empleados = cursor.fetchall()

    # print("---CORREO QUE NO SEA DE TECHCORP O QUE EL APELLIDO TERMINE CON EZ---")
    # for emp in empleados:
    #   print(f"Nombre: {emp[0]}{emp[1]} | Email: {emp[2]}")

    # Consulta 5
    # sql_empleados = """
    # SELECT nombre, apellidos, puesto
    # FROM empleados
    # WHERE departamento_id IS NULL
    # """
    # cursor.execute(sql_empleados)
    # empleados_sin_dept = cursor.fetchall()

    # print("---EMPLEADOS SIN DEPARTAMENTO---")
    # for emp in empleados_sin_dept:
    #   print(f"Nombre: {emp[0]}{emp[1]} | Puesto:{emp[2]}")

    # Consulta 5.2
    # sql_proyectos = """
    #   SELECT nombre, fecha_inicio, estado
    #   FROM proyectos
    #   WHERE fecha_fin IS NULL
    # """
    # cursor.execute(sql_proyectos)
    # proyectos_sin_fin = cursor.fetchall()

    # print("\n---PROYECTOS SIN FECHA DE FINALIZACION---")
    # for pro in proyectos_sin_fin:
    #   print(f"Proyecto: {pro[0]} Inicio: {pro[1]} | Estado: {pro[2]}")

    # Consulta 6
    # sql = """
    #   SELECT nombre, presupuesto
    #   FROM proyectos
    #   ORDER BY presupuesto DESC
    #   LIMIT 3
    # """
    # cursor.execute(sql)
    # proyectos_top = cursor.fetchall()

    # print("---PROYECTOS MAS CAROS---")
    # for pro in proyectos_top:
    #   print(f"Proyecto: {pro[0]} | Presupuesto: {pro[1]} €")

    # Consulta 7
    # sql = """
    #   SELECT CONCAT(nombre, ' ', apellidos) AS empleado,
    #         salario AS salario_anual,
    #         ROUND(salario / 12 , 2) AS salario_mensual
    #   FROM empleados
    # """
    # cursor.execute(sql)
    # empleados = cursor.fetchall()

    # print("---SALARIO ANUAL Y MENSUAL---")
    # for emp in empleados:
    #   print(f"Empleado: {emp[0]} | Anual: {emp[1]} € | Mensual: {emp[2]} €")
    
    # Consulta 8
    # sql = """
    #   SELECT COUNT(*) AS total_empleados,
    #         ROUND(AVG(salario), 2) AS salario_medio,
    #         MAX(salario) AS salario_maximo,
    #         MIN(salario) AS salario_minimo
    #   FROM empleados
    # """
    # cursor.execute(sql)
    # stats = cursor.fetchone()

    # print("---ESTADISTICAS DE EMPLEADOS---")
    # for stat in stats:
    #   print(f"Total empleados: {stats[0]} | Salario medio: {stats[1]} € | Máximo: {stats[2]} € | Mínimo: {stats[3]} €")

    # Consulta 9
    # sql = """
    #   SELECT pais, COUNT(*) AS total_clientes
    #   FROM clientes
    #   GROUP BY pais
    #   ORDER BY total_clientes DESC
    # """
    # cursor.execute(sql)
    # clientes_pais = cursor.fetchall()

    # print("--- TOTAL DE CLIENTES POR PAÍS ---")
    # for fila in clientes_pais:
    #   print(f"País: {fila[0]} | Total clientes: {fila[1]}")

    # Consulta 10
    # sql = """
    # SELECT estado, SUM(presupuesto) AS total_presupuesto
    # FROM proyectos
    # GROUP BY estado
    # HAVING SUM(presupuesto) > 150000
    # """
    # cursor.execute(sql)
    # estados_presupuesto = cursor.fetchall()

    # print("--- ESTADOS CON PRESUPUESTO TOTAL SUPERIOR A 150.000 € ---")
    # for fila in estados_presupuesto:
    #   print(f"Estado: {fila[0]} | Presupuesto total: {fila[1]} €")

    # Consulta 11
    # sql = """
    #   SELECT e.nombre, e.apellidos, d.nombre AS departamento, d.ciudad
    #   FROM empleados e
    #   INNER JOIN departamentos d ON e.departamento_id = d.id
    # """
    # cursor.execute(sql)
    # empleados_dept = cursor.fetchall()

    # print("---EMPLEADOS Y DEPARTAMENTO ---")
    # for emp in empleados_dept:
    #   print(f"Nombre: {emp[0]} {emp[1]} | Departamento: {emp[2]} | Ciudad: {emp[3]}")

    # Consulta 12
    # sql = """
    #   SELECT p.nombre, p.presupuesto, c.nombre_empresa
    #   FROM proyectos p
    #   INNER JOIN clientes c ON p.cliente_id = c.id
    #   WHERE c.pais = 'España'
    # """
    # cursor.execute(sql)
    # proyectos_espana = cursor.fetchall()

    # print("---PROYECTOS DE CLIENTES EN ESPAÑA---")
    # for proy in proyectos_espana:
    #   print(f"Proyecto: {proy[0]} | Presupuesto: {proy[1]} € | Cliente: {proy[2]}")

    # Consulta 13
    # sql = """
    #   SELECT d.nombre, COUNT(e.id) AS total_empleados
    #   FROM departamentos d
    #   LEFT JOIN empleados e ON d.id = e.departamento_id
    #   GROUP BY d.id, d.nombre
    # """
    # cursor.execute(sql)
    # departamentos = cursor.fetchall()

    # print("---EMPLEADOS POR DEPARTAMENTO---")
    # for dept in departamentos:
    #   print(f"Departamento: {dept[0]} | Total empleados: {dept[1]}")

    # Consulta 14
    # sql = """
    #   SELECT c.nombre_empresa, c.ciudad, c.sector
    #   FROM clientes c
    #   LEFT JOIN proyectos p ON c.id = p.cliente_id
    #   WHERE p.id IS NULL
    # """
    # cursor.execute(sql)
    # clientes_sin_proyectos = cursor.fetchall()

    # print("---CLIENTES SIN PROYECTOS REGISTRADOS---")
    # for cli in clientes_sin_proyectos:
    #   print(f"Empresa: {cli[0]} | Ciudad: {cli[1]} | Sector: {cli[2]}")

    # Consulta 15
    # sql = """
    #   Select CONCAT(e.nombre, ' ', e.apellidos) AS empleado,
    #         p.nombre AS proyecto,
    #         a.rol,
    #         a.horas_asignadas a
    #   FROM asignaciones a
    #   INNER JOIN empleados e on a.empleado_id = e.id
    #   INNER JOIN proyectos p on a.proyecto_id = p.id
    #   ORDER BY p.nombre ASC
    # """
    # cursor.execute(sql)
    # asignaciones = cursor.fetchall()

    # print("---HISTORIAL DE ASGINACIONES---")
    # for asig in asignaciones:
    #   print(f"Empleado: {asig[0]} | Proyecto: {asig[1]} | Rol: {asig[2]} | Horas: {asig[3]}")

    # Consulta 16
    # sql = """
    #   SELECT p.nombre, SUM(a.horas_asignadas) AS total_horas
    #   FROM proyectos p
    #   INNER JOIN asignaciones a on p.id = a.proyecto_id
    #   GROUP BY p.id, p.nombre
    #   ORDER BY total_horas DESC
    # """
    # cursor.execute(sql)
    # horas_proyectos = cursor.fetchall()

    # print("---TOTAL HORAS ASIGNADAS AL PROYECTO---")
    # for proy in horas_proyectos:
    #   print(f"Proyecto: {proy[0]} | Total horas: {proy[1]}")

    # Consulta 17
    # sql = """
    #   SELECT nombre, apellidos, puesto, salario
    #   FROM empleados
    #   WHERE salario > (SELECT AVG(salario) FROM empleados)
    # """
    # cursor.execute(sql)
    # empleados_top_salario = cursor.fetchall()

    # print("---EMPLEADOS CON SALARIO SUPERIOR A LA MEDIA---")
    # for emp in empleados_top_salario:
    #   print(f"Nombre: {emp[0]} {emp[1]} | Puesto: {emp[2]} | Salario: {emp[3]} €")

    # Consulta 18
    # sql = """
    #   SELECT nombre, apellidos
    #   FROM empleados
    #   WHERE id IN (
    #     SELECT a.empleado_id
    #     FROM asignaciones a
    #     INNER JOIN proyectos p ON a.proyecto_id = p.id
    #     WHERE p.presupuesto > 100000
    #   )
    # """
    # cursor.execute(sql)
    # empleados_proyectos_caros = cursor.fetchall()

    # print("---EMPLEADOS EN PROYECTOS CON PRESUPUESTO SUPERIOR A 100000 €---")
    # for emp in empleados_proyectos_caros:
    #   print(f"Nombre: {emp[0]} {emp[1]}")

    # Consulta 19
    # sql = """
    #   SELECT d.nombre,
    #         COUNT(e.id) AS total_empleados,
    #         ROUND(AVG(e.salario), 2) AS salario_medio
    #   FROM departamentos d
    #   INNER JOIN empleados e ON d.id = e.departamento_id
    #   GROUP BY d.id, d.nombre
    #   HAVING COUNT(e.id) > 2 AND AVG(e.salario) > 35000
    # """
    # cursor.execute(sql)
    # departamentos_filtrados = cursor.fetchall()

    # print("---DEPARTAMENTOS CON 2 EMPLEADOS O  MAS Y SALARIO MEDIO MAYOR A 35.000 €---")
    # for dept in departamentos_filtrados:
    #   print(f"Departamento: {dept[0]} | Empleados: {dept[1]} | Salario medio: {dept[2]} €")

    # Consulta 20
    sql = """
      SELECT c.nombre_empresa,
            c.pais,
            COUNT(p.id) AS total_proyectos,
            COALESCE(SUM(p.presupuesto), 0) AS presupuesto_acumulado
      FROM clientes c
      LEFT JOIN proyectos p ON c.id = p.cliente_id
      GROUP BY c.id, c.nombre_empresa, c.pais
      ORDER BY presupuesto_acumulado DESC
    """
    cursor.execute(sql)
    informe_clientes = cursor.fetchall()

    print("---INFORME DE CLIENTES---")
    for cli in informe_clientes:
      print(f"Empresa: {cli[0]} | País: {cli[1]} | Proyectos: {cli[2]} | Presupuesto acumulado: {cli[3]} €")


except Error as e:
  print("Error al consultar la base de datos:", e)

finally:

  if 'conexion' in locals() and conexion.is_connected():
    cursor.close()
    conexion.close()
