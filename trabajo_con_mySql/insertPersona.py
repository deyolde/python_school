# realizaremos la lógica del insert de datos en mysql con python
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

# creamos el cursor para ejecutar consultas sql
my_cursor = my_conexion.cursor()
sentencia_sql = ("INSERT INTO persona (nombre_persona, apellido_persona, edad_persona) VALUES (%s, %s, %s)")
valores_insertar = ('Victor', 'Ramos', '25')
my_cursor.execute(sentencia_sql, valores_insertar)
my_conexion.commit() # confirmamos la transacción
print(f'Se ha insertado {my_cursor.rowcount} registro\n')
print(f'Id del registro insertado: {my_cursor.lastrowid}\n')
print(f'Datos insertados: {valores_insertar}\n')

# cerramos cursor y conexion
my_cursor.close()
my_conexion.close()