import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",  # O la IP del servidor MySQL
            user="root",       # Usuario de MySQL
            password="root",       # Contraseña de MySQL (déjala vacía si no tiene)
            database="desarrollo"  # Nombre de tu base de datos
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
