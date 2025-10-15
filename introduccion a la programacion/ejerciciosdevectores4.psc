Algoritmo ejerciciosdevectores4
	Definir suma, promedio, ajaa Como Real
	dimension calificaciones[5]
	suma<-0
	para ajaa<- 1 Hasta 5 Con Paso 1
		Escribir "ingrese la calificancion ", ajaa
		Leer calificaciones[ajaa]
		suma<-suma +calificaciones[ajaa]
	FinPara
	promedio<-suma/5
	Escribir "el promedio general es:", promedio

FinAlgoritmo
