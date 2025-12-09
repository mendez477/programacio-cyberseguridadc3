import math

# Clase base
class Figura:
    def area(self):
        # Método genérico, será redefinido en las clases hijas
        return 0


# Clase hija Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


# Clase hija Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# Probando las clases
figuras = [
    Circulo(5),
    Cuadrado(4),
    Figura()
]

for f in figuras:
    print(f"Área de {f.__class__.__name__}: {f.area()}")