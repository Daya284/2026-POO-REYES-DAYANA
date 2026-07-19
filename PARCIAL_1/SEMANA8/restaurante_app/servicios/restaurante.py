from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase de servicio encargada de administrar las colecciones de
    productos y clientes del restaurante.

    Responsabilidad única (SRP): gestiona el registro, la validación
    y el listado de productos y clientes.  No se encarga de la
    interacción por consola; esa responsabilidad recae en main.py.

    Abierto/cerrado (OCP): al recibir objetos de tipo Producto, el
    servicio acepta también cualquier clase hija (como Bebida) sin
    necesidad de modificar su lógica interna.

    Sustitución de Liskov (LSP): durante el listado se invoca
    mostrar_informacion() sin preguntar el tipo concreto del objeto.
    """

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    # ── Productos ───────────────────────────────────────────────

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si su código no existe en la colección.

        Tanto objetos Producto como Bebida se almacenan en la misma
        lista, ya que Bebida es una especialización válida de Producto.
        """
        if self._buscar_producto_por_codigo(producto.codigo):
            print(f"  [!] Ya existe un producto con el codigo '{producto.codigo}'.")
            return False

        self._productos.append(producto)
        print(f"  [OK] Producto '{producto.nombre}' registrado con exito.")
        return True

    def listar_productos(self) -> None:
        """Muestra todos los productos registrados utilizando polimorfismo.

        Se recorre la lista única de productos y se invoca
        mostrar_informacion() en cada elemento.  Cada objeto responde
        según su propia implementación (Producto o Bebida).
        """
        if not self._productos:
            print("  No hay productos registrados en el restaurante.")
            return

        print("\n+======================================+")
        print("|       PRODUCTOS REGISTRADOS          |")
        print("+======================================+")
        for indice, producto in enumerate(self._productos, start=1):
            tipo = type(producto).__name__
            print(f"\n  -- {indice}. [{tipo}] --")
            print(producto.mostrar_informacion())

    def _buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        """Busca un producto por su código (uso interno)."""
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    # ── Clientes ────────────────────────────────────────────────

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente si su identificación no existe."""
        if self._buscar_cliente_por_id(cliente.identificacion):
            print(f"  [!] Ya existe un cliente con la identificacion '{cliente.identificacion}'.")
            return False

        self._clientes.append(cliente)
        print(f"  [OK] Cliente '{cliente.nombre}' registrado con exito.")
        return True

    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados."""
        if not self._clientes:
            print("  No hay clientes registrados en el sistema.")
            return

        print("\n+======================================+")
        print("|        CLIENTES REGISTRADOS          |")
        print("+======================================+")
        for indice, cliente in enumerate(self._clientes, start=1):
            print(f"\n  -- {indice}. --")
            print(cliente.mostrar_informacion())

    def _buscar_cliente_por_id(self, identificacion: str) -> Cliente | None:
        """Busca un cliente por su identificación (uso interno)."""
        for cliente in self._clientes:
            if cliente.identificacion == identificacion:
                return cliente
        return None
