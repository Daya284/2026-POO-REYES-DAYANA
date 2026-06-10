# Archivo: main.py
# Programa principal que demuestra el uso de la clase Mascota

from mascota import Mascota


def main():
    """
    Función principal que crea objetos de la clase Mascota y ejecuta sus métodos.
    """
    
    print("\n" + "="*50)
    print("SISTEMA DE MASCOTAS - PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("="*50)
    
    # Crear el primer objeto de la clase Mascota
    print("\n--- Creando primer objeto Mascota ---")
    mascota1 = Mascota("Max", "perro", 5)
    
    # Crear el segundo objeto de la clase Mascota
    print("--- Creando segundo objeto Mascota ---")
    mascota2 = Mascota("Michi", "gato", 3)
    
    # Crear un tercer objeto para demostrar más funcionalidad
    print("--- Creando tercer objeto Mascota ---")
    mascota3 = Mascota("Tweety", "pájaro", 2)
    
    # Mostrar información de cada mascota
    print("\n" + "="*50)
    print("MOSTRANDO INFORMACIÓN DE LAS MASCOTAS")
    print("="*50)
    
    mascota1.mostrar_informacion()
    mascota2.mostrar_informacion()
    mascota3.mostrar_informacion()
    
    # Ejecutar el método hacer_sonido() para cada mascota
    print("\n" + "="*50)
    print("SONIDOS DE LAS MASCOTAS")
    print("="*50)
    
    mascota1.hacer_sonido()
    mascota2.hacer_sonido()
    mascota3.hacer_sonido()
    
    # Demostración de acceso a atributos
    print("\n" + "="*50)
    print("DEMOSTRACIÓN DE ATRIBUTOS")
    print("="*50)
    print(f"\nLa mascota '{mascota1.nombre}' es un {mascota1.especie} de {mascota1.edad} años.")
    print(f"La mascota '{mascota2.nombre}' es un {mascota2.especie} de {mascota2.edad} años.")
    print(f"La mascota '{mascota3.nombre}' es un {mascota3.especie} de {mascota3.edad} años.")
    
    print("\n" + "="*50)
    print("¡Programa finalizado correctamente!")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
