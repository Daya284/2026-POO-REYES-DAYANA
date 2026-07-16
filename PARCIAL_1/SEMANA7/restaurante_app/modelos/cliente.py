from dataclasses import dataclass

@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.
    Se utiliza @dataclass para simplificar la creación de la clase.
    """
    id_cliente: str
    nombre: str
    correo: str
