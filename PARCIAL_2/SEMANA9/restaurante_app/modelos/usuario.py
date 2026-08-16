class Usuario:
    """Representa a una persona registrada en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion del usuario no puede estar vacia.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre del usuario no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El correo del usuario no puede estar vacio.")
        self._correo = valor.strip()

    def mostrar_informacion(self) -> str:
        return (
            f"  Identificacion : {self.identificacion}\n"
            f"  Nombre         : {self.nombre}\n"
            f"  Correo         : {self.correo}"
        )
