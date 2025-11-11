#Introduce una nota (0-100). Muestra 'Aprobado con A' si es >=90, 'Aprobado' si es >=70 y 'Reprobado' en caso contrario.
nota = int(input("Ingrese su nota: "))
if nota >= 90:
    print("Aprobado con A")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")