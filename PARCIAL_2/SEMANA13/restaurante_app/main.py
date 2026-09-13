"""
Restaurante App - Punto de entrada principal
=============================================
Este archivo crea una única ventana principal de Tkinter, prepara los servicios
necesarios (carga de datos desde JSON y servicio del restaurante) y controla
el cambio entre la pantalla de acceso (LoginView) y la interfaz principal (MainView).

Flujo: main.py → LoginView → validación → MainView → cerrar sesión → LoginView
"""

import tkinter as tk
import os
import sys

# Asegurar que el directorio del proyecto esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:
    """
    Clase principal de la aplicación.
    Mantiene una única instancia de Tk() y controla el ciclo de vida
    de las vistas (login y principal).
    """

    def __init__(self):
        # Crear la ventana principal (única instancia de Tk)
        self.root = tk.Tk()
        self.root.title("Restaurante App - Sistema de Gestión")
        self.root.geometry("800x550")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(True, True)

        # Centrar la ventana en la pantalla
        self._centrar_ventana(800, 550)

        # Preparar los servicios: cargar datos desde los archivos JSON
        directorio_datos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos")
        ruta_usuarios = os.path.join(directorio_datos, "usuarios.json")
        ruta_productos = os.path.join(directorio_datos, "productos.json")

        datos_usuarios = ArchivoServicio.leer_json(ruta_usuarios)
        datos_productos = ArchivoServicio.leer_json(ruta_productos)

        # Crear el servicio del restaurante con los datos cargados
        self.servicio = RestauranteServicio(datos_usuarios, datos_productos)

        # Referencias a las vistas actuales
        self.login_view = None
        self.main_view = None

        # Mostrar la pantalla de login al iniciar
        self._mostrar_login()

    def _centrar_ventana(self, ancho, alto):
        """Centra la ventana en la pantalla."""
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _mostrar_login(self):
        """
        Muestra la vista de login.
        Si existe una vista principal activa, la oculta primero.
        """
        # Ocultar la vista principal si está visible
        if self.main_view:
            self.main_view.ocultar()
            self.main_view = None

        # Crear y mostrar la vista de login
        self.login_view = LoginView(self.root, self.servicio, self._al_iniciar_sesion)
        self.login_view.mostrar()

    def _al_iniciar_sesion(self, usuario):
        """
        Callback ejecutado cuando el login es exitoso.
        Oculta el login y muestra la vista principal con el usuario logueado.

        Args:
            usuario: Objeto Usuario que inició sesión correctamente.
        """
        # Ocultar la vista de login
        if self.login_view:
            self.login_view.ocultar()
            self.login_view = None

        # Crear y mostrar la vista principal
        self.main_view = MainView(self.root, self.servicio, self._mostrar_login)
        self.main_view.mostrar(usuario)

    def ejecutar(self):
        """Inicia el ciclo principal de la aplicación (mainloop)."""
        self.root.mainloop()


# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = RestauranteApp()
    app.ejecutar()
