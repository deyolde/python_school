# importamos logueador
from logger_base import log

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
            except Exception as e:
                print(f'hubo un error {e}')
