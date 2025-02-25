# El polimorfismo en Python es un concepto de la programación orientada a objetos (POO) que permite utilizar 
# un mismo nombre de método para diferentes tipos de objetos. Aunque el método tenga el mismo nombre, su comportamiento 
# puede variar según la clase del objeto.
# 👉 En términos simples: El polimorfismo permite que diferentes objetos respondan de manera distinta a un mismo mensaje o método.

class Perro:
    def hablar(self):
        return "Guau guau!"

class Gato:
    def hablar(self):
        return "Miau miau!"

# Función polimórfica
def hacer_hablar(animal):
    print(animal.hablar())

# Crear instancias
mi_perro = Perro()
mi_gato = Gato()

# Llamar al mismo método en diferentes objetos
hacer_hablar(mi_perro)  # Salida: Guau guau!
hacer_hablar(mi_gato)   # Salida: Miau miau!
