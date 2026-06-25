class Producto:
    """Clase que representa un producto del restaurante (plato, bebida, etc)."""
    
    def __init__(self, nombre: str, precio: float, categoria: str, disponible: bool):
        # Atributos del producto con sus respectivos tipos de datos
        self.nombre: str = nombre
        self.precio: float = precio
        self.categoria: str = categoria
        self.disponible: bool = disponible
        
    def __str__(self) -> str:
        """Retorna la representación en texto del objeto Producto."""
        estado: str = "Disponible" if self.disponible else "Agotado"
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f} [{estado}]"
