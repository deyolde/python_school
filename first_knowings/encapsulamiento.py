# El encapsulamiento nos permite ocultar la información que almacena un objeto
# Esa información también se conoce como estado del objeto
# Para aplicar el concepto de encapsulamiento se deben aplicar dos características:
# 1 - Atributos protegidos oprivados
#     self. _nombre     # protegemos el atributo
#     self. __apellido  # ponemos en privado el atributo
#
# 2 - crear y usar los métodos get(para leer el contenido) y set(para modificar el contenido)

# con poner como protegido, alcanza, pero depende de las necesidades de nuestro proyecto

# ejemplo:
class Persona:

    def __init__(self, nombre, apllido, edad):
        self.nombre = nombre        # atributo público; se puede acceder normalmente
        self._apellido = apllido    # atributo protegido
        self.__edad = edad          # atributo privado

    def imprimir(self):
        print(f'''Datos personales: 
              Nombre: {self.nombre}
              Apellido: {self._apellido}
              Edad: {self.__edad}      
              ''')

# programa principal - se accede al Estado debido al metodo imprimir
if __name__ == '__main__':
    # creación de una persona
    persona1 = Persona('David', 'Yolde', '56')
    persona1.imprimir()

# pero si estamos por fuera de la Clase, hay formas de malas prácitcas que nos permiten acceder
# a los atributos privados y protegidos (porqu python es un lenguaje bastante flexible)

# en el caso de público no hay problema
    print(persona1.nombre)

# en el caso de un atributo protegido
    print(persona1._apellido)

# en el caso de un atributo privado
    print(persona1._Persona__edad)

# hasta podemos cambiar los datos
    persona1.nombre = "Pedro"
    persona1._apellido = "Bustamante"
    persona1._Persona__edad = 70
    persona1.imprimir()


