Algoritmo ejerciciosdefunciones4
	Definir num1,num2,num3,resultado Como Real
	Escribir "ingrese el primer numero"
	leer num1
	Escribir "ingrese el segundo numero"
	leer num2
	Escribir "ingrese el terce numero"
	leer num3
	si num1 >= num2 y num1>= num3
		resultado <-num1
	SiNo
		si num2 >= num1 y num2 >= num3 Entonces
			resultado <- num2
		sino 
			resultado <- num3
		FinSi
	FinSi
	Escribir "el numero mayor es: ",resultado
FinAlgoritmo
