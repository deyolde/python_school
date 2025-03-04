import os
import psutil
import subprocess
import ctypes
import time

def es_admin():
    """Verifica si el script se está ejecutando como administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def obtener_procesos():
    """Obtiene los procesos que más CPU y RAM consumen."""
    procesos = []
    for proceso in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            procesos.append(proceso.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return sorted(procesos, key=lambda x: (x['cpu_percent'], x['memory_info'].rss), reverse=True)

def mostrar_procesos():
    """Muestra los procesos más pesados."""
    procesos = obtener_procesos()
    print("\n🔎 Procesos que consumen más recursos:\n")
    print(f"{'PID':<10}{'Nombre':<30}{'CPU (%)':<10}{'Memoria (MB)':<15}")
    print("=" * 65)
    for p in procesos[:10]:  # Mostrar solo los 10 más exigentes
        print(f"{p['pid']:<10}{p['name']:<30}{p['cpu_percent']:<10.2f}{p['memory_info'].rss / (1024*1024):<15.2f}")

def cerrar_proceso(pid):
    """Cierra un proceso por su PID."""
    try:
        proceso = psutil.Process(pid)
        proceso.terminate()
        print(f"✅ Proceso {pid} ({proceso.name()}) cerrado correctamente.")
    except Exception as e:
        print(f"⚠️ No se pudo cerrar el proceso {pid}: {e}")

def liberar_memoria():
    """Libera memoria RAM usando comandos de Windows."""
    print("\n🧹 Liberando memoria RAM...")
    try:
        subprocess.run("cmd.exe /c 'echo Limpieza de memoria en progreso...' ", shell=True)
        os.system("powershell.exe Clear-MemoryCache")
        os.system("wmic os get FreePhysicalMemory")
        print("✅ Memoria liberada correctamente.")
    except Exception as e:
        print(f"⚠️ Error al liberar memoria: {e}")

def optimizar_servicios():
    """Deshabilita servicios innecesarios para mejorar el rendimiento."""
    print("\n⚡ Optimizando servicios de Windows...")
    servicios = [
        "DiagTrack",  # Telemetría de Windows
        "SysMain",  # Superfetch (consume RAM en segundo plano)
        "WSearch",  # Indexador de Windows (si no usás búsqueda rápida)
    ]
    for servicio in servicios:
        try:
            subprocess.run(f"sc config {servicio} start=disabled", shell=True, check=True)
            subprocess.run(f"net stop {servicio}", shell=True, check=True)
            print(f"✅ Servicio {servicio} deshabilitado.")
        except subprocess.CalledProcessError:
            print(f"⚠️ No se pudo deshabilitar {servicio}.")

# 🔹 Interfaz de usuario
if __name__ == "__main__":
    if not es_admin():
        print("⚠️ Debes ejecutar este script como administrador.")
        exit()

    while True:
        print("\n🔧 Opciones de optimización:")
        print("1️⃣ Mostrar procesos más pesados")
        print("2️⃣ Cerrar un proceso manualmente")
        print("3️⃣ Liberar memoria RAM")
        print("4️⃣ Optimizar servicios de Windows")
        print("5️⃣ Salir")

        opcion = input("👉 Selecciona una opción (1-5): ")

        if opcion == "1":
            mostrar_procesos()
        elif opcion == "2":
            pid = int(input("🔹 Ingresa el PID del proceso a cerrar: "))
            cerrar_proceso(pid)
        elif opcion == "3":
            liberar_memoria()
        elif opcion == "4":
            optimizar_servicios()
        elif opcion == "5":
            print("👋 Saliendo del optimizador. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")
        
        time.sleep(2)
