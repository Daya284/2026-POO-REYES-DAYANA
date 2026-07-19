class Cliente:
    """
    Clase que representa a un cliente registrado del restaurante.

    Responsabilidad única (SRP): se encarga exclusivamente de
    almacenar y presentar la información de un cliente.
    No hereda de Producto porque no existe una relación válida.
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    # ── Propiedades con validación ──────────────────────────────

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion del cliente no puede estar vacia.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre del cliente no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El correo del cliente no puede estar vacio.")
        self._correo = valor.strip()

    # ── Método de presentación ──────────────────────────────────

    def mostrar_informacion(self) -> str:
        """Devuelve la información formateada del cliente."""
        return (
            f"  ID        : {self.identificacion}\n"
            f"  Nombre    : {self.nombre}\n"
            f"  Correo    : {self.correo}"
        )
