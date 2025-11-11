#eEjercicio 2: Listas Crea una lista llamada 'puertos_abiertos' con los valores [22, 80, 443, 8080].
#lista inicial
puertos_abiertos =[80, 22, 8080, 443]

#lista de puetos
print ("puetos abiertos: ",puertos_abiertos)

#se agrega el puerto 21
puertos_abiertos.append(21)

#eliminar puerto
puertos_abiertos.remove(8080)


#mostar puertos
puertos_ordenados = sorted(puertos_abiertos)
print("puertos abiertos: ", puertos_ordenados)

#mostrar la cantidad de puertos
print("cantidad de puertos abiertos:", len(puertos_abiertos))