# incorporo el utf-8 para que pueda imprimir caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ahora realizamos la lectura de datos desde inputs
# utilizando la funcion input() de python

nombre_alumno = input("Ingrese el nombre del alumno: ")
edad_alumno = input("Ingrese la edad del alumno: ")
print(f"La edad del alumno es: {edad_alumno} y su nombre es: {nombre_alumno}")


# sistema para toma de datos de un empleado
# nombre, edad, salario, y si es jefe o no
print('****SISTEMA DE REGISTRO DE EMPLEADOS****')
# ingreso de datos
nombre_empleado  = input("Ingrese el nombre del empleado       : ")
edad_empleado    = int(input("Ingrese la edad del empleado     : ")) # convertimos a entero
salario_empleado = float(input("Ingrese el salario del empleado: ")) 
es_jefe          = input("Es jefe (si/no)                      : ")

# ahora vemos cómo se convierte si es jefe o no
resultado_es_jefe = es_jefe.lower() == "si"

# ahora imprimimos los datos del empleado
print(f"Nombre del empleado: {nombre_empleado}")
print(f"Edad del empleado: {edad_empleado}")
print(f"Salario del empleado: {salario_empleado: .2f}")
print(f"Es jefe: {resultado_es_jefe}")