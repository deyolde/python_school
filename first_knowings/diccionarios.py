# veremos lo que son los diccionarios en python

# los diccionarios son colecciones de datos ordenados por claves; ordenadas (a partir de la versión 3.7)
# se caracterizan por tener una llave (clave) y un valor asociado a esa llave
# son mutables, es decir, se pueden modificar
# se pueden anidar, o sea, crear un diccionario dentro de otro diccionario
# se pueden eliminar elementos de un diccionario
# se pueden recorrer con un bucle for
# se pueden crear diccionarios con la función dict()
# se pueden crear diccionarios con la función dict() y con una lista de tuplas
# se pueden crear diccionarios con la función dict() y con una lista de tuplas y con un valor por defecto
# la clave de un diccionario puede ser cualquier tipo de dato inmutable (números, cadenas, tuplas)
# el valor de un diccionario puede ser cualquier tipo de dato (números, cadenas, listas, tuplas, diccionarios)
# se pueden acceder a los elementos de un diccionario mediante la clave
# se pueden modificar los elementos de un diccionario mediante la clave
# se pueden añadir elementos a un diccionario mediante la clave
# las claves tienen que ser únicas, si se repiten, se quedará la última (o sea, un diccionario no tiene 2 elementos iguales)
# los diccionarios no tienen un orden, por lo que no se pueden acceder a los elementos mediante un índice
# los diccionarios se crean con llaves {} y los elementos se separan por comas 

# creación de un diccionario, con nombre del diccionario, llaves y valores
diccionario = {
    'nombre': 'Juan', 
    'edad': 23, 
    'cursos': ['Python', 'Django', 'JavaScript']
    }

# imprimimos el diccionario y el tipo de dato
print(' ***** imprimimos el diccionario y el tipo de dato *****')
print(diccionario, type(diccionario))

# imprimimos los datos del diccionario
print(f'\n')

# formas de imprimir los datos de un diccionario
print(f'***** con la f adelante *****')
print(f'imprimimos el nombre {diccionario["nombre"]}')
print(f'imprimimos la edad {diccionario["edad"]}')
print(f'imprimimos los cursos {diccionario["cursos"]}')
print(f'\n')

# ahora sin la f
print(f'***** sin la f adelante *****')
print("imprimimos el nombre ", diccionario['nombre'])
print("imprimimos la edad ", diccionario['edad'])
print("imprimimos los cursos ", diccionario['cursos'])
print(f'\n')

# ahora con el método get
print(f'***** con el método get *****')
print("imprimimos el nombre", diccionario.get('nombre'))
print("imprimimos la edad", diccionario.get('edad'))
print("imprimimos los cursos", diccionario.get('cursos'))

# listar diccionario con el método items(), que permite recorrer el diccionario y obtener la clave y el valor
# usando el concepto de unpacking
print(f'\n')
print(' ***** listar diccionario con el método items() *****')
for key, value in diccionario.items():
    print(key, value)

# listar diccionario con el método keys(), que permite recorrer el diccionario y obtener la clave
print(f'\n')
print(' ***** listar diccionario con el método keys() *****')
for key in diccionario.keys():
    print(key)

# listar diccionario con el método values(), que permite recorrer el diccionario y obtener el valor
print(f'\n')
print(' ***** listar diccionario con el método values() *****')
for value in diccionario.values():
    print(value)

# añadir un elemento al diccionario
print(f'\n')
print(' ***** añadir un elemento al diccionario *****')
diccionario['sexo'] = 'masculino'
print(diccionario)

# modificar un elemento del diccionario
print(f'\n')
print(' ***** modificar un elemento del diccionario *****')
diccionario['nombre'] = 'Pedro'
print(diccionario) # ya no aparece Juan, sino Pedro

# eliminar un elemento del diccionario
print(f'\n')
print(' ***** eliminar un elemento del diccionario *****')
del diccionario['sexo'] # ahora eliminamos el sexo
print(diccionario)

# eliminar un elemento del diccionario con el método pop()
print(f'\n')
diccionario.pop('edad') # eliminamos la edad
print(' ***** eliminar un elemento del diccionario con el método pop() *****')
print(diccionario)

# eliminar el último elemento del diccionario con el método popitem()
print(f'\n')
diccionario.popitem() # eliminamos el último elemento
print(' ***** eliminar el último elemento del diccionario con el método popitem() *****')
print(diccionario)

# eliminar todos los elementos del diccionario con el método clear()
print(f'\n')
diccionario.clear() # eliminamos todos los elementos
print(' ***** eliminar todos los elementos del diccionario con el método clear() *****')

# ahora imprimimos el diccionario
print(diccionario)

# eliminar el diccionario con la función del
print(f'\n')
del diccionario # eliminamos el diccionario
print(' ***** eliminar el diccionario con la función del *****')

