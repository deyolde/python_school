# funciones en python
# las funciones son bloques de código que nos sirven para realizar una determinada tarea
# tienen ciertas ventajas, tales como
# modularidad: se separa el programa en bloques de código más pequeños
# escalabilidad: se puede ir creciendo en la cantidad de funciones a usar, sin temor a agrandar el tamaño del código
# mantenimiento: y participación: favorece el mantenimiento y la participación, porque pueden colaborar varias
#                                 personas.
# reutilización de código: permite que el peso del código principal no crezca
# legilibilidad del código: permite que el código principal y la funcionalidad sean comprensibles.

def mi_funcion_saludo():    # firma del proyecto
    print("Estoy saludando desde una Función")

def mi_funcion_suma(num1, num2):
    print(f'La suma de {num1} y {num2} es {num1 + num2} = {num1 + num2}') # print(num1 + num2)

def superheroe_superpoder(nombre, *args, **kwargs):
    print(f'El superheroe {nombre} tiene los siguientes superpoderes:')
    for superpoder in args:
        print(superpoder)

    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

# programa principal
print('******* Funciones en Python ***********')
mi_funcion_saludo()

# podemos pasar parámetros a las funciones
mi_funcion_suma(10, 20)

# podemos pasar argumentos y kwargs a las funciones
superheroe_superpoder('Batman', 'Fuerza', 'Velocidad', 'Volar', 'Super Fuerza', 'Super Velocidad', 'Super Volar')

