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
sentencia_sql = ("UPDATE persona SET nombre_persona=%s, apellido_persona=%s, edad_persona=%s WHERE id_persona=%s")
valores_update = ('Victoria', 'Flores', '55', 5)
my_cursor.execute(sentencia_sql, valores_update)
my_conexion.commit() # confirmamos la transacción
print(f'Se ha modificado {my_cursor.rowcount} registro\n')
print(f'Datos modificados: {valores_update}\n')

# cerramos cursor y conexion
my_cursor.close()
my_conexion.close()