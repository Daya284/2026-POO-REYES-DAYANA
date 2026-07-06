class Producto:
    """Clase padre que representa un producto general del restaurante."""
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado
        self.disponibilidad = disponibilidad
    
    def obtener_precio(self):
        """Método de acceso para obtener el precio."""
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """Método de modificación para cambiar el precio con validación."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor a cero.")
            
    def mostrar_informacion(self):
        """Método genérico para mostrar información del producto."""
        estado = "Disponible" if self.disponibilidad else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"
