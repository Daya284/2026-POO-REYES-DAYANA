class Producto:
    """Representa un producto del restaurante con control de stock."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El codigo del producto no puede estar vacio.")
        self._codigo = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La categoria del producto no puede estar vacia.")
        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor a cero.")
        self._precio = float(valor)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if int(valor) < 0:
            raise ValueError("El stock del producto no puede ser negativo.")
        self._stock = int(valor)

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock del producto en la cantidad indicada.

        Lanza ValueError si la cantidad es inválida o supera el stock disponible.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if cantidad > self._stock:
            raise ValueError(
                f"Stock insuficiente. Disponible: {self._stock}, solicitado: {cantidad}."
            )
        self._stock -= cantidad

    def a_diccionario(self) -> dict:
        """Convierte el objeto Producto a un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"  Codigo    : {self.codigo}\n"
            f"  Nombre    : {self.nombre}\n"
            f"  Categoria : {self.categoria}\n"
            f"  Precio    : ${self.precio:.2f}\n"
            f"  Stock     : {self.stock}"
        )
