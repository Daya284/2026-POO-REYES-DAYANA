# Archivo principal del sistema de gestión de restaurante
# Punto de entrada para demostrar el funcionamiento del sistema

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

# ============================================================
# 1. CREAR INSTANCIA DEL RESTAURANTE
# ============================================================
print("\n>>> Iniciando sistema de gestión de restaurante <<<\n")

restaurante = Restaurante("La Cocina Feliz", "Centro comercial El Eden, Piso 2")
print(f"Sistema inicializado: {restaurante}")

# ============================================================
# 2. CREAR Y REGISTRAR PRODUCTOS EN EL MENÚ
# ============================================================
print("\n--- REGISTRANDO PRODUCTOS ---")

# Crear productos
pasta_carbonara = Producto("Pasta Carbonara", 12.50, "plato", "Con queso parmesano y tocino")
hamburguesa = Producto("Hamburguesa Premium", 10.00, "plato", "Con carne 100% res")
ensalada = Producto("Ensalada Griega", 8.50, "plato", "Con queso feta y aceitunas")
cerveza = Producto("Cerveza Artesanal", 5.00, "bebida", "IPA local")
jugo = Producto("Jugo Natural", 3.50, "bebida", "Naranja y zanahoria")
flan = Producto("Flan de Caramelo", 4.00, "postre", "Hecho en casa")

# Registrar productos
restaurante.registrar_producto(pasta_carbonara)
restaurante.registrar_producto(hamburguesa)
restaurante.registrar_producto(ensalada)
restaurante.registrar_producto(cerveza)
restaurante.registrar_producto(jugo)
restaurante.registrar_producto(flan)

# ============================================================
# 3. CREAR Y REGISTRAR CLIENTES
# ============================================================
print("\n--- REGISTRANDO CLIENTES ---")

# Crear clientes
cliente1 = Cliente("Juan García", "juan.garcia@email.com", "0987654321")
cliente2 = Cliente("María López", "maria.lopez@email.com", "0912345678")
cliente3 = Cliente("Carlos Mendez", "carlos.mendez@email.com", "0998765432")

# Registrar clientes
restaurante.registrar_cliente(cliente1)
restaurante.registrar_cliente(cliente2)
restaurante.registrar_cliente(cliente3)

# ============================================================
# 4. REGISTRAR PEDIDOS
# ============================================================
print("\n--- REGISTRANDO PEDIDOS ---")

restaurante.registrar_pedido_cliente("Juan García")
restaurante.registrar_pedido_cliente("Juan García")
restaurante.registrar_pedido_cliente("María López")
restaurante.registrar_pedido_cliente("Carlos Mendez")

# ============================================================
# 5. MOSTRAR INFORMACIÓN DEL SISTEMA
# ============================================================

# Mostrar menú
restaurante.mostrar_menu()

# Mostrar clientes
restaurante.mostrar_clientes_registrados()

# Mostrar estadísticas
print("--- ESTADÍSTICAS DEL RESTAURANTE ---")
print(restaurante.obtener_estadisticas())

# ============================================================
# 6. DEMOSTRACIÓN DE OPERACIONES ADICIONALES
# ============================================================
print("\n--- OPERACIONES ADICIONALES ---")

# Aplicar descuento a un producto
print(f"\nAplicando 10% de descuento a {pasta_carbonara.nombre}...")
nuevo_precio = pasta_carbonara.aplicar_descuento(10)
print(f"Nuevo precio: ${nuevo_precio}")

# Verificar información de un cliente específico
print(f"\nDetalles de {cliente1.nombre}:")
print(cliente1.obtener_informacion())

print("\n>>> Sistema finalizado <<<\n")
