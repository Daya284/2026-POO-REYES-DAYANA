from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """
    Servicio principal del restaurante.
    Recibe los datos cargados por ArchivoServicio, los convierte en objetos
    del modelo y proporciona las operaciones necesarias para:
    - Validar el acceso de usuarios.
    - Listar usuarios registrados.
    - Listar productos disponibles.
    - Registrar, consultar, actualizar y eliminar productos.
    - Persistir los cambios en productos.json mediante ArchivoServicio.

    Semana 14: se incorporan operaciones CRUD sobre productos con validaciones
    de negocio centralizadas en este servicio.
    """

    def __init__(self, datos_usuarios, datos_productos, ruta_productos=None):
        """
        Inicializa el servicio convirtiendo los diccionarios recibidos
        en listas de objetos Usuario y Producto.

        Args:
            datos_usuarios: Lista de diccionarios con datos de usuarios.
            datos_productos: Lista de diccionarios con datos de productos.
            ruta_productos: Ruta al archivo productos.json para persistencia.
        """
        self.usuarios = self._crear_usuarios(datos_usuarios)
        self.productos = self._crear_productos(datos_productos)
        self.ruta_productos = ruta_productos

    # ========================
    # Métodos internos
    # ========================

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

    def _guardar_productos(self):
        """
        Persiste la lista actual de productos en el archivo JSON.
        Convierte cada objeto Producto a diccionario mediante a_diccionario().
        """
        if self.ruta_productos:
            datos = [p.a_diccionario() for p in self.productos]
            return ArchivoServicio.escribir_json(self.ruta_productos, datos)
        return False

    def _siguiente_id_producto(self):
        """Calcula el siguiente ID disponible para un nuevo producto."""
        if not self.productos:
            return 1
        return max(p.id for p in self.productos) + 1

    # ========================
    # Validación de acceso
    # ========================

    def validar_acceso(self, nombre_usuario, contrasena):
        """
        Valida las credenciales de acceso simuladas.
        Retorna el objeto Usuario si las credenciales son correctas, None en caso contrario.
        """
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                return usuario
        return None

    # ========================
    # Consultas
    # ========================

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

    def buscar_producto_por_id(self, id_producto):
        """
        Busca un producto por su identificador.

        Args:
            id_producto: ID del producto a buscar.

        Returns:
            Objeto Producto si se encuentra, None en caso contrario.
        """
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None

    # ========================
    # Operaciones CRUD
    # ========================

    def registrar_producto(self, nombre, categoria, precio, cantidad):
        """
        Registra un nuevo producto en el sistema.
        Valida que los datos sean correctos antes de crear el producto.

        Args:
            nombre: Nombre del producto (no vacío).
            categoria: Categoría del producto (no vacía).
            precio: Precio del producto (número positivo).
            cantidad: Cantidad disponible (entero no negativo).

        Returns:
            Tupla (éxito: bool, mensaje: str).
        """
        # Validaciones de negocio
        if not nombre or not nombre.strip():
            return False, "El nombre del producto es obligatorio."

        if not categoria or not categoria.strip():
            return False, "La categoría del producto es obligatoria."

        try:
            precio = float(precio)
        except (ValueError, TypeError):
            return False, "El precio debe ser un valor numérico."

        if precio <= 0:
            return False, "El precio debe ser mayor a cero."

        try:
            cantidad = int(cantidad)
        except (ValueError, TypeError):
            return False, "La cantidad debe ser un número entero."

        if cantidad < 0:
            return False, "La cantidad no puede ser negativa."

        # Crear el producto con ID automático
        nuevo_id = self._siguiente_id_producto()
        nuevo_producto = Producto(
            id=nuevo_id,
            nombre=nombre.strip(),
            categoria=categoria.strip(),
            precio=precio,
            cantidad=cantidad
        )

        self.productos.append(nuevo_producto)
        self._guardar_productos()

        return True, f"Producto '{nombre.strip()}' registrado correctamente con ID {nuevo_id}."

    def actualizar_producto(self, id_producto, nombre, categoria, precio, cantidad):
        """
        Actualiza los datos de un producto existente.
        Valida que el producto exista y que los datos sean correctos.

        Args:
            id_producto: ID del producto a actualizar.
            nombre: Nuevo nombre del producto.
            categoria: Nueva categoría del producto.
            precio: Nuevo precio del producto.
            cantidad: Nueva cantidad disponible.

        Returns:
            Tupla (éxito: bool, mensaje: str).
        """
        # Buscar el producto
        producto = self.buscar_producto_por_id(id_producto)
        if not producto:
            return False, f"No se encontró un producto con ID {id_producto}."

        # Validaciones de negocio
        if not nombre or not nombre.strip():
            return False, "El nombre del producto es obligatorio."

        if not categoria or not categoria.strip():
            return False, "La categoría del producto es obligatoria."

        try:
            precio = float(precio)
        except (ValueError, TypeError):
            return False, "El precio debe ser un valor numérico."

        if precio <= 0:
            return False, "El precio debe ser mayor a cero."

        try:
            cantidad = int(cantidad)
        except (ValueError, TypeError):
            return False, "La cantidad debe ser un número entero."

        if cantidad < 0:
            return False, "La cantidad no puede ser negativa."

        # Actualizar los datos del producto
        producto.nombre = nombre.strip()
        producto.categoria = categoria.strip()
        producto.precio = precio
        producto.cantidad = cantidad

        self._guardar_productos()

        return True, f"Producto '{producto.nombre}' (ID {id_producto}) actualizado correctamente."

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del sistema por su identificador.

        Args:
            id_producto: ID del producto a eliminar.

        Returns:
            Tupla (éxito: bool, mensaje: str).
        """
        producto = self.buscar_producto_por_id(id_producto)
        if not producto:
            return False, f"No se encontró un producto con ID {id_producto}."

        nombre = producto.nombre
        self.productos.remove(producto)
        self._guardar_productos()

        return True, f"Producto '{nombre}' (ID {id_producto}) eliminado correctamente."
