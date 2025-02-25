import random
import string
import json
import os

PASSWORDS_FILE = "passwords.json"

def generate_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def save_password(label, password):
    passwords = load_passwords()
    passwords[label] = password
    with open(PASSWORDS_FILE, "w") as file:
        json.dump(passwords, file, indent=4)
    print(f"Clave guardada: {label} -> {password}")

def load_passwords():
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "r") as file:
            return json.load(file)
    return {}

def show_saved_passwords():
    passwords = load_passwords()
    if not passwords:
        print("No hay claves guardadas.")
    else:
        for label, password in passwords.items():
            print(f"{label}: {password}")

def main():
    while True:
        print("\nGestor de Claves")
        print("1. Generar nueva clave")
        print("2. Guardar clave")
        print("3. Ver claves guardadas")
        print("4. Salir")
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            length = int(input("Longitud de la clave: "))
            password = generate_password(length)
            print(f"Clave generada: {password}")
        elif choice == "2":
            label = input("Ingrese una etiqueta para la clave: ")
            password = input("Ingrese la clave: ")
            save_password(label, password)
        elif choice == "3":
            show_saved_passwords()
        elif choice == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
