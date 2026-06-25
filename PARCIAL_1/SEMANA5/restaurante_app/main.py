from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main() -> None:
    # 1. Crear el objeto principal que administrará el sistema
    mi_restaurante = Restaurante("El Buen Sabor")
    
    # 2. Crear objetos de tipo Producto utilizando tipos básicos (str, float, bool)
    producto_1 = Producto("Hamburguesa Clásica", 5.50, "Plato Fuerte", True)
    producto_2 = Producto("Gaseosa Limón", 1.25, "Bebida", True)
    producto_3 = Producto("Tiramisú", 3.00, "Postre", False)
    
    # Agregar productos a la lista administrada por el restaurante
    mi_restaurante.agregar_producto(producto_1)
    mi_restaurante.agregar_producto(producto_2)
    mi_restaurante.agregar_producto(producto_3)
    
    # 3. Crear objetos de tipo Cliente con identificadores descriptivos
    cliente_1 = Cliente("Juan Pérez", 30, "0991234567", False)
    cliente_2 = Cliente("María Gómez", 25, "0987654321", True)
    
    # Registrar clientes en el sistema
    mi_restaurante.registrar_cliente(cliente_1)
    mi_restaurante.registrar_cliente(cliente_2)
    
    # 4. Mostrar información registrada de forma organizada
    print("Bienvenidos al sistema de gestión de restaurante.\n")
    
    mi_restaurante.mostrar_menu()
    print("")  # Salto de línea para separar la salida en consola
    
    mi_restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()
