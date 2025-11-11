#Adivina el número secreto (ejemplo: 7)
numero_secreto = 7
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        adivinado = True    
    else:
        print("Número incorrecto. Intenta de nuevo.")