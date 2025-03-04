# La sobreescritura en Python ocurre cuando una subclase redefine un método heredado de su clase padre para 
# cambiar su comportamiento. Es una característica clave de la herencia en la programación orientada a objetos.
# En términos simples:
# 👉 La subclase crea un método con el mismo nombre que el de la clase padre, pero con un comportamiento diferente.

# Clase padre
class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido.")

# Clase hija
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra: ¡Guau guau!")

# Crear instancias
animal = Animal()
perro = Perro()

# Llamar a los métodos
animal.hacer_sonido()  # Llama al método de la clase padre
perro.hacer_sonido()   # Llama al método sobreescrito en la subclase

