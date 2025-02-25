# definimos el ciclo while

# inicializamos la variable
i = 0

print("Ciclo while")

# definimos el ciclo while
while i < 10:
    print('ciclo while: ', i)
    i += 1

# ahora definimos el ciclo for
cadena_de_caracters = 'Hola Mundo'

for caracter in cadena_de_caracters:
    print('ciclo for: ', caracter)


# y ahora definimos el ciclo for con un rango
for i in range(10):
    print('ciclo for con rango: ', i)

# y ahora definimos el ciclo for con un rango, pero con un inicio y un fin
for i in range(5, 10):
    print('ciclo for con rango: ', i) # por defecto, si no el incremento, es de 1

for i in range(0,9,2):
    print('ciclo for con rango: ', i) # ahora el incremento es de 2