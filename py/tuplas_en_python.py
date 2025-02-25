# veremos ejemplo de tuplas en python

# definición de una tupla; los parentesis son opcionales, pero las comas no
# la característica principal de las tuplas es que son inmutables; no pueden cambiar a lo largo del tiempo
# no es lo mismo que las listas, que pueden ser redefinidas (más elementos, menos elementos, etc)
# las tuplas son más rápidas que las listas

mi_tupla_1 = ('elemento1', 'elemento2', 'elemento3', 'elemento4', 'elemento5')
mi_tupla_2 = 'elemento1', 'elemento2', 'elemento3', 'elemento4', 'elemento5'
mi_tupla_3 = "Damiel", "Ricardo", "Luis", "Juan", "Pedro"
mi_tupla_mixta = "elemento1", 2, 3.0, True, False, None
mi_tupla_unica = "elemento1", # tupla de un solo elemento

# también podemos crear tuplas vacías
mi_tupla_vacia = ()

# podemos acceder a los elementos de una tupla mediante su índice
# los índices comienzan en 0
print("****** Elemento cero de mi_tupla_1 ******")
print(mi_tupla_1[0]) # elemento1

# podemos acceder a los elementos de una tupla mediante índices negativos
# los índices negativos comienzan en -1
print("****** Elemento -1 de mi_tupla_1 ******")
print(mi_tupla_1[-1]) # elemento5

# podemos acceder a un rango de elementos de una tupla mediante slicing
# slicing: tupla[inicio:fin:incremento]
print("****** Elementos 1 al 3 de mi_tupla_1 ******")
print(mi_tupla_1[1:4]) # ('elemento2', 'elemento3', 'elemento4')

# también, como en las listas, podemos listar la tupla entera
print("****** Tupla completa mi_tupla_1 ******")
for elemento in mi_tupla_1:
    print(elemento)

# tuplas de tuplas
tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("****** Tupla de tuplas mi_tupla_de_tuplas ******")
for tupla in tuple_of_tuples:
    print(tupla)

# desempaquetado de tuplas
mi_tupla_datos = ("Damiel", 30, "Calle Falsa 123")
nombre, edad, direccion = mi_tupla_datos # aquí se desempaquetan los elementos de la tupla
print("****** Desempaquetado de tuplas ******")
print("Nombre:", nombre)
print("Edad:", edad)
print("Dirección:", direccion)

# por lo tanto, ahora podemos armar una lista que contenga tuplas; por ejemplo, una lista de productos y
# que esos productos tengan id, nombre y precio
# lista de productos
la_tupla_producto1 = (399, "Producto 1", 100.0)
la_tupla_producto2 = (400, "Producto 2", 200.0)
la_tupla_producto3 = (401, "Producto 3", 300.0)
la_tupla_producto4 = (402, "Producto 4", 400.0)
la_tupla_producto5 = (403, "Producto 5", 500.0)

lista_de_productos = [
    la_tupla_producto1,
    la_tupla_producto2,
    la_tupla_producto3,
    la_tupla_producto4,
    la_tupla_producto5
]

# ahora imprimo la lista de productos y además acumulamos el precio total de los productos
precio_total = 0.0
print("****** Lista de productos ******")
for producto in lista_de_productos:
# aplicamos el concepto de desempaquetado de tuplas
    id_producto, nombre_producto, precio_producto = producto
    print("ID:", id_producto, "Nombre:", nombre_producto, "Precio:", precio_producto)
    precio_total += precio_producto

print("Precio total de los productos:", precio_total)

