# Creamos una clase llamada Clima
class Clima:
    def __init__(self):
        self.temperaturas = []  # Aquí guardamos las temperaturas

    # Método para ingresar las temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio
    def calcular_promedio(self):
        suma = sum(self.temperaturas)
        cantidad = len(self.temperaturas)
        promedio = suma / cantidad
        return promedio

# Parte principal del programa
def main():
    print("CLIMA - Programación Orientada a Objetos")
    clima = Clima()  # Creamos un objeto de la clase Clima
    clima.ingresar_temperaturas()  # Llamamos al método para pedir datos
    promedio = clima.calcular_promedio()  # Calculamos el promedio
    print(f"El promedio de la semana es: {promedio:.2f} °C")

# Ejecutamos el programa
main()
