# el objeto de esta clase es realizar las operaciones sobre la base de datos
# de entidad Persona
from conexion import Conexion
from persona import Persona
from logger_base import log
# CRUD - Create / Read / Update / Delete
class PersonaDAO:
    '''DAO (Data Acces Object)
       CRUD (Create -  Read - Update - Delete)'''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR    = 'INSERT INTO persona(nombre, apellido, email) values(%s, %S, %s)'
    _ACTUALIZAR  = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s'
    _ELIMINAR    = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):

        with Conexion.obtenerConexion() as cursor: # obtenerConexion() devuelve un objeto conexión
            cursor.execute(cls._SELECCIONAR) # execute() ejecuta una consulta SQL
            registros = cursor.fetchall() # fetchall() recupera todos los registros que se hayan seleccionado
            personas = [] # lista vacía para almacenar los objetos Persona

            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona) # agregar el objeto Persona a la lista personas
                return personas # devolver la lista de objetos Persona
            
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                log.debug(f'Persona a insertar: {persona}')
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount # rowcount devuelve el número de filas afectadas por la consulta
            
if __name__ == '__main__':
# insertar una persona
    persona1 = Persona(nombre='Juan', apellido='Perez', email='jperez@mail.com')
    PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {PersonaDAO.insertar(persona1)}')
    # seleccionar 
    personas = PersonaDAO.seleccionar() # seleccionar() devuelve una lista de objetos Persona
    for persona in personas:
        log.debug(persona) # log.debug() imprime el objeto Persona en la consola