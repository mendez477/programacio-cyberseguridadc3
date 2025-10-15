Algoritmo ejerciciosdevectores5
	Definir cantidad,ajaa Como Entero
	dimension num[10]
	para ajaa<-1 hasta 10 Con Paso 1
		Escribir "ingrese un numero " ,ajaa,":"
		Leer num[ajaa]
		si num[ajaa] % 2=0 Entonces
			cantidad<-cantidad +1
		FinSi
	FinPara
	Escribir "cantidad de numeros pares: " ,cantidad
FinAlgoritmo
