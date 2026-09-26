class Venta:
    """
    Modelo que representa una venta del restaurante.
    Relaciona un usuario con un producto e incluye la fecha de la operación.

    Semana 15: este modelo se incorpora para representar la operación de venta
    como parte del flujo de manejo de eventos.
    """

    def __init__(self, id, id_usuario, nombre_usuario, id_producto,
                 nombre_producto, precio_producto, fecha):
        self.id = id
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.fecha = fecha

    def a_diccionario(self):
        """Convierte el objeto Venta a un diccionario para persistencia en JSON."""
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "id_producto": self.id_producto,
            "nombre_producto": self.nombre_producto,
            "precio_producto": self.precio_producto,
            "fecha": self.fecha
        }

    def __str__(self):
        return (f"Venta #{self.id} - {self.nombre_producto} "
                f"(${self.precio_producto:.2f}) - {self.nombre_usuario} - {self.fecha}")
