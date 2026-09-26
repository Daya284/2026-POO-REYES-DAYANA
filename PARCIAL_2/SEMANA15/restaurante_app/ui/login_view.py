import tkinter as tk
from tkinter import messagebox
import os


class LoginView:
    """
    Vista de acceso (login) del sistema del restaurante.
    Presenta campos para usuario y contraseña, un botón de ingreso
    y mensajes de retroalimentación visual.
    Utiliza RestauranteServicio para validar las credenciales.

    Semana 15: se incorpora el logotipo del sistema desde la carpeta assets/
    para mejorar la experiencia visual del inicio de sesión.
    """

    def __init__(self, root, servicio, al_iniciar_sesion):
        """
        Inicializa la vista de login.

        Args:
            root: Ventana principal de Tkinter.
            servicio: Instancia de RestauranteServicio para validar acceso.
            al_iniciar_sesion: Función callback que se ejecuta al iniciar sesión correctamente.
        """
        self.root = root
        self.servicio = servicio
        self.al_iniciar_sesion = al_iniciar_sesion
        self.frame = None
        self.logo_imagen = None  # Referencia para evitar recolección de basura

    def mostrar(self):
        """Construye y muestra la vista de login en la ventana principal."""
        # Crear el frame principal del login
        self.frame = tk.Frame(self.root, bg="#2C3E50")
        self.frame.pack(fill="both", expand=True)

        # Contenedor central
        contenedor = tk.Frame(self.frame, bg="#34495E", padx=40, pady=40)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        # Logo del restaurante desde assets/
        self._cargar_logo(contenedor)

        # Título del restaurante
        tk.Label(
            contenedor,
            text="🍽️ Restaurante App",
            font=("Arial", 22, "bold"),
            fg="#E74C3C",
            bg="#34495E"
        ).pack(pady=(0, 5))

        # Subtítulo
        tk.Label(
            contenedor,
            text="Sistema de Gestión",
            font=("Arial", 12),
            fg="#BDC3C7",
            bg="#34495E"
        ).pack(pady=(0, 25))

        # Etiqueta de usuario
        tk.Label(
            contenedor,
            text="Usuario:",
            font=("Arial", 12),
            fg="#ECF0F1",
            bg="#34495E",
            anchor="w"
        ).pack(fill="x")

        # Campo de usuario
        self.entrada_usuario = tk.Entry(
            contenedor,
            font=("Arial", 12),
            width=28,
            bg="#ECF0F1",
            fg="#2C3E50",
            relief="flat",
            bd=2
        )
        self.entrada_usuario.pack(pady=(2, 15), ipady=5)

        # Etiqueta de contraseña
        tk.Label(
            contenedor,
            text="Contraseña:",
            font=("Arial", 12),
            fg="#ECF0F1",
            bg="#34495E",
            anchor="w"
        ).pack(fill="x")

        # Campo de contraseña
        self.entrada_contrasena = tk.Entry(
            contenedor,
            font=("Arial", 12),
            width=28,
            show="•",
            bg="#ECF0F1",
            fg="#2C3E50",
            relief="flat",
            bd=2
        )
        self.entrada_contrasena.pack(pady=(2, 20), ipady=5)

        # Etiqueta de mensaje (retroalimentación visual)
        self.etiqueta_mensaje = tk.Label(
            contenedor,
            text="",
            font=("Arial", 10),
            fg="#E74C3C",
            bg="#34495E"
        )
        self.etiqueta_mensaje.pack(pady=(0, 10))

        # Botón de ingreso
        tk.Button(
            contenedor,
            text="Iniciar Sesión",
            font=("Arial", 12, "bold"),
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=20,
            command=self._intentar_ingreso
        ).pack(pady=(0, 10), ipady=5)

        # Texto de ayuda
        tk.Label(
            contenedor,
            text="Usuarios de prueba: admin / cajero1 / mesero1 / cocinero1",
            font=("Arial", 8),
            fg="#7F8C8D",
            bg="#34495E"
        ).pack(pady=(10, 0))

        # Enfocar el campo de usuario al abrir
        self.entrada_usuario.focus_set()

        # Permitir presionar Enter para iniciar sesión
        self.root.bind("<Return>", lambda event: self._intentar_ingreso())

    def _cargar_logo(self, contenedor):
        """
        Carga el logotipo del restaurante desde la carpeta assets/.
        Si la imagen no se encuentra, se omite sin generar error.
        """
        try:
            ruta_assets = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "assets", "logo.png"
            )
            if os.path.exists(ruta_assets):
                imagen_original = tk.PhotoImage(file=ruta_assets)
                # Redimensionar la imagen para el login (reducir si es muy grande)
                ancho = imagen_original.width()
                alto = imagen_original.height()
                factor = max(1, max(ancho, alto) // 100)
                self.logo_imagen = imagen_original.subsample(factor, factor)

                tk.Label(
                    contenedor,
                    image=self.logo_imagen,
                    bg="#34495E"
                ).pack(pady=(0, 15))
        except Exception as e:
            print(f"No se pudo cargar el logo: {e}")

    def _intentar_ingreso(self):
        """
        Valida las credenciales ingresadas mediante RestauranteServicio.
        Si son correctas, ejecuta el callback de inicio de sesión.
        Si están vacías o son incorrectas, muestra un mensaje de error.
        """
        nombre_usuario = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get().strip()

        # Validar campos vacíos
        if not nombre_usuario or not contrasena:
            self.etiqueta_mensaje.config(
                text="⚠️ Por favor complete todos los campos.",
                fg="#F39C12"
            )
            return

        # Validar credenciales a través del servicio
        usuario = self.servicio.validar_acceso(nombre_usuario, contrasena)

        if usuario:
            self.etiqueta_mensaje.config(
                text=f"✅ Bienvenido/a, {usuario.nombre_completo}",
                fg="#2ECC71"
            )
            # Desenlazar la tecla Enter del login
            self.root.unbind("<Return>")
            # Ejecutar callback después de un breve retardo visual
            self.root.after(800, lambda: self.al_iniciar_sesion(usuario))
        else:
            self.etiqueta_mensaje.config(
                text="❌ Usuario o contraseña incorrectos.",
                fg="#E74C3C"
            )
            self.entrada_contrasena.delete(0, tk.END)

    def ocultar(self):
        """Oculta y destruye el frame del login."""
        if self.frame:
            self.frame.destroy()
            self.frame = None
