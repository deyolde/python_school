# ahora tendremos en cuenta los decoradores, que son muy útiles para simplificar código.
# uno de ellos que viene por defecto con python y nos ayuda con el método get es
# @property

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    def imprimir(self):
        print(f'''Datos de la persona:
              Nombre: {self._nombre}
              Apellido: {self._apellido}
              Edad: {self._edad}
              ''')

    # def get_nombre(self):
    #     return self._nombre
    @property  # define el método get de un modo más con la filosofía de python
    def nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido
    
    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad

# programa principal - se accede al Estado debido al metodo imprimir
if __name__ == '__main__':
    # creación de una persona
    persona1 = Persona('David', 'Yolde', '56')
    persona1.imprimir()

# ahora con los métodos get y set
#         nombre: {persona1.get_nombre()}
    print(f'''Los datos de la persona mediante get, son:
          nombre: {persona1.nombre}
          apellido: {persona1.get_apellido()}
          edad: {persona1.get_edad()}
          ''')
    
# ahora cambiamos los datos con set
    persona1.set_apellido("PEREZ")
    persona1.set_nombre("Julio")
    persona1.set_edad(80)

# imprimimos con método de la clase
    persona1.imprimir()


