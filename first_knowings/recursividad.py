# veremos modelos de algoritmos recursivos

# una función recursiva, es una función que se llama a sí misma, y por supuesto, cumple con ciertas características
# - se llama a sí mismacls
# - con cada llamada, se avanza hacia un ciclo base; de lo contrario se cae en bucles infinitos.

# incorporo el utf-8 para que pueda imprimir caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ejemplo de una función recursiva
    
def funcion_recursiva(numero, nivel=0):
    print(f"{'  ' * nivel}→ Entrando: funcion_recursiva({numero})")

    if numero == 1:
        print(f"{'  ' * nivel}⭐ Caso base alcanzado: {numero}")
    else:
        funcion_recursiva(numero - 1, nivel + 1)  # Llamada recursiva
        print(f"{'  ' * nivel}⬅️ Saliendo: {numero}")

if __name__ == "__main__":
    print("📚 Ejecución con trazas de pila:")
    funcion_recursiva(5)
 