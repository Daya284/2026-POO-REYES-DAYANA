from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar productos y usuarios del restaurante."""

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
        "8. Mostrar categorías",
        "9. Salir",
        "========================================",
    )

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

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
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos

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
            "8": "mostrar_categorias",
            "9": "salir",
        }
