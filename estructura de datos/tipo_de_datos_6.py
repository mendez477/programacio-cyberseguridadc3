# Pregunta al usuario si tiene internet en casa (1 = Sí, 0 = No) y guarda la respuesta como lógico.
respuesta = input("tienes internet?  (escribe 1 para si y 0 para no)" ) 

if respuesta==1:
    internet = True
elif respuesta ==0:
    internet = False
else:
    print("⚠️ Respuesta no válida. Usa 'sí' o 'no'.")
    internet = None
   
print("¿Tiene internet?:", internet)








