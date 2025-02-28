# python se comunica con cualquier administrador de bd; mucho mejor con posgreSQL

# 
import psycopg2
from datetime import datetime, timezone



conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='bar_db'
    )

print ('ahora insertamos registros')
# obtengo el time_stamp para los campos de auditoria
timestamp_actual = datetime.now(timezone.utc)

try:
    
    with conexion:
        
        # creamos un cursor para ejecutar sentencias sql en la bd
        with conexion.cursor() as cursor:
            
            # armamos la sentencia para ejecutar sobra la bd
            sentencia = 'INSERT INTO pedidos(mesa_pedido, persona_pedido, date_pedido, upd_pedido)\
                         VALUES (%s, %s, %s, %s)'
            # junto los valores a insertar en una tupla
            datos_a_insertar = (2, 1, timestamp_actual, timestamp_actual)
            
            # se ejecuta la sentencia; y con ello la insertsión en la tabla
            cursor.execute(sentencia, datos_a_insertar)
            
            # no olvidar el commita para que la info persista en la tabla
            # caso contrario, si nos desconectamos, se borran los datos
            conexion.commit()
            
except Exception as e:
    # finaliza no ok
    print(f'Se produjo un error {e}')

    
finally:
    # importante: cierre del cursor
    #cursor.close()
    # importante: cierre de la conexión
    #conexion.close()
    # finaliza ok
    print(' Hice la primera tarea ok')


print('Ahora vamos a contar cuántos bichos hay')

try:
    
    with conexion:
        
        # creamos un cursor para ejecutar sentencias sql en la bd
        with conexion.cursor() as cursor:
            
            sentencia = 'SELECT * FROM pedidos'
            cursor.execute(sentencia)
            total_registros = cursor.rowcount
            
            print(f'La tabla pedidos tiene: {total_registros}')

except Exception as e:
    print(f'Se produjo un error {e}')
    
finally:
    print('Cierro cursor y conexión')
    cursor.close()
    conexion.close()
        