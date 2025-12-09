# Clase base
class Vehiculo:
    def mover(self):
        return "El vehículo se está moviendo."

# Clase hija Carro
class Carro(Vehiculo):
    def mover(self):
        return "El carro avanza por la carretera."

# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta pedalea por el camino."


# Probando las clases
vehiculos = [Carro(), Bicicleta(), Vehiculo()]

for v in vehiculos:
    print(f"{v.__class__.__name__}: {v.mover()}")