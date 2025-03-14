# importamos logueador
from logger_base import log
from conectionPool import ConectionPool

class CursorPool:
    
    def __init__(self):
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        log.debug('Iniciamos el método with y __enter__')
        self._conexion = ConectionPool.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta método __exit__')
        if valor_excepcion:
            log.error(f'Ocurrió un error: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
            self._conexion.rollback()
            log.debug(f'Se realizó el rollback de la transacción')
        else:
            self._conexion.commit()
            log.debug(f'Se realizó el commit de la transacción')
            
        self._cursor.close()
        ConectionPool.liberarConexion()