# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        # Atributos del estudiante
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    # Método para mostrar los datos del estudiante
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")

    # Método para verificar si el estudiante es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")


# Programa principal
if __name__ == "__main__":
    # Crear un objeto (instancia) de la clase Estudiante
    estudiante1 = Estudiante("Lady Obando", 19, "Tecnología de la Información")

    # Usar métodos del objeto
    estudiante1.mostrar_datos()
    estudiante1.es_mayor_de_edad()
