import subprocess
import speedtest
import platform

def medir_velocidad():
    """Mide la velocidad de conexión a Internet."""
    print("\n📡 Midiendo velocidad de Internet...\n")
    st = speedtest.Speedtest()
    st.get_best_server()

    # Medición
    ping = st.results.ping
    velocidad_descarga = st.download() / 1_000_000  # Convertir a Mbps
    velocidad_subida = st.upload() / 1_000_000  # Convertir a Mbps

    print(f"🔹 Ping: {ping:.2f} ms")
    print(f"🔹 Velocidad de descarga: {velocidad_descarga:.2f} Mbps")
    print(f"🔹 Velocidad de subida: {velocidad_subida:.2f} Mbps")

    return ping, velocidad_descarga, velocidad_subida

def obtener_datos_wifi():
    """Obtiene información sobre la señal WiFi en Windows."""
    if platform.system() != "Windows":
        print("❌ Este script solo funciona en Windows para análisis de WiFi.")
        return None

    print("\n📶 Analizando conexión WiFi...\n")

    # Ejecutar el comando de Windows para obtener la señal WiFi
    cmd = "netsh wlan show interfaces"
    resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # Extraer datos útiles
    datos_wifi = {}
    for linea in resultado.stdout.split("\n"):
        if "SSID" in linea and "BSSID" not in linea:
            datos_wifi["SSID"] = linea.split(":")[-1].strip()
        if "Signal" in linea:
            try:
                datos_wifi["Señal"] = int(linea.split(":")[-1].strip().replace("%", ""))
            except ValueError:
                datos_wifi["Señal"] = None
        if "Radio type" in linea:
            datos_wifi["Tipo de Red"] = linea.split(":")[-1].strip()
        if "Channel" in linea:
            datos_wifi["Canal"] = linea.split(":")[-1].strip()
    
    for key, value in datos_wifi.items():
        print(f"🔹 {key}: {value}")

    return datos_wifi

def recomendaciones(ping, descarga, subida, datos_wifi):
    """Genera recomendaciones para mejorar la conexión."""
    print("\n🛠️ Recomendaciones para mejorar la velocidad:\n")

    if ping > 100:
        print("⚠️ El ping es alto. Recomendado reiniciar el router o cambiar a una conexión por cable.")

    if descarga < 30:
        print("⚠️ La velocidad de descarga es baja. Considera acercarte al router o cambiar de canal WiFi.")

    if subida < 10:
        print("⚠️ La velocidad de subida es baja. Asegúrate de que no haya programas consumiendo ancho de banda.")

    if datos_wifi:
        if "Señal" in datos_wifi and datos_wifi["Señal"] is not None and datos_wifi["Señal"] < 50:
            print("⚠️ La señal WiFi es débil. Prueba cambiar la ubicación del router o usar un repetidor WiFi.")

        if "Canal" in datos_wifi and datos_wifi["Canal"] in ["1", "6", "11"]:
            print("✅ Estás en un canal WiFi común. Si hay interferencias, prueba cambiarlo en la configuración del router.")

    print("\n✅ Recomendaciones generales:")
    print("1️⃣ Reinicia tu router al menos una vez por semana.")
    print("2️⃣ Usa conexión por cable si es posible.")
    print("3️⃣ Cierra programas o dispositivos que consuman ancho de banda.")

# 📌 Ejecutar análisis
ping, descarga, subida = medir_velocidad()
datos_wifi = obtener_datos_wifi()
recomendaciones(ping, descarga, subida, datos_wifi)