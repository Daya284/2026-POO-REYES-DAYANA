class Producto:
    """
    Modelo que representa un producto del restaurante.
    Cada producto tiene un identificador, nombre, categoría, precio y cantidad disponible.
    """

    def __init__(self, id, nombre, categoria, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def a_diccionario(self):
        """Convierte el objeto Producto a un diccionario para persistencia en JSON."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio:.2f} - Stock: {self.cantidad}"
