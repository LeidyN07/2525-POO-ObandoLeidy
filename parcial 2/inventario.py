# inventario.py
import json
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()  # Se cargan los productos al iniciar

    # -----------------------------
    # Métodos internos de archivo
    # -----------------------------
    def guardar_inventario(self):
        """Guarda el inventario actual en un archivo JSON."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([p.__dict__ for p in self.productos], f, ensure_ascii=False, indent=4)
            print("💾 Inventario guardado correctamente.")
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"⚠️ Error inesperado al guardar: {e}")

    def cargar_inventario(self):
        """Carga el inventario desde un archivo JSON.
        Si no existe, se crea vacío automáticamente."""
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = [Producto(**p) for p in data]
            print("📂 Inventario cargado correctamente.")
        except FileNotFoundError:
            print("⚠️ Archivo de inventario no encontrado. Se creará uno nuevo.")
            self.guardar_inventario()
        except json.JSONDecodeError:
            print("⚠️ Error: El archivo de inventario está corrupto. Se iniciará vacío.")
            self.productos = []
            self.guardar_inventario()
        except Exception as e:
            print(f"⚠️ Error inesperado al cargar: {e}")

    # -----------------------------
    # Operaciones principales
    # -----------------------------
    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("⚠️ Ya existe un producto con ese ID. Intenta otro.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print(f"✅ Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                self.guardar_inventario()
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
                self.guardar_inventario()
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

