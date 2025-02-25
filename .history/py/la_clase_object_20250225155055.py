# En Python, object es la clase base de todas las clases. Todas las clases, incluso las que defines tú mismo, 
# heredan indirectamente de object.
# 👉 En términos simples:
# La clase object es como el "abuelo" de todas las clases en Python. 
# Proporciona un conjunto básico de métodos que todas las instancias de las clases heredan, como __init__, __str__ y __eq__.
# Todas las clases heredan de object, por lo tanto, tienen acceso a sus métodos básicos.
# Método	Descripción	Ejemplo de Uso
# __init__	Constructor, se ejecuta al crear una instancia.	obj = MiClase()
# __str__	Representación en cadena para print().	print(obj)
# __repr__	Representación detallada para depuración.	repr(obj)
# __eq__	Compara si dos objetos son iguales (==).	obj1 == obj2
# __hash__	Devuelve un valor hash único (para usar en diccionarios).	hash(obj)
# __class__	Devuelve la clase del objeto.	obj.__class__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):  # Representación amigable
        return f"{self.nombre}, {self.edad} años"

    def __eq__(self, otro):  # Comparación personalizada
        return self.nombre == otro.nombre and self.edad == otro.edad

# Crear objetos
if __name__ == '__main__':
    p1 = Persona("Juan", 30)
    p2 = Persona("Juan", 30)
    p3 = Persona("Ana", 25)

# Usar métodos heredados de object
    print(p1)              # __str__ → Juan, 30 años
    print(p1 == p2)        # __eq__ → True (mismo nombre y edad)
    print(p1 == p3)        # __eq__ → False
    print(p1.__class__)    # Devuelve la clase del objeto
    print(hash(p1))        # Valor hash único del objeto
