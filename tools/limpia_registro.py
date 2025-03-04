import os
import winreg
import subprocess

def backup_registry():
    """Realiza un respaldo del registro antes de eliminar claves"""
    backup_path = os.path.expanduser("~") + "\\Desktop\\registry_backup.reg"
    print(f"Respaldando el registro en: {backup_path}")
    subprocess.run(["reg", "export", "HKLM", backup_path, "/y"], shell=True)
    return backup_path

def delete_invalid_keys():
    """Elimina claves inválidas del registro de Windows"""
    paths_to_clean = [
        r"Software\Microsoft\Windows\CurrentVersion\Uninstall",
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    
    for path in paths_to_clean:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_ALL_ACCESS) as key:
                i = 0
                while True:
                    try:
                        subkey = winreg.EnumKey(key, i)
                        full_path = f"{path}\\{subkey}"
                        try:
                            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, full_path) as sub_key:
                                try:
                                    value, _ = winreg.QueryValueEx(sub_key, "DisplayName")
                                    if not os.path.exists(value):
                                        print(f"Eliminando clave huérfana: {full_path}")
                                        winreg.DeleteKey(key, subkey)
                                except FileNotFoundError:
                                    pass  # Si no tiene DisplayName, seguimos
                        except FileNotFoundError:
                            pass
                        
                    except OSError:
                        break  # No hay más claves
                    i += 1
        except Exception as e:
            print(f"Error al acceder a {path}: {e}")

def main():
    print("Ejecutando limpieza del registro...")
    backup_registry()
    delete_invalid_keys()
    print("Limpieza del registro completada.")
    
if __name__ == "__main__":
    if os.name == "nt":
        main()
    else:
        print("Este script solo funciona en Windows.")
