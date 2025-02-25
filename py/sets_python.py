# los sets son "colecciones desordenadas de elementos únicos", también llamadas conjuntos

# Crear un set
mi_set = {1, 2, 3} 

# notamos que, en las listas usamos [], en las tuplas usamos (), y en los sets usamos {}

# ejemplos de tipo set
mi_set1 = {1, 2, 3, 4, 5, 5, 5} # los sets no permiten elementos duplicados -> por lo tanto, solo uno de los 5 se mostrará
print(f'Mi set1 es {mi_set1}') # {1, 2, 3, 4, 5}

mi_set2 = {1.0, "hola", (1, 2, 3)} # los sets pueden contener diferentes tipos de datos
print(f'Mi set con elementos diferentes es así  {mi_set2}') # {1.0, 'hola', (1, 2, 3)}

mi_set3 = set() # crear un set vacío
print(f'El set vacío es así  {mi_set3}') # set()

# los sets no tienen índices, por lo tanto no son ordenados, ni se devuelve los valores ordenados
# es decir; yo puedo imprimir 2 veces el set y venir los elementos en diferente orden

# sí se puede agregar elementos a los sets
mi_set1.add(6)
mi_set1.add(7)
mi_set1.add(8)
print(f'Impresión de mi_set1 {mi_set1}')

# tamebién se pueden eliminar elementos de los sets	
mi_set1.remove(1)
print(f'Impresión de mi_set1 {mi_set1}')

# también se puede preguntar si un elemento está en el set
print(f'¿ Está el 1 en el set ? {1 in mi_set1}') # False