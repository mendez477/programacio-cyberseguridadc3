#Pide 10 números y calcula la suma total.
suma = 0
for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero
print("La suma total de los 10 números es:", suma)