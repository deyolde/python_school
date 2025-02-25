# incorporo el utf-8 para que pueda imprimir caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

# veremos la conversión o casting para obtener datos de un tipo a otro

# convertir de cadena a número
numero_string = "123"
numero_int = int(numero_string)
print(f"El número str converrido a int es {numero_int}")

# convertir de número a flotante
numero_float = float(numero_int)
print(f"El número flotante es  {numero_float} ")

# convertir de número a cadena
numero_int = 2548
numero_string = str(numero_int)
print(f"El número int convertido a str es {numero_string}")

# el tipo bool es Falso en los siguientes casos: --> FALSE
# el valor es 0, es cadena vacía, o es None
# tipo bool es True en los siguientes casos: --> TRUE
# el valor es diferente a 0, no es una cadena vacía, o es diferente a None

numero_entero = 0
dato_bool = bool(numero_entero)
print(f"El valor de dato_bool es {dato_bool}")

cadena_vacia = ""
dato_bool = bool(cadena_vacia)
print(f"El valor de dato_bool es {dato_bool}")

valor_none = None
dato_bool = bool(valor_none)
print(f"El valor de dato_bool es {dato_bool}")

numero_entero = 1
dato_bool = bool(numero_entero)
print(f"El valor de dato_bool es {dato_bool}")

cadena_vacia = " "
dato_bool = bool(cadena_vacia) 
print(f"El valor de dato_bool es {dato_bool}")

valor_none = "Hola cómo está"
dato_bool = bool(valor_none)
print(f"El valor de dato_bool es {dato_bool}")