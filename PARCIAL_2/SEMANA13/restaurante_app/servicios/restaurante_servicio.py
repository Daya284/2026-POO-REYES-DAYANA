from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    """
    Servicio principal del restaurante.
    Recibe los datos cargados por ArchivoServicio, los convierte en objetos
    del modelo y proporciona las operaciones necesarias para:
    - Validar el acceso de usuarios.
    - Listar usuarios registrados.
    - Listar productos disponibles.
    - Consultar la cantidad de productos.
    """

    def __init__(self, datos_usuarios, datos_productos):
        """
        Inicializa el servicio convirtiendo los diccionarios recibidos
        en listas de objetos Usuario y Producto.
        """
        self.usuarios = self._crear_usuarios(datos_usuarios)
        self.productos = self._crear_productos(datos_productos)

    def _crear_usuarios(self, datos):
        """Convierte una lista de diccionarios en objetos Usuario."""
        lista = []
        for d in datos:
            usuario = Usuario(
                id=d["id"],
                nombre_usuario=d["nombre_usuario"],
                contrasena=d["contrasena"],
                nombre_completo=d["nombre_completo"],
                rol=d["rol"]
            )
            lista.append(usuario)
        return lista

    def _crear_productos(self, datos):
        """Convierte una lista de diccionarios en objetos Producto."""
        lista = []
        for d in datos:
            producto = Producto(
                id=d["id"],
                nombre=d["nombre"],
                categoria=d["categoria"],
                precio=d["precio"],
                cantidad=d["cantidad"]
            )
            lista.append(producto)
        return lista

    def validar_acceso(self, nombre_usuario, contrasena):
        """
        Valida las credenciales de acceso simuladas.
        Retorna el objeto Usuario si las credenciales son correctas, None en caso contrario.
        """
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                return usuario
        return None

    def obtener_usuarios(self):
        """Retorna la lista de todos los usuarios registrados."""
        return self.usuarios

    def obtener_productos(self):
        """Retorna la lista de todos los productos registrados."""
        return self.productos

    def obtener_cantidad_productos(self):
        """Retorna la cantidad total de productos registrados."""
        return len(self.productos)

    def obtener_cantidad_usuarios(self):
        """Retorna la cantidad total de usuarios registrados."""
        return len(self.usuarios)
