class Restaurante:
    """Clase de servicio que administra los productos del restaurante."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_productos = []
        
    def agregar_producto(self, producto):
        """Agrega un producto a la lista administrada."""
        self.lista_productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente al restaurante.")
        
    def mostrar_menu(self):
        """Recorre la lista de productos y muestra la información de cada uno, demostrando polimorfismo."""
        print(f"\n--- Menú del Restaurante '{self.nombre}' ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
        else:
            for producto in self.lista_productos:
                # Aquí se evidencia el polimorfismo al llamar a mostrar_informacion()
                # que ejecutará la versión de Platillo o de Bebida según corresponda.
                print(producto.mostrar_informacion())
        print("-------------------------------------------\n")
