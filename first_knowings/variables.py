# incorporo el utf-8 para que pueda imprimir caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')
# vamos a definir ciertas variables
# y a mostrarlas en pantalla

# Definimos una variable de tipo entero
edad = 25
altura = 1.75
nombre = "Juan"

# Mostramos las variables en pantalla
print("La edad de", nombre, "es", edad)
print("La altura de", nombre, "es", altura)

# Cambiamos el valor de la variable edad
edad = 26
print("La edad de", nombre, "es", edad) 
altura = 1.80
print("La altura de", nombre, "es", altura)

# las constantes se escriben en mayusculas
PI = 3.1416
print("El valor de PI es", PI)

NOMBRE_CLIENTE = "Juan"
print("El nombre del cliente es", NOMBRE_CLIENTE)

# importante menejo de caracteres, de manera que cada caracter se guarda como un string
# de forma que se puede recuperar como si fuera una lista de caracteres
nombre = "Juan"
print("yo puedo imprimir el nombre así", nombre)

print("o puedo imprimir cada caracter por separado")
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])

# también es neceario ver la concatenación de strings
word1 = "Hola"
word2 = "Mundo"
print(word1 + " " + word2)      # concatenación de strings 1

# pero lo puedo hacer también mediante un método
concatenacion = word1 + " " + word2
print(concatenacion)            # concatenación de strings 2

concatenacion = ''.join([word1, " ", word2])
print(concatenacion)            # concatenación de strings 3

# tambien con el concepto de f-string
concatenacion = f"{word1} {word2}"
print(concatenacion)            # concatenación de strings 4

# con el método format
concatenacion = "{} {}".format(word1, word2)
print(concatenacion)            # concatenación de strings 5


# metodos de strings
