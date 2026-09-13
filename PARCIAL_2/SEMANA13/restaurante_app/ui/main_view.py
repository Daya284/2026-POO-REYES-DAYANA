import tkinter as tk
from tkinter import ttk, messagebox


class MainView:
    """
    Vista principal del sistema del restaurante.
    Se muestra después de un acceso correcto y permite visualizar:
    - Productos registrados (cargados desde productos.json).
    - Usuarios registrados (cargados desde usuarios.json).
    - Ventas (funcionalidad pendiente para futuras semanas).
    Solicita toda la información a RestauranteServicio.
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

        # ====== CONTENIDO PRINCIPAL ======
        contenido = tk.Frame(self.frame, bg="#2C3E50")
        contenido.pack(fill="both", expand=True, padx=20, pady=15)

        # ====== PANEL DE BOTONES DE NAVEGACIÓN ======
        panel_botones = tk.Frame(contenido, bg="#2C3E50")
        panel_botones.pack(fill="x", pady=(0, 15))

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
            command=self._mostrar_productos
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
            text="🧾 Ventas (Pendiente)",
            font=("Arial", 11, "bold"),
            bg="#7F8C8D",
            fg="white",
            activebackground="#707B7C",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            command=self._mostrar_ventas_pendiente
        ).pack(side="left", padx=(0, 10), ipady=8)

        # ====== ÁREA DE VISUALIZACIÓN ======
        self.area_contenido = tk.Frame(contenido, bg="#34495E", padx=15, pady=15)
        self.area_contenido.pack(fill="both", expand=True)

        # Mensaje de bienvenida inicial
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

        tk.Label(
            resumen,
            text="🧾 Ventas: Funcionalidad pendiente",
            font=("Arial", 12),
            fg="#95A5A6",
            bg="#34495E"
        ).pack(anchor="w", pady=3)

    def _limpiar_area_contenido(self):
        """Elimina todos los widgets del área de contenido."""
        for widget in self.area_contenido.winfo_children():
            widget.destroy()

    def _mostrar_productos(self):
        """
        Muestra los productos registrados en una tabla.
        Solicita los datos a RestauranteServicio.
        """
        self._limpiar_area_contenido()

        # Título de la sección
        tk.Label(
            self.area_contenido,
            text="📦 Productos Registrados",
            font=("Arial", 16, "bold"),
            fg="#2ECC71",
            bg="#34495E"
        ).pack(anchor="w", pady=(0, 15))

        # Crear tabla con Treeview
        columnas = ("ID", "Nombre", "Categoría", "Precio", "Cantidad")
        tabla = ttk.Treeview(
            self.area_contenido,
            columns=columnas,
            show="headings",
            height=10
        )

        # Configurar encabezados
        tabla.heading("ID", text="ID")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Categoría", text="Categoría")
        tabla.heading("Precio", text="Precio ($)")
        tabla.heading("Cantidad", text="Cantidad")

        # Configurar anchos de columnas
        tabla.column("ID", width=50, anchor="center")
        tabla.column("Nombre", width=180, anchor="w")
        tabla.column("Categoría", width=140, anchor="w")
        tabla.column("Precio", width=100, anchor="center")
        tabla.column("Cantidad", width=80, anchor="center")

        # Insertar datos desde el servicio
        productos = self.servicio.obtener_productos()
        for producto in productos:
            tabla.insert("", "end", values=(
                producto.id,
                producto.nombre,
                producto.categoria,
                f"${producto.precio:.2f}",
                producto.cantidad
            ))

        tabla.pack(fill="both", expand=True)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(self.area_contenido, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Información de cantidad total
        tk.Label(
            self.area_contenido,
            text=f"Total de productos: {self.servicio.obtener_cantidad_productos()}",
            font=("Arial", 10),
            fg="#BDC3C7",
            bg="#34495E"
        ).pack(anchor="w", pady=(10, 0))

    def _mostrar_usuarios(self):
        """
        Muestra los usuarios registrados en una tabla.
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
        ).pack(anchor="w", pady=(0, 15))

        # Crear tabla con Treeview
        columnas = ("ID", "Usuario", "Nombre Completo", "Rol")
        tabla = ttk.Treeview(
            self.area_contenido,
            columns=columnas,
            show="headings",
            height=10
        )

        # Configurar encabezados
        tabla.heading("ID", text="ID")
        tabla.heading("Usuario", text="Usuario")
        tabla.heading("Nombre Completo", text="Nombre Completo")
        tabla.heading("Rol", text="Rol")

        # Configurar anchos de columnas
        tabla.column("ID", width=50, anchor="center")
        tabla.column("Usuario", width=120, anchor="w")
        tabla.column("Nombre Completo", width=200, anchor="w")
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

        tabla.pack(fill="both", expand=True)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(self.area_contenido, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Información de cantidad total
        tk.Label(
            self.area_contenido,
            text=f"Total de usuarios: {self.servicio.obtener_cantidad_usuarios()}",
            font=("Arial", 10),
            fg="#BDC3C7",
            bg="#34495E"
        ).pack(anchor="w", pady=(10, 0))

    def _mostrar_ventas_pendiente(self):
        """
        Muestra un mensaje indicando que la funcionalidad de Ventas
        se encuentra pendiente de desarrollo en futuras semanas.
        """
        self._limpiar_area_contenido()

        tk.Label(
            self.area_contenido,
            text="🧾 Módulo de Ventas",
            font=("Arial", 16, "bold"),
            fg="#F39C12",
            bg="#34495E"
        ).pack(pady=(40, 15))

        tk.Label(
            self.area_contenido,
            text="Esta funcionalidad se encuentra pendiente de desarrollo.",
            font=("Arial", 12),
            fg="#BDC3C7",
            bg="#34495E"
        ).pack(pady=(0, 5))

        tk.Label(
            self.area_contenido,
            text="Se implementará en las próximas semanas del curso.",
            font=("Arial", 11),
            fg="#95A5A6",
            bg="#34495E"
        ).pack(pady=(0, 10))

    def _cerrar_sesion(self):
        """Cierra la sesión actual y regresa a la pantalla de login."""
        self.usuario_actual = None
        self.al_cerrar_sesion()

    def ocultar(self):
        """Oculta y destruye el frame de la vista principal."""
        if self.frame:
            self.frame.destroy()
            self.frame = None
