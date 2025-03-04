# importamos logueador
from logger_base import log
import psycopg2 as bd
import sys

# creamos la clase conexión
class conexion:
    _DATABASE = 'bar_db'
    _USERNAE  = 'admin'
    _PASSWORD = 'admin'
    _DB_PORT  = '5342'
    _HOST     = '127.0.0.1'
    _conexion = None
    _cursor   = None
    
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host     = cls._HOST,
                                           user     = cls._USERNAE,
                                           password = cls._PASSWORD,
                                           port     = cls._DB_PORT,
                                           database = cls._DATABASE
                                           )
                log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener la conexión {e}')
                sys.exit()
            else:
                return cls._conexion
    
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió la conexión de manera exitosa')
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener un cursor {e}')
        else:
            return cls._cursor
