# main.py
from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\n===== 📦 SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            id_producto = input("ID único: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("⚠️ Error: cantidad y precio deben ser números.")
                continue

            nuevo = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(nuevo)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (ENTER si no cambia): ")
            precio = input("Nuevo precio (ENTER si no cambia): ")
            inventario.actualizar_producto(
                id_producto,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
