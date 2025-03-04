# vamos a ver las operaciones que se pueden hacer entre sets

# Crear dos sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Unión de sets
union_de_sets = set1 | set2
print('El set 1 es', set1) # {1, 2, 3, 4, 5}
print('El set 2 es', set2) # {4, 5, 6, 7, 8}
print(f'La unión de los sets es {union_de_sets}') # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección de sets
interseccion_de_sets = set1 & set2
print(f'La intersección de los sets es {interseccion_de_sets}') # {4, 5}

# Diferencia de sets
diferencia_de_sets = set1 - set2
print(f'La diferencia de los sets es {diferencia_de_sets}') # {1, 2, 3}
