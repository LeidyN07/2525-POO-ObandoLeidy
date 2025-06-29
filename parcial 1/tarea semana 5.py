# Programa sencillo para convertir dólares a euros

# Mostrar título
print("*****************************")
print("* CONVERSOR DE MONEDA USD → EUR *")
print("*****************************")

# Guardamos el valor del cambio (puedes cambiarlo si varía el dólar)
tasa_cambio = 0.91  # 1 dólar = 0.91 euros

# Pedimos la cantidad en dólares
dolares = float(input("Ingresa la cantidad en dólares que deseas convertir: "))

# Verificamos si la cantidad es válida
if dolares < 0:
    print("No se puede convertir una cantidad negativa.")
else:
    # Convertimos a euros
    euros = dolares * tasa_cambio

    # Mostramos el resultado
    print("Convirtiendo...")
    print(dolares, "dólares son", round(euros, 2), "euros")

# Mensaje final
print("¡Gracias por usar el conversor!")
