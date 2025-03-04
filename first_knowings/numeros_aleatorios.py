# voy a generar números aleatorios, y esto se puede realizar con la librería random
# pero también se puede hacer importando solo la función randint de la librería random

import random # importo la librería random

from random import randint # importo la función randint de la librería random

# elegimos una de las dos formas de importar la librería random

numero_aleatorio = random.randint(1, 100) # genero un número aleatorio entre 1 y 100

print(f" El numero aleatorio es {numero_aleatorio}") # imprimo el número aleatorio generado


# ahora otro sistema para generar números aleatorios, id aleatorio

print('***************Generar un id aleatorio***************')
nombre_alumno   = input("Introduce tu nombre     : ") # pido el nombre del alumno
apellido_alumno = input("Introduce tu apellido   : ") # pido el apellido del alumno
anio_nacimiento = str(input("Año de nacimiento [YYYY]: ")) # pido el año de nacimiento del alumno

id_aleatorio = random.randint(1000, 9999) # genero un número aleatorio entre 1000 y 9999

solo_dos_del_nombre = nombre_alumno.strip().upper()[0:2]
solo_dos_del_apellido = apellido_alumno.strip().upper()[0:2]
solo_dos_del_anio = anio_nacimiento.strip()[2:]

#print(f'año nacimiento {anio_nacimiento} y solo dos son {solo_dos_del_anio}')
id_final_alumno = solo_dos_del_nombre + solo_dos_del_apellido + solo_dos_del_anio + str(id_aleatorio)

print('\n')
print(f'Hola {nombre_alumno}')
print('\t')
print(f'El id aleatorio de {nombre_alumno} {apellido_alumno} es {id_final_alumno}')
