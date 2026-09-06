class Venta:
    """Representa la relación entre un usuario y un producto vendido."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    @property
    def usuario_id(self) -> str:
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion del usuario en la venta no puede estar vacia.")
        self._usuario_id = valor.strip()

    @property
    def producto_codigo(self) -> str:
        return self._producto_codigo

    @producto_codigo.setter
    def producto_codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El codigo del producto en la venta no puede estar vacio.")
        self._producto_codigo = valor.strip()

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if int(valor) <= 0:
            raise ValueError("La cantidad de la venta debe ser mayor a cero.")
        self._cantidad = int(valor)

    def a_diccionario(self) -> dict:
        """Convierte el objeto Venta a un diccionario compatible con JSON."""
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"  Usuario        : {self.usuario_id}\n"
            f"  Producto       : {self.producto_codigo}\n"
            f"  Cantidad       : {self.cantidad}"
        )
