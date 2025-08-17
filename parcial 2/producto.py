# producto.py

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Representa un producto dentro del inventario.
        """
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def valor_total(self):
        """Devuelve el valor total de este producto (cantidad x precio)."""
        return self.cantidad * self.precio

    def __str__(self):
        return f"[{self.id}] {self.nombre} | Stock: {self.cantidad} | Precio: ${self.precio:.2f} | Total: ${self.valor_total():.2f}"
