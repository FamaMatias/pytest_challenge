import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Cargar variables de entorno desde .env
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def get_connection():
    """
    Crea y retorna una conexión a la base de datos MySQL usando la configuración del .env.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def close_connection(connection):
    """
    Cierra la conexión a la base de datos si está activa.
    """
    if connection and connection.is_connected():
        connection.close()

def execute_sql_file(connection, sql_file_path, params=None):
    """
    Ejecuta la consulta SQL contenida en un archivo y retorna los resultados.
    Permite pasar parámetros para la consulta (por ejemplo, para usar %s en el SQL).
    """
    with open(sql_file_path, "r") as file:
        sql = file.read()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results