import os
import sys

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

# Rutas relativas a los archivos JSON
RUTA_DATOS: str = os.path.join(os.path.dirname(__file__), "datos")
RUTA_PRODUCTOS: str = os.path.join(RUTA_DATOS, "productos.json")
RUTA_USUARIOS: str = os.path.join(RUTA_DATOS, "usuarios.json")
RUTA_VENTAS: str = os.path.join(RUTA_DATOS, "ventas.json")


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Vender producto")
    print("9. Consultar ventas de un usuario")
    print("10. Listar todas las ventas")
    print("----------------------------------------")
    print("11. Mostrar categorías")
    print("12. Salir")
    print("========================================")


# ─────────────────────────────────────────────
#  OPERACIONES DE PRODUCTOS
# ─────────────────────────────────────────────

def registrar_producto(servicio: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Registrar Producto ---")
    codigo: str = input("  Codigo    : ")
    nombre: str = input("  Nombre    : ")
    categoria: str = input("  Categoria : ")
    precio_texto: str = input("  Precio    : ")
    stock_texto: str = input("  Stock     : ")

    try:
        precio: float = float(precio_texto)
        stock: int = int(stock_texto)
        producto = Producto(codigo, nombre, categoria, precio, stock)
        if servicio.registrar_producto(producto):
            archivo_servicio.guardar_productos(servicio.listar_productos())
            print("  [OK] Producto registrado correctamente.")
        else:
            print(f"  [!] Ya existe un producto con el codigo '{codigo}'.")
    except ValueError as error:
        print(f"  [ERROR] {error}")


def buscar_producto(servicio: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo: str = input("  Codigo : ")
    producto: Producto | None = servicio.buscar_producto(codigo)
    if producto is None:
        print("  [!] No se encontró un producto con ese código.")
        return
    print("\n" + producto.mostrar_informacion())


def actualizar_producto(servicio: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Actualizar Producto ---")
    codigo: str = input("  Codigo actual : ")
    producto: Producto | None = servicio.buscar_producto(codigo)
    if producto is None:
        print("  [!] No se encontró el producto a actualizar.")
        return

    print("Deje en blanco los campos que no desea modificar.")
    nombre: str | None = input(f"  Nuevo nombre [{producto.nombre}] : ") or None
    categoria: str | None = input(f"  Nueva categoria [{producto.categoria}] : ") or None
    precio_texto: str = input(f"  Nuevo precio [{producto.precio}] : ")
    precio: float | None = float(precio_texto) if precio_texto.strip() else None
    stock_texto: str = input(f"  Nuevo stock [{producto.stock}] : ")
    stock: int | None = int(stock_texto) if stock_texto.strip() else None

    try:
        actualizado: bool = servicio.actualizar_producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock,
        )
        if actualizado:
            archivo_servicio.guardar_productos(servicio.listar_productos())
            print("  [OK] Producto actualizado correctamente.")
        else:
            print("  [!] No fue posible actualizar el producto.")
    except ValueError as error:
        print(f"  [ERROR] {error}")


def eliminar_producto(servicio: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Eliminar Producto ---")
    codigo: str = input("  Codigo : ")
    if servicio.eliminar_producto(codigo):
        archivo_servicio.guardar_productos(servicio.listar_productos())
        print("  [OK] Producto eliminado correctamente.")
    else:
        print("  [!] No se encontró un producto con ese código.")


def listar_productos(servicio: Restaurante) -> None:
    productos: list[Producto] = servicio.listar_productos()
    if not productos:
        print("  No hay productos registrados en el restaurante.")
        return

    print("\n+======================================+")
    print("|       PRODUCTOS REGISTRADOS          |")
    print("+======================================+")
    for indice, producto in enumerate(productos, start=1):
        print(f"\n  -- {indice}. --")
        print(producto.mostrar_informacion())


# ─────────────────────────────────────────────
#  OPERACIONES DE USUARIOS
# ─────────────────────────────────────────────

def registrar_usuario(servicio: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion: str = input("  Identificacion : ")
    nombre: str = input("  Nombre         : ")
    correo: str = input("  Correo         : ")

    try:
        usuario = Usuario(identificacion, nombre, correo)
        if servicio.registrar_usuario(usuario):
            archivo_servicio.guardar_usuarios(servicio.listar_usuarios())
            print("  [OK] Usuario registrado correctamente.")
        else:
            print(f"  [!] Ya existe un usuario con la identificacion '{identificacion}'.")
    except ValueError as error:
        print(f"  [ERROR] {error}")


def listar_usuarios(servicio: Restaurante) -> None:
    usuarios: list[Usuario] = servicio.listar_usuarios()
    if not usuarios:
        print("  No hay usuarios registrados en el sistema.")
        return

    print("\n+======================================+")
    print("|         USUARIOS REGISTRADOS         |")
    print("+======================================+")
    for indice, usuario in enumerate(usuarios, start=1):
        print(f"\n  -- {indice}. --")
        print(usuario.mostrar_informacion())


# ─────────────────────────────────────────────
#  OPERACIONES DE VENTAS
# ─────────────────────────────────────────────

def vender_producto(servicio: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Vender Producto ---")
    identificacion_usuario: str = input("  Identificacion del usuario : ")
    codigo_producto: str = input("  Codigo del producto        : ")
    cantidad_texto: str = input("  Cantidad                   : ")

    try:
        cantidad: int = int(cantidad_texto)
    except ValueError:
        print("  [ERROR] La cantidad debe ser un numero entero valido.")
        return

    # Mostrar información previa a la venta
    producto: Producto | None = servicio.buscar_producto(codigo_producto)
    if producto is not None:
        print(f"\n  Producto: {producto.nombre}")
        print(f"  Stock actual: {producto.stock}")
        print(f"  Cantidad solicitada: {cantidad}")

    resultado: bool = servicio.vender_producto(codigo_producto, identificacion_usuario, cantidad)

    if resultado:
        archivo_servicio.guardar_ventas(servicio.listar_ventas())
        archivo_servicio.guardar_productos(servicio.listar_productos())
        print(f"\n  [OK] Venta registrada correctamente.")
        print(f"  Stock actualizado: {producto.stock}")
    else:
        usuario = servicio.buscar_usuario(identificacion_usuario)
        if usuario is None:
            print("  [!] No se encontró un usuario con esa identificación.")
        elif producto is None:
            print("  [!] No se encontró un producto con ese código.")
        elif cantidad <= 0:
            print("  [!] La cantidad debe ser mayor a cero.")
        else:
            print(f"  [!] Stock insuficiente. Disponible: {producto.stock}, solicitado: {cantidad}.")


def consultar_ventas_usuario(servicio: Restaurante) -> None:
    print("\n--- Consultar Ventas de un Usuario ---")
    identificacion: str = input("  Identificacion del usuario : ")

    usuario: Usuario | None = servicio.buscar_usuario(identificacion)
    if usuario is None:
        print("  [!] No se encontró un usuario con esa identificación.")
        return

    ventas: list[Venta] = servicio.consultar_ventas_por_usuario(identificacion)
    if not ventas:
        print(f"  El usuario '{usuario.nombre}' no tiene ventas registradas.")
        return

    print(f"\n+======================================+")
    print(f"|  VENTAS DE: {usuario.nombre.upper():<24s}|")
    print(f"+======================================+")
    for indice, venta in enumerate(ventas, start=1):
        producto: Producto | None = servicio.buscar_producto(venta.producto_codigo)
        nombre_producto: str = producto.nombre if producto else "Producto no encontrado"
        print(f"\n  -- Venta {indice} --")
        print(f"  Producto : {nombre_producto} ({venta.producto_codigo})")
        print(f"  Cantidad : {venta.cantidad}")


def listar_ventas(servicio: Restaurante) -> None:
    ventas: list[Venta] = servicio.listar_ventas()
    if not ventas:
        print("  No hay ventas registradas en el sistema.")
        return

    print("\n+======================================+")
    print("|         VENTAS REGISTRADAS           |")
    print("+======================================+")
    for indice, venta in enumerate(ventas, start=1):
        producto: Producto | None = servicio.buscar_producto(venta.producto_codigo)
        nombre_producto: str = producto.nombre if producto else "Producto no encontrado"
        usuario: Usuario | None = servicio.buscar_usuario(venta.usuario_id)
        nombre_usuario: str = usuario.nombre if usuario else "Usuario no encontrado"
        print(f"\n  -- Venta {indice} --")
        print(f"  Usuario  : {nombre_usuario} ({venta.usuario_id})")
        print(f"  Producto : {nombre_producto} ({venta.producto_codigo})")
        print(f"  Cantidad : {venta.cantidad}")


# ─────────────────────────────────────────────
#  UTILIDADES
# ─────────────────────────────────────────────

def mostrar_categorias(servicio: Restaurante) -> None:
    categorias: set[str] = servicio.obtener_categorias_unicas()
    if not categorias:
        print("  No hay categorias registradas.")
        return

    print("\n--- Categorías disponibles ---")
    for categoria in sorted(categorias):
        print(f"  - {categoria}")


# ─────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────

def principal() -> None:
    # Crear los servicios
    archivo_servicio = ArchivoServicio(RUTA_PRODUCTOS, RUTA_USUARIOS, RUTA_VENTAS)
    servicio = Restaurante()

    # Cargar datos desde los archivos JSON al iniciar la aplicación
    print("\n  Cargando datos desde archivos JSON...")

    productos_cargados: list[Producto] = archivo_servicio.cargar_productos()
    servicio.cargar_productos_iniciales(productos_cargados)
    print(f"  Se cargaron {len(productos_cargados)} producto(s).")

    usuarios_cargados: list[Usuario] = archivo_servicio.cargar_usuarios()
    servicio.cargar_usuarios_iniciales(usuarios_cargados)
    print(f"  Se cargaron {len(usuarios_cargados)} usuario(s).")

    ventas_cargadas: list[Venta] = archivo_servicio.cargar_ventas()
    servicio.cargar_ventas_iniciales(ventas_cargadas)
    print(f"  Se cargaron {len(ventas_cargadas)} venta(s).")

    menu: dict[str, str] = servicio.obtener_menu_diccionario()

    while True:
        mostrar_menu()
        opcion: str = input("Seleccione una opcion: ").strip()

        if opcion == "12":
            print("\n  Gracias por usar el sistema. Hasta luego.")
            sys.exit(0)

        accion: str | None = menu.get(opcion)
        if accion == "registrar_producto":
            registrar_producto(servicio, archivo_servicio)
        elif accion == "buscar_producto":
            buscar_producto(servicio)
        elif accion == "actualizar_producto":
            actualizar_producto(servicio, archivo_servicio)
        elif accion == "eliminar_producto":
            eliminar_producto(servicio, archivo_servicio)
        elif accion == "listar_productos":
            listar_productos(servicio)
        elif accion == "registrar_usuario":
            registrar_usuario(servicio, archivo_servicio)
        elif accion == "listar_usuarios":
            listar_usuarios(servicio)
        elif accion == "vender_producto":
            vender_producto(servicio, archivo_servicio)
        elif accion == "consultar_ventas_usuario":
            consultar_ventas_usuario(servicio)
        elif accion == "listar_ventas":
            listar_ventas(servicio)
        elif accion == "mostrar_categorias":
            mostrar_categorias(servicio)
        else:
            print("  [!] Opcion no valida. Seleccione una opcion del 1 al 12.")


if __name__ == "__main__":
    principal()
