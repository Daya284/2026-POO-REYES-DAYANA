# Clase que gestiona las operaciones principales del restaurante

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Gestiona los productos, clientes y operaciones del restaurante."""
    
    def __init__(self, nombre, ubicacion):
        """
        Inicializa un restaurante con su información básica.
        
        Args:
            nombre: nombre del restaurante
            ubicacion: ubicación física del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []  # Lista de productos disponibles
        self.clientes = []   # Lista de clientes registrados
    
    def registrar_producto(self, producto):
        """
        Agrega un nuevo producto al menú del restaurante.
        
        Args:
            producto: instancia de la clase Producto
        """
        self.productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' registrado exitosamente.")
    
    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el sistema.
        
        Args:
            cliente: instancia de la clase Cliente
        """
        self.clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado exitosamente.")
    
    def mostrar_menu(self):
        """Muestra todos los productos disponibles organizados por tipo."""
        if not self.productos:
            print("El menú está vacío.")
            return
        
        print("\n" + "="*50)
        print(f"MENÚ - {self.nombre}")
        print("="*50)
        
        # Agrupar productos por tipo
        tipos = {}
        for producto in self.productos:
            if producto.tipo not in tipos:
                tipos[producto.tipo] = []
            tipos[producto.tipo].append(producto)
        
        # Mostrar productos organizados
        for tipo, productos in tipos.items():
            print(f"\n{tipo.upper()}:")
            for producto in productos:
                print(f"  • {producto.obtener_informacion()}")
        
        print("="*50 + "\n")
    
    def mostrar_clientes_registrados(self):
        """Muestra todos los clientes registrados con su información."""
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        
        print("\n" + "="*50)
        print(f"CLIENTES REGISTRADOS - {self.nombre}")
        print("="*50)
        
        for i, cliente in enumerate(self.clientes, 1):
            print(f"\nCliente {i}:")
            print(cliente.obtener_informacion())
        
        print("="*50 + "\n")
    
    def registrar_pedido_cliente(self, nombre_cliente):
        """
        Registra un pedido para un cliente específico.
        
        Args:
            nombre_cliente: nombre del cliente que realiza el pedido
        """
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre_cliente.lower():
                cliente.registrar_pedido()
                print(f"✓ Pedido registrado para {cliente.nombre}.")
                return
        
        print(f"✗ Cliente '{nombre_cliente}' no encontrado en el sistema.")
    
    def obtener_estadisticas(self):
        """Retorna estadísticas del restaurante."""
        total_clientes = len(self.clientes)
        total_productos = len(self.productos)
        total_pedidos = sum(cliente.pedidos_realizados for cliente in self.clientes)
        
        estadisticas = f"""
        {self.nombre} - Ubicación: {self.ubicacion}
        Total de productos en menú: {total_productos}
        Total de clientes registrados: {total_clientes}
        Total de pedidos procesados: {total_pedidos}
        """
        return estadisticas
    
    def __str__(self):
        """Representación en texto del restaurante."""
        return f"Restaurante: {self.nombre} | Ubicación: {self.ubicacion}"
