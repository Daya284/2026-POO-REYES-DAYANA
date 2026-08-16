import sys

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


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
    print("8. Mostrar categorías")
    print("9. Salir")
    print("========================================")


def registrar_producto(servicio: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    codigo = input("  Codigo    : ")
    nombre = input("  Nombre    : ")
    categoria = input("  Categoria : ")
    precio_texto = input("  Precio    : ")

    try:
        precio = float(precio_texto)
        producto = Producto(codigo, nombre, categoria, precio)
        if servicio.registrar_producto(producto):
            print("  [OK] Producto registrado correctamente.")
        else:
            print(f"  [!] Ya existe un producto con el codigo '{codigo}'.")
    except ValueError as error:
        print(f"  [ERROR] {error}")


def buscar_producto(servicio: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = input("  Codigo : ")
    producto = servicio.buscar_producto(codigo)
    if producto is None:
        print("  [!] No se encontró un producto con ese código.")
        return
    print("\n" + producto.mostrar_informacion())


def actualizar_producto(servicio: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    codigo = input("  Codigo actual : ")
    producto = servicio.buscar_producto(codigo)
    if producto is None:
        print("  [!] No se encontró el producto a actualizar.")
        return

    print("Deje en blanco los campos que no desea modificar.")
    nombre = input(f"  Nuevo nombre [{producto.nombre}] : ") or None
    categoria = input(f"  Nueva categoria [{producto.categoria}] : ") or None
    precio_texto = input(f"  Nuevo precio [{producto.precio}] : ")
    precio = float(precio_texto) if precio_texto.strip() else None

    try:
        actualizado = servicio.actualizar_producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
        )
        if actualizado:
            print("  [OK] Producto actualizado correctamente.")
        else:
            print("  [!] No fue posible actualizar el producto.")
    except ValueError as error:
        print(f"  [ERROR] {error}")


def eliminar_producto(servicio: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    codigo = input("  Codigo : ")
    if servicio.eliminar_producto(codigo):
        print("  [OK] Producto eliminado correctamente.")
    else:
        print("  [!] No se encontró un producto con ese código.")


def listar_productos(servicio: Restaurante) -> None:
    productos = servicio.listar_productos()
    if not productos:
        print("  No hay productos registrados en el restaurante.")
        return

    print("\n+======================================+")
    print("|       PRODUCTOS REGISTRADOS          |")
    print("+======================================+")
    for indice, producto in enumerate(productos, start=1):
        print(f"\n  -- {indice}. --")
        print(producto.mostrar_informacion())


def registrar_usuario(servicio: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = input("  Identificacion : ")
    nombre = input("  Nombre         : ")
    correo = input("  Correo         : ")

    try:
        usuario = Usuario(identificacion, nombre, correo)
        if servicio.registrar_usuario(usuario):
            print("  [OK] Usuario registrado correctamente.")
        else:
            print(f"  [!] Ya existe un usuario con la identificacion '{identificacion}'.")
    except ValueError as error:
        print(f"  [ERROR] {error}")


def listar_usuarios(servicio: Restaurante) -> None:
    usuarios = servicio.listar_usuarios()
    if not usuarios:
        print("  No hay usuarios registrados en el sistema.")
        return

    print("\n+======================================+")
    print("|         USUARIOS REGISTRADOS         |")
    print("+======================================+")
    for indice, usuario in enumerate(usuarios, start=1):
        print(f"\n  -- {indice}. --")
        print(usuario.mostrar_informacion())


def mostrar_categorias(servicio: Restaurante) -> None:
    categorias = servicio.obtener_categorias_unicas()
    if not categorias:
        print("  No hay categorias registradas.")
        return

    print("\n--- Categorías disponibles ---")
    for categoria in sorted(categorias):
        print(f"  - {categoria}")


def principal() -> None:
    servicio = Restaurante()
    menu = servicio.obtener_menu_diccionario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "9":
            print("\n  Gracias por usar el sistema. Hasta luego.")
            sys.exit(0)

        accion = menu.get(opcion)
        if accion == "registrar_producto":
            registrar_producto(servicio)
        elif accion == "buscar_producto":
            buscar_producto(servicio)
        elif accion == "actualizar_producto":
            actualizar_producto(servicio)
        elif accion == "eliminar_producto":
            eliminar_producto(servicio)
        elif accion == "listar_productos":
            listar_productos(servicio)
        elif accion == "registrar_usuario":
            registrar_usuario(servicio)
        elif accion == "listar_usuarios":
            listar_usuarios(servicio)
        elif accion == "mostrar_categorias":
            mostrar_categorias(servicio)
        else:
            print("  [!] Opcion no valida. Seleccione una opcion del 1 al 9.")


if __name__ == "__main__":
    principal()
