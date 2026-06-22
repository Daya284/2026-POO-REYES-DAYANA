# Clase que representa un cliente del restaurante

class Cliente:
    """Representa a un cliente que visita o ha visitado el restaurante."""
    
    def __init__(self, nombre, correo, telefono):
        """
        Inicializa un cliente con sus datos de contacto.
        
        Args:
            nombre: nombre completo del cliente
            correo: correo electrónico del cliente
            telefono: número telefónico del cliente
        """
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.pedidos_realizados = 0  # Contador de pedidos
    
    def registrar_pedido(self):
        """Incrementa el contador de pedidos realizados por el cliente."""
        self.pedidos_realizados += 1
    
    def obtener_informacion(self):
        """Retorna información de contacto del cliente."""
        return f"Nombre: {self.nombre}\nCorreo: {self.correo}\nTeléfono: {self.telefono}\nPedidos realizados: {self.pedidos_realizados}"
    
    def __str__(self):
        """Representación en texto del cliente."""
        return f"{self.nombre} ({self.telefono})"
