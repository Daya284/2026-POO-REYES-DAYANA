from modelos.producto import Producto

class Bebida(Producto):
    """Clase hija que representa una bebida del restaurante."""
    def __init__(self, nombre, precio, disponibilidad, volumen_ml):
        # Utilizar super() para inicializar atributos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml  # Atributo específico de Bebida
        
    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre (Polimorfismo)."""
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tipo: Bebida | Volumen: {self.volumen_ml} ml"
