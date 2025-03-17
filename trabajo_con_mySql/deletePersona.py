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
sentencia_sql = ("DELETE FROM persona WHERE id_persona=%s")
valores_delete = (5,) # se especifica el id del registro a borrar pero con una coma al final para que sea una tupla
my_cursor.execute(sentencia_sql, valores_delete)
my_conexion.commit() # confirmamos la transacción
print(f'Se ha borrado {my_cursor.rowcount} registro\n')
print(f'Datos borrados: {valores_delete}\n')

# cerramos cursor y conexion
my_cursor.close()
my_conexion.close()