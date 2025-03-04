# veremos ómo se trabaja con archivos en python
# En python se pueden manejar archivos de tipo texto, como los populares txt
# También de tipo binarios: audio, foto, etc

# archivos de tipo txt

# como la sentencia open() puede generar una excepción, se lo mete en un bloque de control

try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
# se abre un archivo o se crea si no exite; en este caso creamos uno para write
    archivo.write('Agrego datos sí o sí al archivo\n')
    archivo.write('Te mando saludos.')
except Exception as e:
    print('Error archivo ',e)
else:
    print('archivo creado')
finally:
    archivo.close()
    
# ----------------------------------------------------------------------------------------------------------------------------
# tipos de funciones para usar con archivos
# r = es para solo lectura
# a = abre el archivo ya creado y agrega información; es diferente de w porque si ya está creado y lo volvemos a abrir en w:
#     se borra la info; con a, se agregan datos
# w = crea el archivo (si no existe) y lo abre para escritura
# x = solamente crea el archivo si no exite; si existe retorna error
# w+ - escribir y leer
# r+ - leer y escirbir
# ----------------------------------------------------------------------------------------------------------------------------
# se le puede adicionar el parámetro para especificar si el tipo de archivo es binario o texto
# t - texto
# b - binario
# ----------------------------------------------------------------------------------------------------------------------------


