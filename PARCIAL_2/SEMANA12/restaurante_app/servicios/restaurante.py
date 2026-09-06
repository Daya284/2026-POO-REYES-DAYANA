from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Servicio encargado de administrar productos, usuarios y ventas del restaurante.

    Semana 12 — Mejora de rendimiento mediante colecciones auxiliares:
    - Se conservan las listas principales (_productos, _usuarios, _ventas) para
      almacenar, recorrer, listar y persistir los objetos.
    - Se crean índices en memoria con diccionarios para búsquedas frecuentes:
        * _indice_productos: dict[str, Producto]  → búsqueda por código de producto en O(1).
        * _indice_usuarios: dict[str, Usuario]    → búsqueda por identificación de usuario en O(1).
        * _ventas_por_usuario: dict[str, list[Venta]] → consulta de ventas agrupadas por usuario en O(1).
    - Se utiliza un set (_codigos_productos) para validar rápidamente si un código
      de producto ya existe antes de registrar uno nuevo.
    - Todas las estructuras auxiliares se mantienen sincronizadas cuando se registran,
      modifican o eliminan datos.
    - Los índices se reconstruyen al cargar datos iniciales desde JSON.
    """

    MENU_PRINCIPAL: tuple[str, ...] = (
        "========================================",
        "        SISTEMA DE RESTAURANTE",
        "========================================",
        "1. Registrar producto",
        "2. Buscar producto",
        "3. Actualizar producto",
        "4. Eliminar producto",
        "5. Listar productos",
        "----------------------------------------",
        "6. Registrar usuario",
        "7. Listar usuarios",
        "----------------------------------------",
        "8. Vender producto",
        "9. Consultar ventas de un usuario",
        "10. Listar todas las ventas",
        "----------------------------------------",
        "11. Mostrar categorías",
        "12. Salir",
        "========================================",
    )

    def __init__(self) -> None:
        # ── Colecciones principales (listas) ──
        # Se conservan para almacenar, recorrer, listar y persistir objetos.
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

        # ── Índices auxiliares (diccionarios) ──
        # Permiten búsquedas en O(1) por clave única, evitando recorrer
        # toda la lista cada vez que se necesita localizar un objeto.
        self._indice_productos: dict[str, Producto] = {}
        self._indice_usuarios: dict[str, Usuario] = {}

        # ── Índice de ventas agrupadas por usuario (diccionario de listas) ──
        # Evita recorrer toda la lista de ventas cada vez que se consultan
        # las ventas de un usuario específico.
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

        # ── Set auxiliar para validación de pertenencia ──
        # Permite verificar en O(1) si un código de producto ya existe,
        # sin necesidad de buscar en el diccionario ni recorrer la lista.
        self._codigos_productos: set[str] = set()

    # ─────────────────────────────────────────────
    #  RECONSTRUCCIÓN DE ÍNDICES
    # ─────────────────────────────────────────────

    def _reconstruir_indice_productos(self) -> None:
        """Reconstruye el índice de productos y el set de códigos a partir de la lista principal.

        Se invoca al cargar datos iniciales desde JSON para garantizar coherencia
        entre la lista y las estructuras auxiliares.
        """
        self._indice_productos.clear()
        self._codigos_productos.clear()

        for producto in self._productos:
            clave: str = producto.codigo.lower()
            self._indice_productos[clave] = producto
            self._codigos_productos.add(clave)

    def _reconstruir_indice_usuarios(self) -> None:
        """Reconstruye el índice de usuarios a partir de la lista principal.

        Se invoca al cargar datos iniciales desde JSON para garantizar coherencia
        entre la lista y la estructura auxiliar.
        """
        self._indice_usuarios.clear()

        for usuario in self._usuarios:
            clave: str = usuario.identificacion.lower()
            self._indice_usuarios[clave] = usuario

    def _reconstruir_indice_ventas(self) -> None:
        """Reconstruye el índice de ventas agrupadas por usuario a partir de la lista principal.

        Se invoca al cargar datos iniciales desde JSON para garantizar coherencia
        entre la lista y la estructura auxiliar.
        """
        self._ventas_por_usuario.clear()

        for venta in self._ventas:
            clave: str = venta.usuario_id.lower()
            if clave not in self._ventas_por_usuario:
                self._ventas_por_usuario[clave] = []
            self._ventas_por_usuario[clave].append(venta)

    # ─────────────────────────────────────────────
    #  CARGA INICIAL DE DATOS
    # ─────────────────────────────────────────────

    def cargar_productos_iniciales(self, productos: list[Producto]) -> None:
        """Recibe los productos cargados desde el archivo JSON al iniciar la aplicación.

        Después de asignar la lista, reconstruye el índice de productos y el set
        de códigos para que las búsquedas posteriores sean en O(1).
        """
        self._productos = productos
        self._reconstruir_indice_productos()

    def cargar_usuarios_iniciales(self, usuarios: list[Usuario]) -> None:
        """Recibe los usuarios cargados desde el archivo JSON al iniciar la aplicación.

        Después de asignar la lista, reconstruye el índice de usuarios para que
        las búsquedas posteriores sean en O(1).
        """
        self._usuarios = usuarios
        self._reconstruir_indice_usuarios()

    def cargar_ventas_iniciales(self, ventas: list[Venta]) -> None:
        """Recibe las ventas cargadas desde el archivo JSON al iniciar la aplicación.

        Después de asignar la lista, reconstruye el índice de ventas agrupadas
        por usuario para que las consultas posteriores sean en O(1).
        """
        self._ventas = ventas
        self._reconstruir_indice_ventas()

    # ─────────────────────────────────────────────
    #  PRODUCTOS
    # ─────────────────────────────────────────────

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un nuevo producto en el sistema.

        Semana 12: utiliza el set _codigos_productos para validar en O(1) si
        el código ya existe, en lugar de recorrer toda la lista de productos.
        Si el registro es exitoso, actualiza la lista, el índice y el set.
        """
        clave: str = producto.codigo.lower()

        # Validación de existencia en O(1) gracias al set auxiliar
        if clave in self._codigos_productos:
            return False

        # Agregar a la lista principal (persistencia y recorrido)
        self._productos.append(producto)

        # Sincronizar índice y set auxiliar
        self._indice_productos[clave] = producto
        self._codigos_productos.add(clave)

        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        """Busca un producto por su código.

        Semana 12: utiliza el diccionario _indice_productos para acceder
        directamente al producto en O(1), eliminando el recorrido lineal
        de la lista completa que se realizaba en la Semana 11.
        """
        clave: str = codigo.strip().lower()
        return self._indice_productos.get(clave)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
    ) -> bool:
        """Actualiza los atributos de un producto existente.

        Semana 12: la búsqueda del producto es en O(1) gracias al índice.
        El objeto se modifica en su lugar, por lo que la lista principal y el
        índice permanecen sincronizados automáticamente (apuntan al mismo objeto).
        """
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
        if stock is not None:
            producto.stock = stock
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto del sistema.

        Semana 12: la búsqueda es en O(1) mediante el índice. Al eliminar,
        se sincroniza la lista principal, el diccionario y el set auxiliar.
        """
        clave: str = codigo.strip().lower()
        producto: Producto | None = self._indice_productos.get(clave)

        if producto is None:
            return False

        # Eliminar de la lista principal
        self._productos.remove(producto)

        # Sincronizar índice y set auxiliar
        del self._indice_productos[clave]
        self._codigos_productos.discard(clave)

        return True

    def listar_productos(self) -> list[Producto]:
        """Retorna la lista principal de productos para recorrido, listado y persistencia."""
        return self._productos

    # ─────────────────────────────────────────────
    #  USUARIOS
    # ─────────────────────────────────────────────

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un nuevo usuario en el sistema.

        Semana 12: utiliza el diccionario _indice_usuarios para validar en O(1)
        si la identificación ya existe, en lugar de recorrer toda la lista.
        Si el registro es exitoso, actualiza la lista y el índice.
        """
        clave: str = usuario.identificacion.lower()

        # Validación de existencia en O(1) gracias al índice
        if clave in self._indice_usuarios:
            return False

        # Agregar a la lista principal
        self._usuarios.append(usuario)

        # Sincronizar índice auxiliar
        self._indice_usuarios[clave] = usuario

        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        """Busca un usuario por su identificación.

        Semana 12: utiliza el diccionario _indice_usuarios para acceder
        directamente al usuario en O(1), eliminando el recorrido lineal
        de la lista completa que se realizaba en la Semana 11.
        """
        clave: str = identificacion.strip().lower()
        return self._indice_usuarios.get(clave)

    def listar_usuarios(self) -> list[Usuario]:
        """Retorna la lista principal de usuarios para recorrido, listado y persistencia."""
        return self._usuarios

    # ─────────────────────────────────────────────
    #  VENTAS
    # ─────────────────────────────────────────────

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        """Registra una venta relacionando un usuario con un producto.

        Valida que:
        - El usuario exista.
        - El producto exista.
        - La cantidad solicitada sea mayor que cero.
        - Exista stock suficiente.

        Si la venta es válida, crea un objeto Venta, lo agrega a la colección,
        y disminuye el stock del producto.

        Semana 12: las búsquedas del usuario y del producto son en O(1) gracias
        a los índices. Al registrar la venta, se sincroniza tanto la lista
        principal como el índice _ventas_por_usuario.
        """
        usuario: Usuario | None = self.buscar_usuario(identificacion_usuario)
        producto: Producto | None = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)

        # Agregar a la lista principal
        self._ventas.append(venta)

        # Sincronizar índice de ventas por usuario
        clave_usuario: str = usuario.identificacion.lower()
        if clave_usuario not in self._ventas_por_usuario:
            self._ventas_por_usuario[clave_usuario] = []
        self._ventas_por_usuario[clave_usuario].append(venta)

        producto.vender(cantidad)
        return True

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        """Retorna las ventas asociadas a un usuario específico.

        Semana 12: utiliza el diccionario _ventas_por_usuario para acceder
        directamente a la lista de ventas del usuario en O(1), eliminando
        el recorrido completo de la lista de ventas que se realizaba en la
        Semana 11 con un filtrado lineal.
        """
        clave: str = identificacion_usuario.strip().lower()
        return self._ventas_por_usuario.get(clave, [])

    def listar_ventas(self) -> list[Venta]:
        """Retorna la lista principal de ventas para recorrido, listado y persistencia."""
        return self._ventas

    # ─────────────────────────────────────────────
    #  UTILIDADES
    # ─────────────────────────────────────────────

    def obtener_categorias_unicas(self) -> set[str]:
        """Retorna el conjunto de categorías únicas registradas.

        Utiliza un set para garantizar valores únicos sin duplicados.
        """
        categorias: set[str] = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias

    def obtener_menu_diccionario(self) -> dict[str, str]:
        """Retorna un diccionario que mapea opciones numéricas a nombres de acción.

        Permite acceder a la acción correspondiente en O(1) sin utilizar
        cadenas de if-elif.
        """
        return {
            "1": "registrar_producto",
            "2": "buscar_producto",
            "3": "actualizar_producto",
            "4": "eliminar_producto",
            "5": "listar_productos",
            "6": "registrar_usuario",
            "7": "listar_usuarios",
            "8": "vender_producto",
            "9": "consultar_ventas_usuario",
            "10": "listar_ventas",
            "11": "mostrar_categorias",
            "12": "salir",
        }
