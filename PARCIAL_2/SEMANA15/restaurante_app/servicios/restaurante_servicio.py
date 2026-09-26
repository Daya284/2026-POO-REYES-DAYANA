from datetime import datetime
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
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
    - Registrar y consultar ventas (Semana 15).
    - Persistir los cambios en productos.json y ventas.json mediante ArchivoServicio.

    Semana 14: se incorporan operaciones CRUD sobre productos con validaciones
    de negocio centralizadas en este servicio.

    Semana 15: se incorpora la gestión de ventas con validaciones, persistencia
    en ventas.json y el flujo command= → callback → servicio → persistencia.
    """

    def __init__(self, datos_usuarios, datos_productos, ruta_productos=None,
                 datos_ventas=None, ruta_ventas=None):
        """
        Inicializa el servicio convirtiendo los diccionarios recibidos
        en listas de objetos Usuario, Producto y Venta.

        Args:
            datos_usuarios: Lista de diccionarios con datos de usuarios.
            datos_productos: Lista de diccionarios con datos de productos.
            ruta_productos: Ruta al archivo productos.json para persistencia.
            datos_ventas: Lista de diccionarios con datos de ventas (Semana 15).
            ruta_ventas: Ruta al archivo ventas.json para persistencia (Semana 15).
        """
        self.usuarios = self._crear_usuarios(datos_usuarios)
        self.productos = self._crear_productos(datos_productos)
        self.ruta_productos = ruta_productos

        # Semana 15: gestión de ventas
        self.ventas = self._crear_ventas(datos_ventas if datos_ventas else [])
        self.ruta_ventas = ruta_ventas

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

    def _crear_ventas(self, datos):
        """Convierte una lista de diccionarios en objetos Venta (Semana 15)."""
        lista = []
        for d in datos:
            venta = Venta(
                id=d["id"],
                id_usuario=d["id_usuario"],
                nombre_usuario=d["nombre_usuario"],
                id_producto=d["id_producto"],
                nombre_producto=d["nombre_producto"],
                precio_producto=d["precio_producto"],
                fecha=d["fecha"]
            )
            lista.append(venta)
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

    def _guardar_ventas(self):
        """
        Persiste la lista actual de ventas en el archivo JSON (Semana 15).
        Convierte cada objeto Venta a diccionario mediante a_diccionario().
        """
        if self.ruta_ventas:
            datos = [v.a_diccionario() for v in self.ventas]
            return ArchivoServicio.escribir_json(self.ruta_ventas, datos)
        return False

    def _siguiente_id_producto(self):
        """Calcula el siguiente ID disponible para un nuevo producto."""
        if not self.productos:
            return 1
        return max(p.id for p in self.productos) + 1

    def _siguiente_id_venta(self):
        """Calcula el siguiente ID disponible para una nueva venta (Semana 15)."""
        if not self.ventas:
            return 1
        return max(v.id for v in self.ventas) + 1

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

    def obtener_ventas(self):
        """Retorna la lista de todas las ventas registradas (Semana 15)."""
        return self.ventas

    def obtener_cantidad_productos(self):
        """Retorna la cantidad total de productos registrados."""
        return len(self.productos)

    def obtener_cantidad_usuarios(self):
        """Retorna la cantidad total de usuarios registrados."""
        return len(self.usuarios)

    def obtener_cantidad_ventas(self):
        """Retorna la cantidad total de ventas registradas (Semana 15)."""
        return len(self.ventas)

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

    def buscar_usuario_por_id(self, id_usuario):
        """
        Busca un usuario por su identificador (Semana 15).

        Args:
            id_usuario: ID del usuario a buscar.

        Returns:
            Objeto Usuario si se encuentra, None en caso contrario.
        """
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None

    # ========================
    # Operaciones CRUD - Productos
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

    # ========================
    # Operaciones de Ventas (Semana 15)
    # ========================

    def registrar_venta(self, id_usuario, id_producto):
        """
        Registra una nueva venta en el sistema.
        Valida que el usuario y el producto existan antes de registrar.
        La fecha se genera automáticamente al momento del registro.

        Este método es invocado desde el callback de la interfaz, siguiendo
        el flujo: command= → callback → servicio → persistencia.

        Args:
            id_usuario: ID del usuario que realiza la venta.
            id_producto: ID del producto vendido.

        Returns:
            Tupla (éxito: bool, mensaje: str).
        """
        # Validar que se proporcionaron los IDs
        if id_usuario is None:
            return False, "Debe seleccionar un usuario para registrar la venta."

        if id_producto is None:
            return False, "Debe seleccionar un producto para registrar la venta."

        # Buscar el usuario
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            return False, f"No se encontró un usuario con ID {id_usuario}."

        # Buscar el producto
        producto = self.buscar_producto_por_id(id_producto)
        if not producto:
            return False, f"No se encontró un producto con ID {id_producto}."

        # Verificar disponibilidad del producto
        if producto.cantidad <= 0:
            return False, f"El producto '{producto.nombre}' no tiene stock disponible."

        # Generar la fecha actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crear la venta con ID automático
        nuevo_id = self._siguiente_id_venta()
        nueva_venta = Venta(
            id=nuevo_id,
            id_usuario=usuario.id,
            nombre_usuario=usuario.nombre_completo,
            id_producto=producto.id,
            nombre_producto=producto.nombre,
            precio_producto=producto.precio,
            fecha=fecha_actual
        )

        # Reducir la cantidad disponible del producto
        producto.cantidad -= 1
        self._guardar_productos()

        # Agregar la venta y persistir
        self.ventas.append(nueva_venta)
        self._guardar_ventas()

        return True, (f"Venta #{nuevo_id} registrada: '{producto.nombre}' "
                      f"(${producto.precio:.2f}) vendido a {usuario.nombre_completo}.")
