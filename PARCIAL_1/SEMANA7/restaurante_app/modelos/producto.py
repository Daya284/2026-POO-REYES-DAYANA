class Producto:
    """
    Clase que representa un producto del restaurante.
    Implementa constructores tradicionales, @property y @setter para encapsulamiento.
    """
    
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Asignamos mediante las propiedades para que se validen los datos
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = valor

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = valor

    def mostrar_informacion(self) -> str:
        """Devuelve la información del producto de manera formateada."""
        estado = "Disponible" if self.disponible else "No Disponible"
        return f"[{self.categoria}] {self.nombre} - ${self.precio:.2f} ({estado})"
