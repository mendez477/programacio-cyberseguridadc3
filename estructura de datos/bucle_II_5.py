#Pide 5 notas, calcula la suma y el promedio final.
suma = 0
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    suma += nota
promedio = suma / 5
print(f"La suma total de las notas es: {suma}")
print(f"El promedio final es: {promedio}")
