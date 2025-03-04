# aplicaremos mejores prácticas para hacer una conexión con la bd
# creamos una clase llamada conexción
# luego un clase llamada Persona (con atributos privados)
# también una clase PersonaDAO (Data Access Object) --> ésta clase nos sirve para hacer las consulta
#                                                       sobre la bd de Personas
# también aplicaremos un logueador


# clase Persona

class Persona:
    def __init__(self, id_persona, nombre, apellido, email):
        self._id_persona = id_persona
        self._nombre     = nombre
        self._apellido   = apellido
        self._email      = email
        
