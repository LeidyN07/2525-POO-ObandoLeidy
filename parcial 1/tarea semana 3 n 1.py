# Función para pedir las temperaturas
def ingresar_temperaturas():
    temperaturas = []  # Lista vacía donde se guardarán las temperaturas
    for i in range(7):  # Se repite 7 veces, uno por cada día de la semana
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)  # Agrega la temperatura a la lista
    return temperaturas  # Devuelve la lista con todas las temperaturas

# Función para sacar el promedio
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)  # Suma todas las temperaturas
    cantidad = len(temperaturas)  # Cuenta cuántas temperaturas hay (debería ser 7)
    promedio = suma / cantidad  # Saca el promedio
    return promedio  # Devuelve el resultado

# Parte principal del programa
def main():
    print("CLIMA - Programación Tradicional")
    temperaturas = ingresar_temperaturas()  # Llama a la función para pedir datos
    promedio = calcular_promedio(temperaturas)  # Llama a la función para sacar promedio
    print(f"El promedio de la semana es: {promedio:.2f} °C")

# Ejecutamos el programa
main()
