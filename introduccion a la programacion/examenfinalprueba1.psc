Algoritmo examenfinalprueba1
		dimension usuarios[3], contraseñas[3] 
		Definir i, tieneNumero, tieneMinuscula Como Entero
		Definir c Como Caracter
		
		// Cargar los datos de usuario y contraseña
		Para i <- 1 Hasta 3 Con Paso 1 Hacer
			Escribir "Ingrese el nombre del usuario ", i, ": "
			Leer usuarios[i]
			
			Escribir "Ingrese la contraseña del usuario ", i, ": "
			Leer contraseñas[i]
			
			// Verificar condiciones
			Si Longitud(contraseñas[i]) > 8 Entonces
				tieneNumero <- 0
				tieneMinuscula <- 0
				
				Para j <- 1 Hasta Longitud(contraseñas[i]) Hacer
					c <- Subcadena(contraseñas[i], j, j)
					// Verificar si es número
					Si c >= "0" Y c <= "9" Entonces
						tieneNumero <- 1
					FinSi
					// Verificar si es minúscula
					Si c >= "a" Y c <= "z" Entonces
						tieneMinuscula <- 1
					FinSi
				FinPara
				
				Si tieneNumero = 1 Y tieneMinuscula = 1 Entonces
					Escribir "? Contraseña válida para el usuario ", usuarios[i]
				Sino
					Escribir "? La contraseña debe tener al menos una minúscula y un número."
				FinSi
			Sino
				Escribir "? La contraseña debe tener más de 8 caracteres."
			FinSi
			Escribir "------------------------------------"
		FinPara
FinAlgoritmo
