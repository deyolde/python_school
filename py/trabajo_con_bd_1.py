# python se comunica con cualquier administrador de bd; mucho mejor con posgreSQL
import psycopg2


conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='bar_db'
    )

# creamos un cursor para ejecutar sentencias sql en la bd
cursor = conexion.cursor()

# armamos la sentencia para ejecutar sobra la bd
sentencia = 'select * from persona'

# se ejecuta la sentencia; lo que devuelve el contenido
cursor.execute(sentencia)

# y con esto traemos el contenido del cursor
registros=cursor.fetchall()

# impresión en pantalla de los datos de cursor
print(registros)

# importante: cierre del cursor
cursor.close()

# importante: cierre de la conexión
conexion.close()

print(' Cerré cursor y conexión - Ciao ')

