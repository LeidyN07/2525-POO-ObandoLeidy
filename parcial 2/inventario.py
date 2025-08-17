# inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("⚠️ Ya existe un producto con ese ID. Intenta otro.")
        else:
            self.productos.append(producto)
            print(f"✅ Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                print(f"🗑 Producto '{p.nombre}' eliminado.")
                return
        print("❌ No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                print(f"🔄 Producto '{p.nombre}' actualizado.")
                return
        print("❌ No se encontró el producto.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print(f"🔎 Se encontraron {len(encontrados)} producto(s):")
            for p in encontrados:
                print("   ", p)
        else:
            print("❌ Ningún producto coincide con la búsqueda.")

    def mostrar_productos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Productos en inventario:")
            for p in self.productos:
                print("   ", p)
