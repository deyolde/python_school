import psutil
import subprocess
import socket
import requests

# Lista de nombres de procesos sospechosos (Ejemplo)
spyware_sospechosos = [
    "keylogger.exe", "spyware.exe", "trojan.exe", "malware.exe", 
    "rat.exe", "darkcomet.exe", "njrat.exe", "zeus.exe"
]

def obtener_procesos():
    print("\n[+] Analizando procesos en ejecución...\n")
    for proceso in psutil.process_iter(attrs=['pid', 'name', 'exe']):
        try:
            pid = proceso.info['pid']
            nombre = proceso.info['name']
            ruta = proceso.info['exe'] or "Desconocida"

            # Verificar si el proceso está en la lista negra
            if nombre.lower() in spyware_sospechosos:
                print(f"[ALERTA] Spyware detectado: {nombre} (PID: {pid}) en {ruta}")

            # Detectar procesos sin ruta legítima
            if ruta == "Desconocida":
                print(f"[Sospechoso] Proceso sin ruta detectado: {nombre} (PID: {pid})")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def obtener_conexiones():
    print("\n[+] Analizando conexiones de red activas...\n")
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED':  # Solo conexiones activas
                ip_remota = conn.raddr.ip if conn.raddr else "Desconocida"
                puerto_remoto = conn.raddr.port if conn.raddr else "Desconocido"
                pid = conn.pid

                # Obtener nombre del proceso
                proceso = psutil.Process(pid).name() if pid else "Desconocido"

                # Verificar si la IP es sospechosa
                if ip_remota != "Desconocida":
                    try:
                        host = socket.gethostbyaddr(ip_remota)
                        print(f"Conexión activa -> Proceso: {proceso} | IP: {ip_remota} | Host: {host[0]} | Puerto: {puerto_remoto}")
                    except socket.herror:
                        print(f"[Sospechoso] Conexión desconocida -> Proceso: {proceso} | IP: {ip_remota} | Puerto: {puerto_remoto}")

    except Exception as e:
        print(f"Error al obtener conexiones: {e}")

if __name__ == "__main__":
    print("=== Análisis de Seguridad Básico ===")
    obtener_procesos()
    obtener_conexiones()
    print("\n[✓] Análisis completado.")
