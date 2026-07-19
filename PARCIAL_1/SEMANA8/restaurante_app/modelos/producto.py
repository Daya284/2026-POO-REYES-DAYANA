class Producto:
    """
    Clase base que representa un producto general del restaurante.

    Responsabilidad única (SRP): esta clase se encarga exclusivamente
    de almacenar y presentar la información de un producto.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # ── Propiedades con validación ──────────────────────────────

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
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = valor

    # ── Método de presentación (polimorfismo) ───────────────────

    def mostrar_informacion(self) -> str:
        """Devuelve la información formateada del producto.

        Este método será reutilizado o sobrescrito por las clases hijas,
        garantizando el principio de sustitución de Liskov (LSP).
        """
        return (
            f"  Codigo    : {self.codigo}\n"
            f"  Nombre    : {self.nombre}\n"
            f"  Categoria : {self.categoria}\n"
            f"  Precio    : ${self.precio:.2f}"
        )
