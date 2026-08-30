from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Servicio encargado de administrar productos, usuarios y ventas del restaurante."""

    MENU_PRINCIPAL: tuple[str, ...] = (
        "========================================",
        "        SISTEMA DE RESTAURANTE",
        "========================================",
        "1. Registrar producto",
        "2. Buscar producto",
        "3. Actualizar producto",
        "4. Eliminar producto",
        "5. Listar productos",
        "----------------------------------------",
        "6. Registrar usuario",
        "7. Listar usuarios",
        "----------------------------------------",
        "8. Vender producto",
        "9. Consultar ventas de un usuario",
        "10. Listar todas las ventas",
        "----------------------------------------",
        "11. Mostrar categorías",
        "12. Salir",
        "========================================",
    )

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

    # ─────────────────────────────────────────────
    #  CARGA INICIAL DE DATOS
    # ─────────────────────────────────────────────

    def cargar_productos_iniciales(self, productos: list[Producto]) -> None:
        """Recibe los productos cargados desde el archivo JSON al iniciar la aplicación."""
        self._productos = productos

    def cargar_usuarios_iniciales(self, usuarios: list[Usuario]) -> None:
        """Recibe los usuarios cargados desde el archivo JSON al iniciar la aplicación."""
        self._usuarios = usuarios

    def cargar_ventas_iniciales(self, ventas: list[Venta]) -> None:
        """Recibe las ventas cargadas desde el archivo JSON al iniciar la aplicación."""
        self._ventas = ventas

    # ─────────────────────────────────────────────
    #  PRODUCTOS
    # ─────────────────────────────────────────────

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self._productos:
            if producto.codigo.lower() == codigo.strip().lower():
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
        if stock is not None:
            producto.stock = stock
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos

    # ─────────────────────────────────────────────
    #  USUARIOS
    # ─────────────────────────────────────────────

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.identificacion.lower() == identificacion.strip().lower():
                return usuario
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    # ─────────────────────────────────────────────
    #  VENTAS
    # ─────────────────────────────────────────────

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        """Registra una venta relacionando un usuario con un producto.

        Valida que:
        - El usuario exista.
        - El producto exista.
        - La cantidad solicitada sea mayor que cero.
        - Exista stock suficiente.

        Si la venta es válida, crea un objeto Venta, lo agrega a la colección,
        y disminuye el stock del producto.
        """
        usuario: Usuario | None = self.buscar_usuario(identificacion_usuario)
        producto: Producto | None = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)
        return True

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        """Filtra y retorna las ventas asociadas a un usuario específico."""
        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if venta.usuario_id.lower() == identificacion_usuario.strip().lower():
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        return self._ventas

    # ─────────────────────────────────────────────
    #  UTILIDADES
    # ─────────────────────────────────────────────

    def obtener_categorias_unicas(self) -> set[str]:
        categorias: set[str] = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias

    def obtener_menu_diccionario(self) -> dict[str, str]:
        return {
            "1": "registrar_producto",
            "2": "buscar_producto",
            "3": "actualizar_producto",
            "4": "eliminar_producto",
            "5": "listar_productos",
            "6": "registrar_usuario",
            "7": "listar_usuarios",
            "8": "vender_producto",
            "9": "consultar_ventas_usuario",
            "10": "listar_ventas",
            "11": "mostrar_categorias",
            "12": "salir",
        }
