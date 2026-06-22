# Clase que representa un producto (plato o bebida) del restaurante

class Producto:
    """Representa un producto disponible en el menú del restaurante."""
    
    def __init__(self, nombre, precio, tipo, descripcion=""):
        """
        Inicializa un producto con sus atributos.
        
        Args:
            nombre: nombre del producto
            precio: precio del producto
            tipo: tipo de producto (plato, bebida, postre, etc.)
            descripcion: descripción adicional del producto
        """
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.descripcion = descripcion
    
    def obtener_informacion(self):
        """Retorna información detallada del producto."""
        info = f"{self.nombre} - ${self.precio}"
        if self.descripcion:
            info += f" ({self.descripcion})"
        return info
    
    def __str__(self):
        """Representación en texto del producto."""
        return f"[{self.tipo.upper()}] {self.nombre} - ${self.precio}"
    
    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento al precio del producto.
        
        Args:
            porcentaje: porcentaje de descuento (0-100)
        
        Returns:
            el nuevo precio con descuento aplicado
        """
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        return self.precio
