# PATRON DE DISEÑO DAO (DATA ACCESS OBJECT): un plano que podemos usar y personalizar para usar en
# nuestras aplicaciones, para acceder a los datos de la base de datos.
# se encargará de administrar la información de la entidad cliente
from connectionMySQL import connectionMySQL
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id_cliente'
    INSERTAR    = '''INSERT INTO cliente(nombre_cliente, apellido_cliente, edad_cliente, telefono_cliente) 
                    VALUES(%s, %s, %s, %s)'''
    ACTUALIZAR  = '''UPDATE cliente 
                    SET nombre_cliente=%s, 
                    apellido_cliente=%s, 
                    edad_cliente=%s, 
                    telefono_cliente=%s 
                    WHERE id_cliente=%s'''
    BORRAR      = 'DELETE FROM cliente WHERE id_cliente=%s'
    
    @classmethod
    def seleccionar(cls):
        connection_select = None
        clientes_lista = []
        cantidad_registros = 0  # Inicializamos la variable
        
        try:
            connection_select = connectionMySQL.get_connection()
            cursor = connection_select.cursor()
            cursor.execute(cls.SELECCIONAR)
            
            registros = cursor.fetchall() # obtiene todos los registros
            cantidad_registros = len(registros)  # Contar registros manualmente
            
            for registro in registros:
                cliente_UNO = Cliente(registro[0], registro[1], registro[2],
                                      registro[3], registro[4], registro[5],
                                      registro[6])
                clientes_lista.append(cliente_UNO)
        
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            
        finally:
            if cursor:
                cursor.close()
            if connection_select:
                connection_select.close()
                
        return clientes_lista
                
    @classmethod
    def insertar(cls, cliente):
        connection_insert = None
        try:
            connection_insert = connectionMySQL.get_connection()
            cursor = connection_insert.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.edad, cliente.telefono)
            cursor.execute(cls.INSERTAR, valores)
            connection_insert.commit()
        
        except Exception as e:
            print(f'Ocurrión un error: {e}')
            
        finally:
            if connection_insert is not None:
                cursor.close()
                connectionMySQL.release_connection(connection_insert)
                
        return cursor.rowcount # retorna el numero de registros que se insertaron
                
    @classmethod
    def actualizar(cls, cliente):
        connection_update = None
        filas_afectadas = 0  # Para almacenar el resultado
        
        try:
            connection_update = connectionMySQL.get_connection()
            cursor = connection_update.cursor()
            valores = (cliente.id_cliente, cliente.nombre, cliente.apellido, cliente.edad, cliente.telefono)
            cursor.execute(cls.ACTUALIZAR, valores)
            connection_update.commit()
            filas_afectadas = cursor.rowcount  # Verificar si se modificó alguna fila
        
        except Exception as e:
            print(f'Ocurrión un error: {e}')
            
        finally:
            if cursor:
                cursor.close()
            if connection_update:
                connection_update.close()
                
        return filas_afectadas  # Devuelve la cantidad de filas modificadas
                
    @classmethod
    def borrar(cls, id):
        connection_borrar = None
        try:
            connection_borrar = connectionMySQL.get_connection()
            cursor = connection_borrar.cursor()
            cursor.execute(cls.BORRAR, id)
            connection_borrar.commit()
        
        except Exception as e:
            print(f'Ocurrión un error: {e}')

        finally:
            if connection_borrar is not None:
                cursor.close()
                connectionMySQL.release_connection(connection_borrar)

        return cursor.rowcount # retorna el numero de registros que se borraron

# pruebas
# d:\Programación\python_school\trabajo_con_mySql\test_clienteDAO.py

if __name__ == '__main__':
# # insertar un nuevo cliente
#     cliente1 = Cliente(nombre='Diana', apellido='Mondino', edad=25, telefono='657-1234')
#     clientes_insertados = ClienteDAO.insertar(cliente1)
#     print(f'Clientes insertados: {clientes_insertados}')

# # actualizar un cliente
    cliente1 = Cliente('Néstor', 'Agripa', 25, '657-9999',4)
    # mostrar los datos a modificar
    print(f' Cliente a modificar: {cliente1}')
    cliente_modificado = ClienteDAO.actualizar(cliente1)
    print(f'Clientes modificados: {cliente_modificado}')
    
    # listar todos los clientes
    clientes, cantidad= ClienteDAO.seleccionar()
    print(f'Cantidad de Clientes: {cantidad}')  # Imprimir la cantidad de registros{cantidad}')
    for cliente in clientes:
        print(cliente)