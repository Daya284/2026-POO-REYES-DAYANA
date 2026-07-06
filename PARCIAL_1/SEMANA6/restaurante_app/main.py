from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    # 1. Crear la clase de servicio Restaurante
    mi_restaurante = Restaurante("El Buen Sabor")
    
    # 2. Crear objetos de tipo Platillo (al menos dos)
    platillo1 = Platillo("Lasaña de Carne", 12.50, True, 850)
    platillo2 = Platillo("Ensalada César", 7.00, True, 350)
    
    # 3. Crear objetos de tipo Bebida (al menos dos)
    bebida1 = Bebida("Jugo de Naranja", 3.00, True, 500)
    bebida2 = Bebida("Agua Mineral", 1.50, False, 600)
    
    # 4. Agregar los objetos creados a la lista administrada por Restaurante
    print("--- Registrando productos en el sistema ---")
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)
    
    # 5. Mostrar la información registrada demostrando polimorfismo
    mi_restaurante.mostrar_menu()
    
    # 6. Demostrar el uso de la encapsulación
    print("--- Demostrando Encapsulación y Validación ---")
    # Obtener el precio usando el método de acceso
    print(f"Precio original de '{platillo1.nombre}': ${platillo1.obtener_precio():.2f}")
    
    # Modificar precio correctamente
    platillo1.cambiar_precio(15.00)
    print(f"Nuevo precio modificado de '{platillo1.nombre}': ${platillo1.obtener_precio():.2f}")
    
    # Intentar modificar el precio con un valor inválido (negativo)
    print(f"Intentando cambiar precio de '{platillo1.nombre}' a -5.00:")
    platillo1.cambiar_precio(-5.00)
    
    # Mostrar menú actualizado
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()
