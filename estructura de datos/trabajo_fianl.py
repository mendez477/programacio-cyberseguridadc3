#gestor de contraseñas
import re
import secrets
import string
usuarios = []
contraseñas = []

#usuario y contraseña
def registrar_usuario():
    usuarios.append(input("Ingrese el nombre de usuario: "))
    contraseñas.append(input("Ingrese la contraseña: "))
    print("Usuario registrado correctamente.\n")

#gestion de contraseñas
def verificar_contraseña(contraseña):
    longitud = len(contraseña) >= 8
    mayuscula = re.search(r"[A-Z]", contraseña)
    minuscula = re.search(r"[a-z]", contraseña)
    numero = re.search(r"[0-9]", contraseña)
    simbolo = re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña)
    return all([longitud, mayuscula, minuscula, numero, simbolo])

def generar_alertas():
    print("\nVerificando contraseñas...")
    for i in range(len(usuarios)):
        fuerza = verificar_contraseña(contraseñas[i])
        if fuerza:
            print(f"La contraseña de {usuarios[i]} es segura.")
        else:
            print(f"La contraseña de {usuarios[i]} es débil. Considere usar al menos 8 caracteres, mayúsculas, minúsculas, números y símbolos.")



#general menu
def menu():
    while True:
        print("\n--- Gestor de Contraseñas ---")
        print("1. Registrar usuario")
        print("2. Verificar contraseñas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            generar_alertas()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
if __name__ == "__main__":
    menu()
