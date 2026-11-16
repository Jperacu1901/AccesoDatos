import mysql.connector

try:
    bd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="contactos",
    )

    print("Conexión exitosa a la base de datos 'contactos'")

    cursor = bd.cursor()
    cursor.execute("SELECT id, nombre, telefono FROM contactos")

    for id_contacto, nombre, telefono in cursor.fetchall():
        print(f"{id_contacto} - {nombre}: {telefono}")

except mysql.connector.Error as err:
    print("Error de conexión:", err)

finally:
    if "bd" in locals() and bd.is_connected():
        cursor.close()
        bd.close()