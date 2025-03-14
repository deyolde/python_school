# aplicaremos mejores prácticas para hacer una conexión con la bd
# creamos una clase llamada conexción
# luego un clase llamada Persona (con atributos privados)
# también una clase PersonaDAO (Data Access Object) --> ésta clase nos sirve para hacer las consulta
#                                                       sobre la bd de Personas
# también aplicaremos un logueador

# importamos logueador
from logger_base import log
from datetime import datetime, timezone

# clase Persona
# el valor None es para poder pasar cualquier atributo y el otro tendrá null o lo que se especifique
class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, datePersona=None, updPersona=None):
        self._id_persona   = id_persona
        self._nombre       = nombre
        self._apellido     = apellido
        self._datePersona  = datePersona
        self._updPersona   = updPersona
        
# método str para devolver los datos de la clase persona
    def __str__(self):
        return f'''
            Id Persona: {self._id_persona},
            nombre: {self._nombre},
            apellido: {self._apellido},
            create: {self._datePersona},
            update: {self._updPersona}
    '''

# métodos get y set para modificar y recuperar persona
# get y set para id_persona
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
        
# get y set para nombre de la persona
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

# get y set para apellido de la persona
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

# get y set para date of creation of record de la persona
    @property
    def datePersona(self):
        return self._datePersona
    
    @datePersona.setter
    def datePersona(self, datePersona):
        self._datePersona = datePersona

# get y set para update record de la persona
    @property
    def updPersona(self):
        return self._updPersona
    
    @updPersona.setter
    def update(self, updPersona):
        self._updPersona = updPersona

if __name__ == '__main__':
    timestamp_actual = datetime.now(timezone.utc)
    persona1 = Persona(nombre='Susana', apellido='Torio', datePersona=timestamp_actual, updPersona=timestamp_actual)
    persona1 = Persona(nombre='Gabi', apellido='Lazarte', datePersona=timestamp_actual, updPersona=timestamp_actual)
    log.debug(persona1)