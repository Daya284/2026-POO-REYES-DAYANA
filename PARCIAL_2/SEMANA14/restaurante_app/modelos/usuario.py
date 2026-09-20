class Usuario:
    """
    Modelo que representa un usuario del sistema del restaurante.
    Cada usuario tiene un identificador, nombre de usuario, contraseña,
    nombre completo y rol dentro del sistema.
    """

    def __init__(self, id, nombre_usuario, contrasena, nombre_completo, rol):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.nombre_completo = nombre_completo
        self.rol = rol

    def __str__(self):
        return f"{self.nombre_completo} ({self.nombre_usuario}) - Rol: {self.rol}"
