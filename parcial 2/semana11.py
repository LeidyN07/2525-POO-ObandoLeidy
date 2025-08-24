import json
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}          # Diccionario {id: Producto}
        self.historial = []          # Lista de operaciones
        self.nombres_unicos = set()  # Conjunto de nombres únicos

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("⚠️ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id] = producto
            self.nombres_unicos.add(producto.nombre)
            self.historial.append(f"Agregado: {producto.nombre}")
            print("✅ Producto agregado con éxito.")

    def eliminar_producto(self, id):
        if id in self.productos:
            eliminado = self.productos[id].nombre
            del self.productos[id]
            self.historial.append(f"Eliminado: {eliminado}")
            # Recalcular conjunto de nombres
            self.nombres_unicos = set([p.nombre for p in self.productos.values()])
            print("🗑️ Producto eliminado.")
        else:
            print("⚠️ No existe un producto con ese ID.")

    def mostrar_historial(self):
        print("📜 Historial de operaciones:")
        for h in self.historial:
            print("-", h)

    def mostrar_menu(self):
        # Usamos una tupla para las opciones
        opciones = (
            "Agregar producto",
            "Eliminar producto",
            "Actualizar producto",
            "Buscar producto por nombre",
            "Mostrar todos los productos",
            "Guardar inventario en archivo",
            "Salir"
        )
        for i, opcion in enumerate(opciones):
            print(f"{i+1}. {opcion}")
