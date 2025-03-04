# importamos logueador
from logger_base import log
import psycopg2 as bd

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
                log.debug(f'Ocurrió una excepción {e}')
