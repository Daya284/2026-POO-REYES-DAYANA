class Cliente:
    """Clase que representa a un cliente registrado en el restaurante."""
    
    def __init__(self, nombre: str, edad: int, telefono: str, es_vip: bool):
        # Atributos del cliente con sus respectivos tipos de datos
        self.nombre: str = nombre
        self.edad: int = edad
        self.telefono: str = telefono
        self.es_vip: bool = es_vip
        
    def __str__(self) -> str:
        """Retorna la representación en texto del objeto Cliente."""
        tipo: str = "VIP" if self.es_vip else "Regular"
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Tel: {self.telefono} - Tipo: {tipo}"
