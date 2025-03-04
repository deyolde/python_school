# aplicaremos mejores prácticas para hacer una conexión con la bd
# creamos una clase llamada conexción
# luego un clase llamada Persona (con atributos privados)
# también una clase PersonaDAO (Data Access Object) --> ésta clase nos sirve para hacer las consulta
#                                                       sobre la bd de Personas
# también aplicaremos un logueador

# importamos logueador
from logger_base import log

# clase Persona
# el valor None es para poder pasar cualquier atributo y el otro tendrá null o lo que se especifique
class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre     = nombre
        self._apellido   = apellido
        self._email      = email
        
# método str para devolver los datos de la clase persona
    def __str__(self):
        return f'''
            Id Persona: {self._id_persona},
            nombre: {self._nombre},
            apellido: {self._apellido},
            email: {self._email}
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

# get y set para enail de la persona
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    persona1 = Persona(1, 'David', 'Yolde', 'deyolde@mail.com')
    log.debug(persona1)
    persona1 = Persona('Jorge', 'Lazarte', 'jlazarte@mai.com')
    log.debug(persona1)