Algoritmo examenfinalprueba1
		dimension usuarios[3], contrase�as[3] 
		Definir i, tieneNumero, tieneMinuscula Como Entero
		Definir c Como Caracter
		
		// Cargar los datos de usuario y contrase�a
		Para i <- 1 Hasta 3 Con Paso 1 Hacer
			Escribir "Ingrese el nombre del usuario ", i, ": "
			Leer usuarios[i]
			
			Escribir "Ingrese la contrase�a del usuario ", i, ": "
			Leer contrase�as[i]
			
			// Verificar condiciones
			Si Longitud(contrase�as[i]) > 8 Entonces
				tieneNumero <- 0
				tieneMinuscula <- 0
				
				Para j <- 1 Hasta Longitud(contrase�as[i]) Hacer
					c <- Subcadena(contrase�as[i], j, j)
					// Verificar si es n�mero
					Si c >= "0" Y c <= "9" Entonces
						tieneNumero <- 1
					FinSi
					// Verificar si es min�scula
					Si c >= "a" Y c <= "z" Entonces
						tieneMinuscula <- 1
					FinSi
				FinPara
				
				Si tieneNumero = 1 Y tieneMinuscula = 1 Entonces
					Escribir "? Contrase�a v�lida para el usuario ", usuarios[i]
				Sino
					Escribir "? La contrase�a debe tener al menos una min�scula y un n�mero."
				FinSi
			Sino
				Escribir "? La contrase�a debe tener m�s de 8 caracteres."
			FinSi
			Escribir "------------------------------------"
		FinPara
FinAlgoritmo
