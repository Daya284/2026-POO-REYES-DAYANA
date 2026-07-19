"""
main.py — Punto de arranque del sistema de restaurante (Semana 8).

Responsabilidad única (SRP): este archivo se encarga exclusivamente
de la interacción por consola.  Solicita los datos, crea los objetos
y delega las operaciones al servicio Restaurante.
"""

import sys

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# ── Funciones de interacción ────────────────────────────────────


def mostrar_menu() -> None:
    """Muestra las opciones del menú principal del sistema."""
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("========================================")


def registrar_producto(servicio: Restaurante) -> None:
    """Solicita los datos de un producto y lo registra en el servicio."""
    print("\n--- Registrar Producto ---")
    codigo: str = input("  Codigo    : ")
    nombre: str = input("  Nombre    : ")
    categoria: str = input("  Categoria : ")
    precio_texto: str = input("  Precio    : ")

    try:
        precio: float = float(precio_texto)
        nuevo_producto: Producto = Producto(codigo, nombre, categoria, precio)
        servicio.registrar_producto(nuevo_producto)
    except ValueError as error:
        print(f"  [ERROR] {error}")


def registrar_bebida(servicio: Restaurante) -> None:
    """Solicita los datos de una bebida y la registra en el servicio.

    La bebida se almacena en la misma colección de productos gracias
    a la herencia (Bebida es un Producto).  Esto demuestra el
    principio abierto/cerrado: el servicio no necesitó modificarse.
    """
    print("\n--- Registrar Bebida ---")
    codigo: str = input("  Codigo      : ")
    nombre: str = input("  Nombre      : ")
    categoria: str = input("  Categoria   : ")
    precio_texto: str = input("  Precio      : ")
    tamanio: str = input("  Tamanio     : ")
    tipo_envase: str = input("  Tipo envase : ")

    try:
        precio: float = float(precio_texto)
        nueva_bebida: Bebida = Bebida(
            codigo, nombre, categoria, precio, tamanio, tipo_envase
        )
        servicio.registrar_producto(nueva_bebida)
    except ValueError as error:
        print(f"  [ERROR] {error}")


def registrar_cliente(servicio: Restaurante) -> None:
    """Solicita los datos de un cliente y lo registra en el servicio."""
    print("\n--- Registrar Cliente ---")
    identificacion: str = input("  ID     : ")
    nombre: str = input("  Nombre : ")
    correo: str = input("  Correo : ")

    try:
        nuevo_cliente: Cliente = Cliente(identificacion, nombre, correo)
        servicio.registrar_cliente(nuevo_cliente)
    except ValueError as error:
        print(f"  [ERROR] {error}")


# ── Función principal ───────────────────────────────────────────


def principal() -> None:
    """Ejecuta el bucle del menú interactivo del restaurante."""
    servicio: Restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion: str = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_producto(servicio)
        elif opcion == "2":
            registrar_bebida(servicio)
        elif opcion == "3":
            registrar_cliente(servicio)
        elif opcion == "4":
            servicio.listar_productos()
        elif opcion == "5":
            servicio.listar_clientes()
        elif opcion == "6":
            print("\n  Gracias por usar el sistema. Hasta luego.")
            sys.exit(0)
        else:
            print("  [!] Opcion no valida. Seleccione una opcion del 1 al 6.")


# ── Punto de arranque ───────────────────────────────────────────

if __name__ == "__main__":
    principal()
