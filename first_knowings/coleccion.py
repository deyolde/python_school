# las listas en python son colecciones de elementos que pueden ser de cualquier tipo
# las listas son mutables, es decir, se pueden modificar; y también son dinámicas, o sea
# que pueden cambiar de tamaño en tiempo de ejecución

# incorporo el utf-8 para que pueda imprimir caracteres especiales
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

# crear una lista vacía
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for i in lista:
    print(i)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numeros:
    print(i)

nombres = ["Juan", "Pedro", "María", "Ana", "Luis", "Carlos", "Sofía", "Elena", "Jorge", "Marta"]
for i in nombres:
    print(i)

# borro la pantalla
os.system('cls')
lista_mixta = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5, ["f", 6, "g", 7], "h", 8, "i", 9, "j", 10]
for i in lista_mixta:
    print(i)

# agrego un elemento al final de la lista
lista_mixta.append("k")
for i in lista_mixta:  
    print(i)

# agrego un elemento en la posición 5 
os.system('cls')
lista_mixta.insert(5, "JUAN")
for i in lista_mixta:
    print(i)