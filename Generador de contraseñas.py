import random
import string

# --- ENFOQUE FUNCIONAL (Unidad 4) ---
def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Uso de join y list comprehension (Estilo funcional)
    # Esto elimina la necesidad de inicializar una variable vacía y usar un bucle tradicional
    password = "".join([random.choice(caracteres) for _ in range(longitud)])
    
    return password

# --- LÓGICA DE INTERFAZ (Unidad 3) ---
def menu():
    while True:
        print("\n--- GENERADOR DE CONTRASEÑAS SEGURAS (UIDE) ---")
        try:
            largo = int(input("¿De cuántos caracteres quieres tu clave?: "))
            
            if largo >= 8: # Añadimos una validación de seguridad mínima
                print(f"Tu nueva contraseña es: {generar_password(largo)}")
            else:
                print("Seguridad insuficiente: Se recomiendan al menos 8 caracteres.")
        
        except ValueError:
            print("Error: Ingresa un número entero válido.")

        if input("\n¿Generar otra? (s/n): ").lower() != 's':
            print("Cerrando sistema... ¡Éxitos en tu semestre!")
            break

if __name__ == "__main__":
    menu()