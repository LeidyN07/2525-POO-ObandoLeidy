import os

# ============================ #
#      DASHBOARD PRINCIPAL    #
#   Programación Orientada a Objetos - UEA
# ============================ #

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del archivo .py en consola.
    """
    ruta_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_absoluta, 'r') as archivo:
            print(f"\n📄 --- Código de: {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("⚠️ El archivo no se encontró.")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")


def mostrar_menu():
    """
    Muestra el menú de navegación para elegir el archivo a visualizar.
    """
    ruta_base = os.path.dirname(__file__)  # Ruta actual del script

    # Diccionario de opciones: Clave -> Ruta relativa del script
    opciones = {
        '1': 'UNIDAD 1/1.1 Introducción/introduccion_poo.py',
        '2': 'UNIDAD 1/1.2 Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '3': 'UNIDAD 2/2.1 Clases y Objetos/clases_y_objetos.py',
        '4': 'UNIDAD 2/2.2 Encapsulamiento/encapsulamiento.py',
        '5': 'UNIDAD 3/Herencia/herencia_ejemplo.py',
        '6': 'UNIDAD 4/Polimorfismo/polimorfismo.py'
        # Puedes agregar más scripts aquí
    }

    while True:
        print("\n==========================")
        print("📚 DASHBOARD DE PROYECTOS")
        print("==========================")
        for key, value in opciones.items():
            tema = value.split("/")[-1].replace(".py", "")
            print(f"{key}. {tema}")

        print("0. ❌ Salir")
        eleccion = input("\n👉 Elige una opción para ver el código: ")

        if eleccion == '0':
            print("\n👋 ¡Gracias por usar el Dashboard!\n")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("⚠️ Opción no válida. Intenta nuevamente.")

# ===================================== #
#            EJECUCIÓN DEL PROGRAMA     #
# ===================================== #
if __name__ == "__main__":
    mostrar_menu()
