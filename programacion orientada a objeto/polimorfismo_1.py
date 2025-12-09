class animal: 
    def hablar(self):
        return"los animales hacen ruidos"
    

class perro(animal):
    def hablar(self):
        return (" guau guap")
    
class gato(animal):
    def hablar(self):
        return "miau miau"

animales= [perro(), gato(), animal()]

for animal in animales:
    print(animal.hablar())