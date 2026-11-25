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

    # Ejercicio A-1

    # sql = """
    #     INSERT INTO departamentos (nombre, ciudad, presupuesto_anual)
    #     VALUES (%s, %s, %s)
    # """

    # datos = ("Soporte Técnico", "Málaga", 140000.00)
    # cursor.execute(sql, datos)
    # conexion.commit()

    # print("---NUEVO DEPARTAMENTO---")
    # print(f"Departamento: {datos[0]} | Ciudad: {datos[1]} | Presupuesto: {datos[2]} € | ID asignado: {cursor.lastrowid}")

    # Ejercicio A-2

    # sql = """
    #     INSERT INTO clientes (nombre_empresa, ciudad, pais, sector)
    #     VALUES (%s, %s, %s, %s)
    # """
    # nuevos_clientes = [
    #     ("TechNorte S.A.", "Bilbao", "España", "Industria"),
    #     ("DataSur Consulting", "Granada", "España", "Consultoría")
    # ]
    # cursor.executemany(sql, nuevos_clientes)
    # conexion.commit()

    # print("---NUEVOS CLIENTES INSERTADOS---")
    # for cli in nuevos_clientes:
    #     print(f"Empresa: {cli[0]} | Ciudad: {cli[1]} | País: {cli[2]} | Sector: {cli[3]}")
    # print(f"Total de clientes añadidos: {cursor.rowcount}")

    # Ejercicio A-3

    # sql = """
    #     INSERT INTO empleados (nombre, apellidos, email, puesto, salario, fecha_alta, activo, departamento_id)
    #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    # """
    # datos = ("Mateo", "Luna Morales", "mluna@techcorp.es", "Tecnico soporte", 25000.00, "2026-11-20", 1, 7)
    # cursor.execute(sql, datos)
    # conexion.commit()

    # print("---NUEVO EMPLEADO---")
    # print(f"Empleado: {datos[0]} {datos[1]} | Email: {datos[2]} | Puesto: {datos[3]} | Salario: {datos[4]} € | Departamento ID: {datos[7]} | ID asignado: {cursor.lastrowid}")

    # Ejercicio B-4

    sql = """
        UPDATE empleados
        SET salario = salario + %s
        WHERE email = %s
    """
    datos = (1500.00, "mluna@techcorp.es")
    cursor.execute(sql, datos)
    conexion.commit()

    print("---ACTUALIZACION SALARIO---")
    print(f"Filas actualizadas: {cursor.rowcount}")

    sql2 = """
        SELECT nombre, apellidos, email, salario
        FROM empleados
        WHERE email = %s
    """
    cursor.execute(sql2, ("mluna@techcorp.es",))
    empleado = cursor.fetchone()

    
    if empleado:
        print(f"Empleado: {empleado[0]} {empleado[1]} | Email: {empleado[2]} | Nuevo salario: {empleado[3]} €")

except Error as e:
  print("Error al consultar la base de datos:", e)

finally:

  if 'conexion' in locals() and conexion.is_connected():
    cursor.close()
    conexion.close()
