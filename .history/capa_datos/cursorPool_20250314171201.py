# importamos logueador
from logger_base import log
from conectionPool import ConectionPool

class CursorPool:
    
    def __init__(self):
        self._connection = None
        self._cursor = None
        
    def __enter__(self):
        log.debug('Iniciamos el método with y __enter__')
        self._connection = ConectionPool.obtenerConexion()
        self._cursor = self._connection()
        return self._cursor