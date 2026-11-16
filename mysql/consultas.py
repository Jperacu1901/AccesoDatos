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



except Error as e:
  print("Error al consultar la base de datos:", e)

finally:

  if 'conexion' in locals() and conexion.is_connected():
    cursor.close()
    conexion.close()