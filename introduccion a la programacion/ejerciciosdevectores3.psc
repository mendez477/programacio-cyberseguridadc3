Algoritmo ejerciciosdevectores3
	Definir ajaa,numerobuscado Como Entero
	Definir esemismo Como Logico
	dimension num[8]
	//completar vector
	para ajaa <- 1 Hasta 8 Con Paso 1
		Escribir " coloque el  valor: ", ajaa
		Leer num[ajaa]
	FinPara
	// solicitud del numero
	Escribir "coloque el numero que desea buscar: "
	Leer numerobuscado
	// busqueda
	esemismo <- Falso
	para ajaa <- 1 Hasta 8
		si num[ajaa] = numerobuscado Entonces
			esemismo <- Verdadero
		FinSi
	FinPara
	si esemismo Entonces
		Escribir "el numero: " , numerobuscado, " fue encontrado en el verctor."
	SiNo
		Escribir "el numero: ", numerobuscado, " no fue encontrado en el vector."
	FinSi
FinAlgoritmo
