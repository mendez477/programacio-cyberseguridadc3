# Valida una contraseña. Mientras no sea '1234', vuelve a pedirla.
contraseña_correcta = "1234"
contraseña_ingresada = input("Ingresa la contraseña: ")
while contraseña_ingresada != contraseña_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contraseña_ingresada = input("Ingresa la contraseña: ")
print("¡Contraseña correcta! Acceso concedido.")