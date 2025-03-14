# importamos logueador
from logger_base import log
from psycopg2 import pool
import sys

# creamos la clase conexión
class ConectionPool:
    _DATABASE = 'bar_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT  = '5432'
    _HOST     = '127.0.0.1'
    _MIN      = 1
    _MAX      = 5
    _pool     = None
    
    # inicializamos el pool de conexiones
    @classmethod
    def obtenerPool(cls):
    # si no existe el pool lo creamos
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN, 
                                                      cls._MAX, 
                                                      host=cls._HOST, 
                                                      user=cls._USERNAME, 
                                                      password=cls._PASSWORD, 
                                                      port=cls._DB_PORT, 
                                                      database=cls._DATABASE)
                log.debug(f'Conexión del pool de conexiones exitoso')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool de conexiones: {e}')
                sys.exit()
    #
    # si el pool de conexiones existe regresamos
        else:
            return cls._pool

    # obtenemos una conexión del pool de conexiones
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool de conexiones: {conexion}')
        return conexion
    
    # devolvemos una conexión que ya no se use al pool de conexiones
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool de conexiones: {conexion}')
        
    # cerrar todas las conexiones
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f'Se cerraron todas las conexiones')

if __name__ == '__main__':
    # obtenemos varias conexiones del pool de conexiones
    conexion1 = ConectionPool.obtenerConexion()
    # se libera el objeto de conexiones
    ConectionPool.liberarConexion(conexion1)
    
    # obtenemos una segunda conexión del pool
    conexion2 = ConectionPool.obtenerConexion()
    