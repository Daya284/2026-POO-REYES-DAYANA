import sys
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    """Muestra las opciones del menú principal del sistema."""
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")
    print("========================================")

def principal():
    # Instanciamos el servicio principal del restaurante
    sistema = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("\n--- Registrar Producto ---")
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            try:
                precio_str = input("Ingrese el precio del producto: ")
                precio = float(precio_str)
                # Creamos el objeto Producto a partir de los datos ingresados
                nuevo_producto = Producto(nombre, categoria, precio)
                sistema.registrar_producto(nuevo_producto)
            except ValueError as e:
                print(f"Error al registrar producto: {e}")
                
        elif opcion == '2':
            sistema.listar_productos()
            
        elif opcion == '3':
            print("\n--- Buscar Producto ---")
            nombre = input("Ingrese el nombre del producto a buscar: ")
            sistema.buscar_producto(nombre)
            
        elif opcion == '4':
            print("\n--- Registrar Cliente ---")
            id_cliente = input("Ingrese el ID del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            
            # Creamos el objeto Cliente usando su dataclass
            nuevo_cliente = Cliente(id_cliente=id_cliente, nombre=nombre, correo=correo)
            sistema.registrar_cliente(nuevo_cliente)
            
        elif opcion == '5':
            sistema.listar_clientes()
            
        elif opcion == '6':
            print("\n--- Buscar Cliente ---")
            id_cliente = input("Ingrese el ID del cliente a buscar: ")
            sistema.buscar_cliente(id_cliente)
            
        elif opcion == '7':
            print("Saliendo del sistema de restaurante. ¡Hasta luego!")
            sys.exit(0)
            
        else:
            print("Opción no válida. Por favor, intente de nuevo con una opción del 1 al 7.")

if __name__ == "__main__":
    # Punto de arranque del programa
    principal()
