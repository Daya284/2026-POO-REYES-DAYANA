# Archivo: mascota.py
# Clase Mascota para Programación Orientada a Objetos

class Mascota:
    """
    Clase que representa una mascota.
    
    Atributos:
        nombre (str): El nombre de la mascota
        especie (str): La especie de la mascota (perro, gato, pájaro, etc.)
        edad (int): La edad de la mascota en años
    
    Métodos:
        mostrar_informacion(): Muestra la información de la mascota
        hacer_sonido(): Emite el sonido caracterísitco de la mascota
    """
    
    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.
        
        Args:
            nombre (str): El nombre de la mascota
            especie (str): La especie de la mascota
            edad (int): La edad de la mascota
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def mostrar_informacion(self):
        """
        Método que muestra la información de la mascota de forma organizada.
        """
        print("\n" + "="*50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("="*50)
        print(f"Nombre:   {self.nombre}")
        print(f"Especie:  {self.especie}")
        print(f"Edad:     {self.edad} años")
        print("="*50)
    
    def hacer_sonido(self):
        """
        Método que emite el sonido característico de la mascota según su especie.
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "pájaro": "¡Pío pío!",
            "conejo": "¡Squeak squeak!",
            "pez": "Blub blub...",
            "hamster": "¡Squeak!",
            "tortuga": "...",
        }
        
        # Obtener el sonido según la especie (en minúsculas)
        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, "Sonido desconocido")
        
        print(f"\n{self.nombre} ({self.especie}) hace: {sonido}")
