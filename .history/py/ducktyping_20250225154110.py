# El Duck Typing en Python es un concepto de la programación dinámica que se basa en el
# comportamiento de un objeto en lugar de su tipo explícito.
# 👉 Explicación sencilla:
# Si un objeto se comporta como un pato (camina como un pato y hace "cuac" como un pato), 
# entonces Python lo trata como un pato, sin importar si realmente es un pato. 🦆
# En términos de programación:
# "No me importa de qué tipo es el objeto, solo me importa si puede hacer lo que necesito."

class Pato:
    def hacer_sonido(self):
        return "¡Cuac cuac!"

class Persona:
    def hacer_sonido(self):
        return "¡Hola!"

# Función que no se fija en el tipo de objeto, solo en si tiene el método hacer_sonido
def reproducir_sonido(ser):
    print(ser.hacer_sonido())

# Crear instancias
pato = Pato()
persona = Persona()

# Usar la función
reproducir_sonido(pato)    # Salida: ¡Cuac cuac!
reproducir_sonido(persona) # Salida: ¡Hola!