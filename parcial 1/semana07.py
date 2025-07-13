# Definimos una clase llamada Persona
class Persona:
    # El constructor __init__ se activa al crear un nuevo objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado la persona: {self.nombre}, edad {self.edad}")

    # Método para mostrar información
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    # El destructor __del__ se activa cuando el objeto se elimina
    def __del__(self):
        print(f"La persona {self.nombre} ha sido eliminada de la memoria.")


# Código principal
if __name__ == "__main__":
    # Crear un objeto de la clase Persona
    persona1 = Persona("Leidy", 18)

    # Mostrar información de la persona
    persona1.mostrar_info()

    # El destructor se activará automáticamente al final del programa
