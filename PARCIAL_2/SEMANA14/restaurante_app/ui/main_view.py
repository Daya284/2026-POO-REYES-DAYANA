import tkinter as tk
from tkinter import ttk, messagebox


class MainView:
    """
    Vista principal del sistema del restaurante.
    Se muestra después de un acceso correcto y permite:
    - Consultar usuarios registrados.
    - Gestionar productos mediante operaciones CRUD (Registrar, Consultar,
      Actualizar, Eliminar) utilizando componentes y contenedores de Tkinter.

    Semana 14: la interfaz evoluciona con contenedores organizados (LabelFrame),
    formularios con Entry, Combobox, Spinbox, botones con command=, y un Treeview
    para la visualización de datos. Las operaciones se delegan a RestauranteServicio.
    """

    def __init__(self, root, servicio, al_cerrar_sesion):
        """
        Inicializa la vista principal.

        Args:
            root: Ventana principal de Tkinter.
            servicio: Instancia de RestauranteServicio para obtener datos.
            al_cerrar_sesion: Función callback que se ejecuta al cerrar sesión.
        """
        self.root = root
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion
        self.frame = None
        self.usuario_actual = None

        # Variables de los campos del formulario de productos
        self.var_id = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_categoria = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_cantidad = tk.StringVar()

        # Referencia a la tabla de productos
        self.tabla_productos = None

        # Etiqueta de estado para retroalimentación
        self.etiqueta_estado = None

    def mostrar(self, usuario):
        """
        Construye y muestra la vista principal con la información del usuario logueado.

        Args:
            usuario: Objeto Usuario que inició sesión.
        """
        self.usuario_actual = usuario

        # Frame principal
        self.frame = tk.Frame(self.root, bg="#2C3E50")
        self.frame.pack(fill="both", expand=True)

        # ====== BARRA SUPERIOR ======
        self._crear_barra_superior(usuario)

        # ====== CONTENIDO PRINCIPAL ======
        contenido = tk.Frame(self.frame, bg="#2C3E50")
        contenido.pack(fill="both", expand=True, padx=15, pady=10)

        # ====== PANEL DE NAVEGACIÓN ======
        self._crear_panel_navegacion(contenido)

        # ====== ÁREA DE CONTENIDO DINÁMICO ======
        self.area_contenido = tk.Frame(contenido, bg="#34495E", padx=15, pady=15)
        self.area_contenido.pack(fill="both", expand=True)

        # Mostrar mensaje de bienvenida inicial
        self._mostrar_bienvenida(usuario)

    # ================================================================
    # Construcción de la barra superior
    # ================================================================

    def _crear_barra_superior(self, usuario):
        """Crea la barra superior con título, info del usuario y botón de cerrar sesión."""
        barra_superior = tk.Frame(self.frame, bg="#E74C3C", height=60)
        barra_superior.pack(fill="x")
        barra_superior.pack_propagate(False)

        tk.Label(
            barra_superior,
            text="🍽️ Restaurante App",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#E74C3C"
        ).pack(side="left", padx=20)

        # Información del usuario logueado
        tk.Label(
            barra_superior,
            text=f"👤 {usuario.nombre_completo} ({usuario.rol})",
            font=("Arial", 10),
            fg="white",
            bg="#E74C3C"
        ).pack(side="right", padx=(0, 10))

        # Botón de cerrar sesión
        tk.Button(
            barra_superior,
            text="Cerrar Sesión",
            font=("Arial", 9, "bold"),
            bg="#C0392B",
            fg="white",
            activebackground="#A93226",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self._cerrar_sesion
        ).pack(side="right", padx=10, pady=15)

    # ================================================================
    # Panel de navegación
    # ================================================================

    def _crear_panel_navegacion(self, contenedor_padre):
        """Crea el panel de botones de navegación entre secciones."""
        panel_botones = tk.Frame(contenedor_padre, bg="#2C3E50")
        panel_botones.pack(fill="x", pady=(0, 10))

        tk.Button(
            panel_botones,
            text="📦 Productos",
            font=("Arial", 11, "bold"),
            bg="#27AE60",
            fg="white",
            activebackground="#1E8449",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            command=self._mostrar_seccion_productos
        ).pack(side="left", padx=(0, 10), ipady=8)

        tk.Button(
            panel_botones,
            text="👥 Usuarios",
            font=("Arial", 11, "bold"),
            bg="#2980B9",
            fg="white",
            activebackground="#1F618D",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            command=self._mostrar_usuarios
        ).pack(side="left", padx=(0, 10), ipady=8)

        tk.Button(
            panel_botones,
            text="🏠 Inicio",
            font=("Arial", 11, "bold"),
            bg="#8E44AD",
            fg="white",
            activebackground="#6C3483",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            command=lambda: self._mostrar_bienvenida(self.usuario_actual)
        ).pack(side="left", padx=(0, 10), ipady=8)

    # ================================================================
    # Pantalla de bienvenida
    # ================================================================

    def _mostrar_bienvenida(self, usuario):
        """Muestra el mensaje de bienvenida con resumen de datos."""
        self._limpiar_area_contenido()

        tk.Label(
            self.area_contenido,
            text=f"Bienvenido/a al sistema, {usuario.nombre_completo}",
            font=("Arial", 16, "bold"),
            fg="#ECF0F1",
            bg="#34495E"
        ).pack(pady=(20, 10))

        tk.Label(
            self.area_contenido,
            text="Seleccione una opción del menú para comenzar.",
            font=("Arial", 12),
            fg="#BDC3C7",
            bg="#34495E"
        ).pack(pady=(0, 10))

        # Resumen de datos cargados
        resumen = tk.Frame(self.area_contenido, bg="#34495E")
        resumen.pack(pady=20)

        cantidad_productos = self.servicio.obtener_cantidad_productos()
        cantidad_usuarios = self.servicio.obtener_cantidad_usuarios()

        tk.Label(
            resumen,
            text=f"📦 Productos registrados: {cantidad_productos}",
            font=("Arial", 12),
            fg="#2ECC71",
            bg="#34495E"
        ).pack(anchor="w", pady=3)

        tk.Label(
            resumen,
            text=f"👥 Usuarios registrados: {cantidad_usuarios}",
            font=("Arial", 12),
            fg="#3498DB",
            bg="#34495E"
        ).pack(anchor="w", pady=3)

    # ================================================================
    # Sección de PRODUCTOS (Semana 14 - Componentes y contenedores)
    # ================================================================

    def _mostrar_seccion_productos(self):
        """
        Muestra la sección completa de gestión de productos.
        Organiza la interfaz en contenedores:
        - LabelFrame superior: Formulario de datos del producto.
        - Frame de acciones: Botones CRUD con command=.
        - LabelFrame inferior: Tabla Treeview con los productos.
        - Barra de estado: Retroalimentación de las operaciones.
        """
        self._limpiar_area_contenido()

        # Título de la sección
        tk.Label(
            self.area_contenido,
            text="📦 Gestión de Productos",
            font=("Arial", 16, "bold"),
            fg="#2ECC71",
            bg="#34495E"
        ).pack(anchor="w", pady=(0, 10))

        # ---- CONTENEDOR DEL FORMULARIO (LabelFrame) ----
        frame_formulario = tk.LabelFrame(
            self.area_contenido,
            text=" Datos del Producto ",
            font=("Arial", 11, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50",
            padx=15,
            pady=10
        )
        frame_formulario.pack(fill="x", pady=(0, 10))

        # Organización del formulario usando grid dentro del LabelFrame
        # Fila 0: ID y Nombre
        tk.Label(
            frame_formulario, text="ID:", font=("Arial", 10, "bold"),
            fg="#ECF0F1", bg="#2C3E50"
        ).grid(row=0, column=0, sticky="w", padx=(0, 5), pady=4)

        entrada_id = tk.Entry(
            frame_formulario, textvariable=self.var_id,
            font=("Arial", 10), width=8, bg="#ECF0F1", fg="#2C3E50",
            relief="flat", bd=2
        )
        entrada_id.grid(row=0, column=1, sticky="w", padx=(0, 20), pady=4, ipady=3)

        tk.Label(
            frame_formulario, text="Nombre:", font=("Arial", 10, "bold"),
            fg="#ECF0F1", bg="#2C3E50"
        ).grid(row=0, column=2, sticky="w", padx=(0, 5), pady=4)

        tk.Entry(
            frame_formulario, textvariable=self.var_nombre,
            font=("Arial", 10), width=25, bg="#ECF0F1", fg="#2C3E50",
            relief="flat", bd=2
        ).grid(row=0, column=3, sticky="w", padx=(0, 20), pady=4, ipady=3)

        # Fila 1: Categoría y Precio
        tk.Label(
            frame_formulario, text="Categoría:", font=("Arial", 10, "bold"),
            fg="#ECF0F1", bg="#2C3E50"
        ).grid(row=1, column=0, sticky="w", padx=(0, 5), pady=4)

        # Combobox para categorías predefinidas
        categorias = [
            "Comida rápida", "Pizzas", "Ensaladas", "Bebidas",
            "Platos fuertes", "Acompañamientos", "Postres", "Sopas"
        ]
        combo_categoria = ttk.Combobox(
            frame_formulario, textvariable=self.var_categoria,
            values=categorias, font=("Arial", 10), width=16, state="normal"
        )
        combo_categoria.grid(row=1, column=1, sticky="w", padx=(0, 20), pady=4, ipady=3)

        tk.Label(
            frame_formulario, text="Precio ($):", font=("Arial", 10, "bold"),
            fg="#ECF0F1", bg="#2C3E50"
        ).grid(row=1, column=2, sticky="w", padx=(0, 5), pady=4)

        tk.Entry(
            frame_formulario, textvariable=self.var_precio,
            font=("Arial", 10), width=10, bg="#ECF0F1", fg="#2C3E50",
            relief="flat", bd=2
        ).grid(row=1, column=3, sticky="w", padx=(0, 20), pady=4, ipady=3)

        # Fila 2: Cantidad
        tk.Label(
            frame_formulario, text="Cantidad:", font=("Arial", 10, "bold"),
            fg="#ECF0F1", bg="#2C3E50"
        ).grid(row=2, column=0, sticky="w", padx=(0, 5), pady=4)

        spinbox_cantidad = tk.Spinbox(
            frame_formulario, textvariable=self.var_cantidad,
            from_=0, to=999, font=("Arial", 10), width=8,
            bg="#ECF0F1", fg="#2C3E50", relief="flat", bd=2
        )
        spinbox_cantidad.grid(row=2, column=1, sticky="w", padx=(0, 20), pady=4, ipady=3)

        # ---- CONTENEDOR DE ACCIONES (botones CRUD) ----
        frame_acciones = tk.Frame(self.area_contenido, bg="#34495E")
        frame_acciones.pack(fill="x", pady=(0, 10))

        # Botón Registrar
        tk.Button(
            frame_acciones,
            text="➕ Registrar",
            font=("Arial", 10, "bold"),
            bg="#27AE60", fg="white",
            activebackground="#1E8449", activeforeground="white",
            relief="flat", cursor="hand2", width=14,
            command=self._registrar_producto
        ).pack(side="left", padx=(0, 8), ipady=5)

        # Botón Consultar / Cargar
        tk.Button(
            frame_acciones,
            text="🔍 Consultar",
            font=("Arial", 10, "bold"),
            bg="#2980B9", fg="white",
            activebackground="#1F618D", activeforeground="white",
            relief="flat", cursor="hand2", width=14,
            command=self._consultar_producto
        ).pack(side="left", padx=(0, 8), ipady=5)

        # Botón Actualizar
        tk.Button(
            frame_acciones,
            text="✏️ Actualizar",
            font=("Arial", 10, "bold"),
            bg="#F39C12", fg="white",
            activebackground="#D68910", activeforeground="white",
            relief="flat", cursor="hand2", width=14,
            command=self._actualizar_producto
        ).pack(side="left", padx=(0, 8), ipady=5)

        # Botón Eliminar
        tk.Button(
            frame_acciones,
            text="🗑️ Eliminar",
            font=("Arial", 10, "bold"),
            bg="#E74C3C", fg="white",
            activebackground="#C0392B", activeforeground="white",
            relief="flat", cursor="hand2", width=14,
            command=self._eliminar_producto
        ).pack(side="left", padx=(0, 8), ipady=5)

        # Botón Limpiar formulario
        tk.Button(
            frame_acciones,
            text="🧹 Limpiar",
            font=("Arial", 10, "bold"),
            bg="#7F8C8D", fg="white",
            activebackground="#616A6B", activeforeground="white",
            relief="flat", cursor="hand2", width=14,
            command=self._limpiar_formulario
        ).pack(side="left", padx=(0, 8), ipady=5)

        # ---- CONTENEDOR DE LA TABLA (LabelFrame) ----
        frame_tabla = tk.LabelFrame(
            self.area_contenido,
            text=" Productos Registrados ",
            font=("Arial", 11, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50",
            padx=10,
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True, pady=(0, 5))

        # Crear tabla con Treeview
        columnas = ("ID", "Nombre", "Categoría", "Precio", "Cantidad")

        # Estilo personalizado para la tabla
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview",
                         background="#34495E",
                         foreground="#ECF0F1",
                         fieldbackground="#34495E",
                         font=("Arial", 10),
                         rowheight=28)
        estilo.configure("Treeview.Heading",
                         background="#1ABC9C",
                         foreground="white",
                         font=("Arial", 10, "bold"))
        estilo.map("Treeview",
                    background=[("selected", "#1ABC9C")],
                    foreground=[("selected", "white")])

        self.tabla_productos = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=8,
            selectmode="browse"
        )

        # Configurar encabezados
        self.tabla_productos.heading("ID", text="ID")
        self.tabla_productos.heading("Nombre", text="Nombre")
        self.tabla_productos.heading("Categoría", text="Categoría")
        self.tabla_productos.heading("Precio", text="Precio ($)")
        self.tabla_productos.heading("Cantidad", text="Cantidad")

        # Configurar anchos de columnas
        self.tabla_productos.column("ID", width=50, anchor="center")
        self.tabla_productos.column("Nombre", width=200, anchor="w")
        self.tabla_productos.column("Categoría", width=140, anchor="w")
        self.tabla_productos.column("Precio", width=100, anchor="center")
        self.tabla_productos.column("Cantidad", width=80, anchor="center")

        # Scrollbar vertical para la tabla
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical",
                                   command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscrollcommand=scrollbar.set)

        self.tabla_productos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Cargar los datos iniciales en la tabla
        self._actualizar_tabla_productos()

        # ---- BARRA DE ESTADO ----
        frame_estado = tk.Frame(self.area_contenido, bg="#2C3E50", pady=5)
        frame_estado.pack(fill="x")

        self.etiqueta_estado = tk.Label(
            frame_estado,
            text=f"Total de productos: {self.servicio.obtener_cantidad_productos()}",
            font=("Arial", 10),
            fg="#BDC3C7",
            bg="#2C3E50"
        )
        self.etiqueta_estado.pack(side="left")

    # ================================================================
    # Operaciones CRUD delegadas al servicio
    # ================================================================

    def _registrar_producto(self):
        """
        Registra un nuevo producto delegando la operación a RestauranteServicio.
        Toma los datos del formulario (ignora el ID, se genera automáticamente).
        """
        nombre = self.var_nombre.get()
        categoria = self.var_categoria.get()
        precio = self.var_precio.get()
        cantidad = self.var_cantidad.get()

        exito, mensaje = self.servicio.registrar_producto(
            nombre, categoria, precio, cantidad
        )

        if exito:
            self._actualizar_tabla_productos()
            self._limpiar_formulario()
            self._mostrar_estado(mensaje, "#2ECC71")
            messagebox.showinfo("Registro exitoso", mensaje)
        else:
            self._mostrar_estado(mensaje, "#E74C3C")
            messagebox.showwarning("Error de validación", mensaje)

    def _consultar_producto(self):
        """
        Consulta un producto por ID y carga sus datos en el formulario.
        Permite al usuario ver la información de un producto existente.
        """
        id_texto = self.var_id.get().strip()

        if not id_texto:
            messagebox.showwarning(
                "ID requerido",
                "Ingrese el ID del producto que desea consultar."
            )
            return

        try:
            id_producto = int(id_texto)
        except ValueError:
            messagebox.showwarning(
                "ID inválido",
                "El ID debe ser un número entero."
            )
            return

        producto = self.servicio.buscar_producto_por_id(id_producto)

        if producto:
            # Cargar los datos del producto en el formulario
            self.var_nombre.set(producto.nombre)
            self.var_categoria.set(producto.categoria)
            self.var_precio.set(str(producto.precio))
            self.var_cantidad.set(str(producto.cantidad))
            self._mostrar_estado(
                f"Producto '{producto.nombre}' (ID {producto.id}) cargado en el formulario.",
                "#3498DB"
            )
        else:
            self._mostrar_estado(
                f"No se encontró un producto con ID {id_producto}.",
                "#E74C3C"
            )
            messagebox.showinfo(
                "Producto no encontrado",
                f"No existe un producto con ID {id_producto}."
            )

    def _actualizar_producto(self):
        """
        Actualiza un producto existente delegando la operación a RestauranteServicio.
        Toma el ID y los datos del formulario.
        """
        id_texto = self.var_id.get().strip()

        if not id_texto:
            messagebox.showwarning(
                "ID requerido",
                "Ingrese el ID del producto que desea actualizar."
            )
            return

        try:
            id_producto = int(id_texto)
        except ValueError:
            messagebox.showwarning(
                "ID inválido",
                "El ID debe ser un número entero."
            )
            return

        nombre = self.var_nombre.get()
        categoria = self.var_categoria.get()
        precio = self.var_precio.get()
        cantidad = self.var_cantidad.get()

        exito, mensaje = self.servicio.actualizar_producto(
            id_producto, nombre, categoria, precio, cantidad
        )

        if exito:
            self._actualizar_tabla_productos()
            self._mostrar_estado(mensaje, "#F39C12")
            messagebox.showinfo("Actualización exitosa", mensaje)
        else:
            self._mostrar_estado(mensaje, "#E74C3C")
            messagebox.showwarning("Error de validación", mensaje)

    def _eliminar_producto(self):
        """
        Elimina un producto por ID delegando la operación a RestauranteServicio.
        Solicita confirmación antes de eliminar.
        """
        id_texto = self.var_id.get().strip()

        if not id_texto:
            messagebox.showwarning(
                "ID requerido",
                "Ingrese el ID del producto que desea eliminar."
            )
            return

        try:
            id_producto = int(id_texto)
        except ValueError:
            messagebox.showwarning(
                "ID inválido",
                "El ID debe ser un número entero."
            )
            return

        # Verificar que el producto existe antes de confirmar
        producto = self.servicio.buscar_producto_por_id(id_producto)
        if not producto:
            self._mostrar_estado(
                f"No se encontró un producto con ID {id_producto}.",
                "#E74C3C"
            )
            messagebox.showinfo(
                "Producto no encontrado",
                f"No existe un producto con ID {id_producto}."
            )
            return

        # Confirmar eliminación
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el producto '{producto.nombre}' (ID {id_producto})?"
        )

        if confirmacion:
            exito, mensaje = self.servicio.eliminar_producto(id_producto)
            if exito:
                self._actualizar_tabla_productos()
                self._limpiar_formulario()
                self._mostrar_estado(mensaje, "#E74C3C")
                messagebox.showinfo("Eliminación exitosa", mensaje)
            else:
                self._mostrar_estado(mensaje, "#E74C3C")
                messagebox.showwarning("Error", mensaje)

    # ================================================================
    # Métodos auxiliares de la sección de productos
    # ================================================================

    def _actualizar_tabla_productos(self):
        """
        Actualiza la tabla Treeview con los datos actuales del servicio.
        Limpia las filas existentes y las recarga desde RestauranteServicio.
        """
        if not self.tabla_productos:
            return

        # Limpiar todas las filas de la tabla
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        # Insertar los datos actualizados
        productos = self.servicio.obtener_productos()
        for producto in productos:
            self.tabla_productos.insert("", "end", values=(
                producto.id,
                producto.nombre,
                producto.categoria,
                f"${producto.precio:.2f}",
                producto.cantidad
            ))

        # Actualizar el contador en la barra de estado
        if self.etiqueta_estado:
            self.etiqueta_estado.config(
                text=f"Total de productos: {self.servicio.obtener_cantidad_productos()}"
            )

    def _limpiar_formulario(self):
        """Limpia todos los campos del formulario de productos."""
        self.var_id.set("")
        self.var_nombre.set("")
        self.var_categoria.set("")
        self.var_precio.set("")
        self.var_cantidad.set("")

    def _mostrar_estado(self, mensaje, color="#BDC3C7"):
        """
        Actualiza el mensaje de la barra de estado.

        Args:
            mensaje: Texto a mostrar.
            color: Color del texto (por defecto gris claro).
        """
        if self.etiqueta_estado:
            self.etiqueta_estado.config(text=mensaje, fg=color)

    # ================================================================
    # Sección de USUARIOS
    # ================================================================

    def _mostrar_usuarios(self):
        """
        Muestra los usuarios registrados en una tabla Treeview.
        Solicita los datos a RestauranteServicio.
        """
        self._limpiar_area_contenido()

        # Título de la sección
        tk.Label(
            self.area_contenido,
            text="👥 Usuarios Registrados",
            font=("Arial", 16, "bold"),
            fg="#3498DB",
            bg="#34495E"
        ).pack(anchor="w", pady=(0, 10))

        # Contenedor de la tabla de usuarios (LabelFrame)
        frame_tabla = tk.LabelFrame(
            self.area_contenido,
            text=" Información de Usuarios ",
            font=("Arial", 11, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50",
            padx=10,
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True, pady=(0, 10))

        # Crear tabla con Treeview
        columnas = ("ID", "Usuario", "Nombre Completo", "Rol")
        tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=10,
            selectmode="browse"
        )

        # Configurar encabezados
        tabla.heading("ID", text="ID")
        tabla.heading("Usuario", text="Usuario")
        tabla.heading("Nombre Completo", text="Nombre Completo")
        tabla.heading("Rol", text="Rol")

        # Configurar anchos de columnas
        tabla.column("ID", width=50, anchor="center")
        tabla.column("Usuario", width=120, anchor="w")
        tabla.column("Nombre Completo", width=220, anchor="w")
        tabla.column("Rol", width=120, anchor="center")

        # Insertar datos desde el servicio
        usuarios = self.servicio.obtener_usuarios()
        for usuario in usuarios:
            tabla.insert("", "end", values=(
                usuario.id,
                usuario.nombre_usuario,
                usuario.nombre_completo,
                usuario.rol.capitalize()
            ))

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)

        tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Información de cantidad total
        tk.Label(
            self.area_contenido,
            text=f"Total de usuarios: {self.servicio.obtener_cantidad_usuarios()}",
            font=("Arial", 10),
            fg="#BDC3C7",
            bg="#34495E"
        ).pack(anchor="w", pady=(5, 0))

    # ================================================================
    # Métodos generales
    # ================================================================

    def _limpiar_area_contenido(self):
        """Elimina todos los widgets del área de contenido."""
        for widget in self.area_contenido.winfo_children():
            widget.destroy()
        # Resetear referencias a componentes de la sección de productos
        self.tabla_productos = None
        self.etiqueta_estado = None

    def _cerrar_sesion(self):
        """Cierra la sesión actual y regresa a la pantalla de login."""
        self.usuario_actual = None
        self.al_cerrar_sesion()

    def ocultar(self):
        """Oculta y destruye el frame de la vista principal."""
        if self.frame:
            self.frame.destroy()
            self.frame = None
