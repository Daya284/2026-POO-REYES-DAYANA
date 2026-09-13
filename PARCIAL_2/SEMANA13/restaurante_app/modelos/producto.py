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

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio:.2f} - Stock: {self.cantidad}"
