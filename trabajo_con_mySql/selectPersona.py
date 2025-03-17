# importamos librerias necesarias
# para trabajar con mysql
import mysql.connector
# para trabajar con fechas
from datetime import datetime

# creamos la conexión a la base de datos
my_conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='unidad_negocio_db'
)

# creamos el cursor para ejecutar consultas SQL
my_cursor = my_conexion.cursor()
my_cursor.execute('SELECT * FROM persona')
# obtenemos los registros de la consulta y los guardamos en una variable
my_recordset = my_cursor.fetchall()
# imprimimos los registros obtenidos
for record in my_recordset:
    print(record)
    
# cerramos el cursor y la conexión a la base de datos
my_cursor.close()
my_conexion.close()