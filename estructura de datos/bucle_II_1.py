# Muestra la tabla de multiplicar de un número ingresado por el usuario.
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1