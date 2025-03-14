# el objeto de esta clase es realizar las operaciones sobre la base de datos
# de entidad Persona
from conexion import Conexion
from persona import Persona
from logger_base import log
from datetime import datetime, timezone
from cursorPool import CursorPool

# CRUD - Create / Read / Update / Delete
class PersonaDAO:
    '''DAO (Data Acces Object)
       CRUD (Create -  Read - Update - Delete)'''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR    = 'INSERT INTO persona(nombre_persona, apellido_persona, date_persona, upd_persona) values(%s, %s, %s, %s)'
    _ACTUALIZAR  = 'UPDATE persona SET nombre_persona = %s, apellido_persona = %s, upd_persona = %s WHERE id_persona = %s'
    _ELIMINAR    = 'DELETE FROM persona WHERE id_persona = %s'

# método para seleccionar
    @classmethod
    def seleccionar(cls):
#
        personas_select = [] # lista vacía para almacenar los objetos Persona
#
        with CursorPool as cursor_select:
            cursor_select.execute(cls._SELECCIONAR)
            registros_select = cursor_select.fetchall() # fetchall() recupera todos los registros que se hayan seleccionado
#
            for registro in registros_select:
                persona = Persona(registro[0], registro[1], registro[2], registro[3], registro[4])
                personas_select.append(persona) # agregar el objeto Persona a la lista personas
#
        return personas_select # devolver la lista de objetos Persona

# método para insertar un nuevo registro
    @classmethod
    def insertar(cls, persona):
        with CursorPool as cursor_insert:
            valores = (persona.nombre, persona.apellido, persona.datePersona, persona.updPersona)
            cursor_insert.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor_insert.rowcount # rowcount devuelve el número de filas afectadas por la consulta
            
# método para realizar la actualización de un registro
    @classmethod
    def actualizar(cls, persona):
        with CursorPool as cursor_update:
            valores = (persona.nombre, persona.apellido, persona.updPersona, persona.id_persona)
            cursor_update.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor_update.rowcount
            
# método para realizar un delete de un registro
    @classmethod
    def eliminar(cls, persona):
        with CursorPool as cursor_delete:
            valores = (persona.id_persona,)
            cursor_delete.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor_delete.rowcount
            
if __name__ == '__main__':
    timestamp_actual = datetime.now(timezone.utc)
# insertar una persona
    # persona1 = Persona(nombre='Pedro', apellido='Perez', datePersona=timestamp_actual, updPersona=timestamp_actual)
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')
    
# modificar una persona
    # persona_update = Persona(1, 'Juan Carlos', 'Juarez', timestamp_actual)
    # personas_actualizadas = PersonaDAO.actualizar(persona_update)
    # log.debug(f'Personas Actualizadas: {personas_actualizadas}')

# eliminar una persona
    persona_delete = Persona(id_persona=5)
    personas_eliminadas = PersonaDAO.eliminar(persona_delete)
    log.debug(f'Personas eliminadas {personas_eliminadas}')
    
# seleccionar() devuelve una lista de objetos Persona
    personas = PersonaDAO.seleccionar() 
    for persona in personas:
        log.debug(persona) # log.debug() imprime el objeto Persona en la consola
