from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio que administra las listas de productos y clientes."""
    
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        # Uso de listas para almacenar múltiples objetos
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []
        
    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un objeto Producto a la lista del restaurante."""
        self.productos.append(producto)
        
    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un objeto Cliente en el sistema."""
        self.clientes.append(cliente)
        
    def mostrar_menu(self) -> None:
        """Muestra en consola todos los productos disponibles."""
        print(f"--- Menú de {self.nombre} ---")
        for producto in self.productos:
            print(producto)
            
    def mostrar_clientes(self) -> None:
        """Muestra en consola todos los clientes registrados."""
        print(f"--- Clientes de {self.nombre} ---")
        for cliente in self.clientes:
            print(cliente)
