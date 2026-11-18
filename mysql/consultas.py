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
    sql = """
      SELECT COUNT(*) AS total_empleados,
            ROUND(AVG(salario), 2) AS salario_medio,
            MAX(salario) AS salario_maximo,
            MIN(salario) AS salario_minimo
      FROM empleados
    """
    cursor.execute(sql)
    stats = cursor.fetchone()

    print("---ESTADISTICAS DE EMPLEADOS---")
    for stat in stats:
      print(f"Total empleados: {stats[0]} | Salario medio: {stats[1]} € | Máximo: {stats[2]} € | Mínimo: {stats[3]} €")

except Error as e:
  print("Error al consultar la base de datos:", e)

finally:

  if 'conexion' in locals() and conexion.is_connected():
    cursor.close()
    conexion.close()
