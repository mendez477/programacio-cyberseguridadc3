class empleado:
    def trabajar(self):
        print("el empleado esta trabajando")

class ingeniero(empleado):
    def trabajar(self):
        print("el ingeniero esta administrando la red")

class tecnico(empleado):
    def trabajar(self):
        print("el tecnico esta reparando un servidor")



persona1 = [empleado(), ingeniero(), tecnico()]

for persona in persona1:
    persona.trabajar()