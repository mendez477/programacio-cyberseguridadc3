# Clase base
class Dispositivo:
    def encender(self):
        return "El dispositivo se está encendiendo..."

# Clase hija Laptop
class Laptop(Dispositivo):
    def encender(self):
        return "La laptop está iniciando el sistema operativo."

# Clase hija Teléfono
class Telefono(Dispositivo):
    def encender(self):
        return "El teléfono está mostrando la pantalla de inicio."


# Probando las clases
dispositivos = [Laptop(), Telefono(), Dispositivo()]

for d in dispositivos:
    print(f"{d.__class__.__name__}: {d.encender()}")