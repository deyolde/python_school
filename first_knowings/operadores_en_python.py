# vamos a ver los diferentes operadores en python
# importamos random para generar números aleatorios
from random import randint
# operadores aritmeticos
# nos permiten realizar operaciones matemáticas básicas

numero1 = randint(1, 10)
numero2 = randint(1, 4)

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
division_entera = numero1 // numero2
modulo = numero1 % numero2
potencia = numero1 ** numero2

print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} y {numero2} es: {division}")
print(f"La división entera de {numero1} y {numero2} es: {division_entera}")
print(f"El módulo de {numero1} y {numero2} es: {modulo}")
print(f"La potencia de {numero1} y {numero2} es: {potencia}")
print()

# operadores lógicos

# operadores de comparación
print(5 < 3)
print(3==3)
resultado1 = 5 < 3
resultado2 = 3 == 3
print(resultado1 and resultado2)
print(resultado1 or resultado2)
print(not resultado1)
print()

# operadores de asignación

# operadores de identidad

# operadores de membresía

# operadores de bits

# operadores de precedencia

