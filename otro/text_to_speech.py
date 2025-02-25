import pyttsx3

def leer_archivo(ruta):
    """Lee y retorna el contenido de un archivo de texto."""
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def reproducir_texto(texto, factor=1.0):
    """Convierte el texto a voz y lo reproduce ajustando la velocidad."""
    engine = pyttsx3.init()
    # Obtiene la velocidad por defecto y la ajusta según el factor ingresado
    velocidad_defecto = engine.getProperty('rate')
    velocidad_nueva = int(velocidad_defecto * factor)
    engine.setProperty('rate', velocidad_nueva)
    
    engine.say(texto)
    engine.runAndWait()

if __name__ == '__main__':
    # Se solicita la ruta del archivo
    ruta_archivo = input("Introduce la ruta del archivo txt que quieres reproducir: ").strip('"\'')

    contenido = leer_archivo(ruta_archivo)
    
    # Se solicita al usuario un factor de velocidad
    try:
        factor = float(input("Introduce un factor de velocidad (por ejemplo, 0.8 para más lento, 1 para normal): "))
    except ValueError:
        print("Valor no válido. Se usará la velocidad normal.")
        factor = 1.0

    reproducir_texto(contenido, factor)
