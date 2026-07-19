from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase hija de Producto que representa una bebida del restaurante.

    Principio abierto/cerrado (OCP): amplía el sistema agregando
    atributos y comportamiento específico sin modificar la clase
    Producto ni la lógica del servicio Restaurante.

    Principio de sustitución de Liskov (LSP): un objeto Bebida puede
    utilizarse en cualquier lugar donde se espere un Producto, ya que
    mantiene la misma interfaz y comportamiento coherente.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamanio: str,
        tipo_envase: str,
    ) -> None:
        # Reutilizamos el constructor de la clase base
        super().__init__(codigo, nombre, categoria, precio)
        self.tamanio = tamanio
        self.tipo_envase = tipo_envase

    # ── Propiedades específicas de Bebida ───────────────────────

    @property
    def tamanio(self) -> str:
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El tamanio de la bebida no puede estar vacio.")
        self._tamanio = valor.strip()

    @property
    def tipo_envase(self) -> str:
        return self._tipo_envase

    @tipo_envase.setter
    def tipo_envase(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El tipo de envase no puede estar vacio.")
        self._tipo_envase = valor.strip()

    # ── Sobrescritura polimórfica ───────────────────────────────

    def mostrar_informacion(self) -> str:
        """Devuelve la información de la bebida incluyendo los datos
        heredados de Producto y los atributos propios.

        Al sobrescribir este método se demuestra el polimorfismo:
        el servicio Restaurante invoca mostrar_informacion() sin
        necesidad de preguntar si el objeto es Producto o Bebida.
        """
        informacion_base = super().mostrar_informacion()
        return (
            f"{informacion_base}\n"
            f"  Tamanio   : {self.tamanio}\n"
            f"  Envase    : {self.tipo_envase}"
        )
