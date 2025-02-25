# La herencia en Python es un concepto de la programación orientada a objetos (POO) 
# que permite crear una nueva clase basada en una clase existente. La nueva clase hereda 
# los atributos y métodos de la clase original, y puede agregar o modificar su comportamiento.

# En términos simples:
# 👉 La herencia permite reutilizar código y extender la funcionalidad de una clase existente.

# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} hace un sonido.")

# Clase hija que hereda de Animal
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} ladra: ¡Guau guau!")

# Crear instancia de la subclase
mi_perro = Perro("Firulais")

# Usar métodos heredados y propios
mi_perro.hablar()  # Método heredado de Animal
mi_perro.ladrar()  # Método propio de Perro

