# Clase base
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

    def calcular_bono(self):
        # Método genérico, puede ser redefinido en las clases hijas
        return self.salario * 0.05


# Clase hija Gerente
class Gerente(Empleado):
    def calcular_bono(self):
        # Los gerentes reciben un 20% de bono
        return self.salario * 0.20


# Clase hija Técnico
class Técnico(Empleado):
    def calcular_bono(self):
        # Los técnicos reciben un 10% de bono
        return self.salario * 0.10


# Probando las clases
empleados = [
    Gerente("Ana", 5000),
    Técnico("Luis", 3000),
    Empleado("Carlos", 2500)
]

for emp in empleados:
    print(emp.mostrar_info())
    print(f"Bono: {emp.calcular_bono()}")
    print("-" * 40)