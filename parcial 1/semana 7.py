# Ejemplo base (puedes modificarlo)
class Animal:
    def __init__(self, nombre):
        self._nombre = nombre  # atributo encapsulado

    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):  # polimorfismo: sobrescribe método de la clase base
        return "Ladra"

class Gato(Animal):
    def hablar(self):  # polimorfismo: sobrescribe método de la clase base
        return "Maulla"

# Instancias
mascota1 = Perro("Max")
mascota2 = Gato("Luna")

print(mascota1.hablar())  # Ladra
print(mascota2.hablar())  # Maulla
