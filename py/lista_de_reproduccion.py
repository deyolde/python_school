# realizaremos una lista de reproducción de música, que es una lista de canciones que se pueden 
# reproducir en un reproductor de música

# creamos la lista de reproducción
lista_de_reproduccion = []

# agregamos canciones a la lista de reproducción
lista_de_reproduccion.append("Love me do - TheBeatles")
lista_de_reproduccion.append("Rolling in the deep - Adele")
lista_de_reproduccion.append("Dancing queen - ABBA")
lista_de_reproduccion.append("Another brick in the wall - Pink Floyd")
lista_de_reproduccion.append("Bohemian Rhapsody - Queen")
lista_de_reproduccion.append("Hotel California - Eagles")
lista_de_reproduccion.append("Stairway to heaven - Led Zeppelin")
lista_de_reproduccion.append("Imagine - John Lennon")
lista_de_reproduccion.append("Like a rolling stone - Bob Dylan")
lista_de_reproduccion.append("Yesterday - The Beatles")

# mostramos la lista de reproducción sin ordenar

print("Lista de reproducción, sin ordenar:")    
for cancion in lista_de_reproduccion:
    print(cancion)

print("\n") # linea vacia

# ordenamos la lista alfabéticamente, de manerea ascendente
lista_de_reproduccion.sort()

# mostramos la lista de reproducción
print("Lista de reproducción, ordenada:")
for cancion in lista_de_reproduccion:
    print(cancion)

