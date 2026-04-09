import random
import string

# --- FUNCIÓN PRINCIPAL DEL GENERADOR ---
def generar_password(longitud):
    # Definimos el set de caracteres (Estructura de datos)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # ESTRUCTURA REPETITIVA (Unidad 3): Bucle for para construir la clave
    # Se repite tantas veces como el usuario indicó en 'longitud'
    password = ""
    for i in range(longitud):
        password += random.choice(caracteres)
    
    return password

# --- LÓGICA DEL PROGRAMA Y MENÚ ---
def menu():
    # ESTRUCTURA REPETITIVA (Unidad 3): Bucle While para el menú interactivo
    while True:
        print("\n--- GENERADOR DE CONTRASEÑAS SEGURAS ---")
        
        try:
            # Entrada de datos del usuario
            largo = int(input("¿De cuántos caracteres quieres tu clave?: "))

            # ESTRUCTURA LÓGICA (Unidad 3): Condicional para validar la longitud
            if largo > 0:
                resultado = generar_password(largo)
                print(f"Tu nueva contraseña es: {resultado}")
            else:
                print("Error: La longitud debe ser un número positivo.")
        
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

        # LÓGICA DE CONTROL: Decisión para repetir o salir del bucle
        opcion = input("\n¿Quieres generar otra? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa... ¡Éxitos!")
            break # Rompe el bucle repetitivo

# Ejecución del programa
if __name__ == "__main__":
    menu()