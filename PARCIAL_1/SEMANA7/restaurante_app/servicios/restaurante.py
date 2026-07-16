from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio encargada de administrar las listas de productos y clientes."""

    def __init__(self):
        # Listas para almacenar los objetos creados
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto):
        """Agrega un producto a la lista de productos del restaurante."""
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado con éxito.")

    def listar_productos(self):
        """Muestra todos los productos registrados en el sistema."""
        if not self.productos:
            print("No hay productos registrados en el restaurante.")
            return
        
        print("\n--- Lista de Productos ---")
        for idx, prod in enumerate(self.productos, 1):
            print(f"{idx}. {prod.mostrar_informacion()}")

    def buscar_producto(self, nombre: str):
        """Busca un producto por su nombre ignorando mayúsculas/minúsculas."""
        # Se busca cualquier producto que contenga la cadena ingresada
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if not encontrados:
            print(f"No se encontró ningún producto que coincida con '{nombre}'.")
            return
        
        print(f"\n--- Resultados de búsqueda para '{nombre}' ---")
        for p in encontrados:
            print(p.mostrar_informacion())

    def registrar_cliente(self, cliente: Cliente):
        """Agrega un cliente a la lista de clientes del restaurante."""
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado con éxito.")

    def listar_clientes(self):
        """Muestra todos los clientes registrados en el sistema."""
        if not self.clientes:
            print("No hay clientes registrados en el sistema.")
            return
        
        print("\n--- Lista de Clientes ---")
        for idx, cli in enumerate(self.clientes, 1):
            print(f"{idx}. ID: {cli.id_cliente} | Nombre: {cli.nombre} | Correo: {cli.correo}")

    def buscar_cliente(self, id_cliente: str):
        """Busca un cliente exactamente por su ID."""
        for cli in self.clientes:
            if cli.id_cliente == id_cliente:
                print(f"\n--- Cliente Encontrado ---")
                print(f"ID: {cli.id_cliente} | Nombre: {cli.nombre} | Correo: {cli.correo}")
                return
        print(f"No se encontró ningún cliente con el ID '{id_cliente}'.")
