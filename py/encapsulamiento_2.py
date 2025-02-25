# # The word `ahora` in the code comments is used to indicate a change or update in the code. In this
# context, it is used to highlight that the code is now incorporating the use of decorators,
# specifically the `@property` decorator in Python, to simplify the code by defining getter and
# setter methods in a more Pythonic way. The `@property` decorator allows you to define properties
# as if they were attributes, making the code cleaner and more readable.
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
        
# definimos los métodos get de un modo más con la filosofía de python
    # def get_nombre(self):
    #     return self._nombre
    @property  
    def nombre(self):
        return self._nombre
    
    # def get_apellido(self):
    #     return self._apellido
    @property 
    def apellido(self):
        return self._apellido

    # def get_edad(self):
    #     return self._edad
    @property 
    def edad(self):
        return self._edad

# definimos los métodos set de un modo más con la filosofía de python
    # def set_nombre(self, nombre):
    #     self._nombre = nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # def set_apellido(self, apellido):
    #     self._apellido = apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # def set_edad(self, edad):
    #     self._edad = edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

# programa principal - se accede al Estado debido al metodo imprimir
if __name__ == '__main__':
    # creación de una persona
    persona1 = Persona('David', 'Yolde', '56')
    persona1.imprimir()

# ahora con los métodos get y set
#         nombre: {persona1.get_nombre()}
    print(f'''Los datos de la persona mediante property, son:
          nombre: {persona1.nombre}
          apellido: {persona1.apellido}
          edad: {persona1.edad}
          ''')
    
# ahora cambiamos los datos con setter
    persona1.apellido = "Perez"
    persona1.nombre   = "Julio"
    persona1.edad     = 80

# imprimimos con método de la clase, modificados con setter
    persona1.imprimir()




