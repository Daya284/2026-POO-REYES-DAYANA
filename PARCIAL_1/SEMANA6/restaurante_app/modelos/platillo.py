from modelos.producto import Producto

class Platillo(Producto):
    """Clase hija que representa una comida o plato del restaurante."""
    def __init__(self, nombre, precio, disponibilidad, calorias):
        # Utilizar super() para reutilizar el constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias  # Atributo específico de Platillo
        
    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre (Polimorfismo)."""
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tipo: Platillo | Calorías: {self.calorias} kcal"
