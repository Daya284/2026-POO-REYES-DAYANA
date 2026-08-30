import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """Servicio encargado de cargar y guardar productos, usuarios y ventas mediante archivos JSON."""

    def __init__(self, ruta_productos: str, ruta_usuarios: str, ruta_ventas: str) -> None:
        self._ruta_productos: str = ruta_productos
        self._ruta_usuarios: str = ruta_usuarios
        self._ruta_ventas: str = ruta_ventas

    # ─────────────────────────────────────────────
    #  PRODUCTOS
    # ─────────────────────────────────────────────

    def cargar_productos(self) -> list[Producto]:
        """Lee datos/productos.json y reconstruye una lista de objetos Producto.

        Controla las excepciones:
        - FileNotFoundError: si el archivo aún no existe, retorna lista vacía.
        - json.JSONDecodeError: si el contenido no es JSON válido.
        - PermissionError: si no hay permisos de lectura.
        - KeyError: si un registro no contiene las claves esperadas.
        - ValueError: si los datos de un registro no pasan las validaciones de Producto.
        """
        productos: list[Producto] = []

        try:
            with open(self._ruta_productos, "r", encoding="utf-8") as archivo:
                datos: list[dict] = json.load(archivo)
        except FileNotFoundError:
            print("  [INFO] El archivo de productos no existe todavia. Se inicia con una coleccion vacia.")
            return productos
        except json.JSONDecodeError:
            print("  [ERROR] El archivo de productos no contiene un formato JSON valido. Se inicia con una coleccion vacia.")
            return productos
        except PermissionError:
            print("  [ERROR] No se tienen permisos suficientes para leer el archivo de productos.")
            return productos

        if not isinstance(datos, list):
            print("  [ERROR] La estructura del archivo JSON de productos no es una lista. Se inicia con una coleccion vacia.")
            return productos

        for indice, registro in enumerate(datos):
            try:
                codigo: str = registro["codigo"]
                nombre: str = registro["nombre"]
                categoria: str = registro["categoria"]
                precio: float = registro["precio"]
                stock: int = registro.get("stock", 0)

                producto = Producto(codigo, nombre, categoria, precio, stock)
                productos.append(producto)
            except KeyError as error:
                print(f"  [ADVERTENCIA] Producto registro {indice + 1}: falta la clave {error}. Se omitio este registro.")
            except ValueError as error:
                print(f"  [ADVERTENCIA] Producto registro {indice + 1}: {error}. Se omitio este registro.")

        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        """Convierte la lista de objetos Producto a diccionarios y guarda en JSON.

        Controla las excepciones:
        - PermissionError: si no hay permisos de escritura.
        """
        lista_diccionarios: list[dict] = []
        for producto in productos:
            lista_diccionarios.append(producto.a_diccionario())

        try:
            directorio: str = os.path.dirname(self._ruta_productos)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            with open(self._ruta_productos, "w", encoding="utf-8") as archivo:
                json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("  [ERROR] No se tienen permisos suficientes para escribir el archivo de productos.")
            return False

    # ─────────────────────────────────────────────
    #  USUARIOS
    # ─────────────────────────────────────────────

    def cargar_usuarios(self) -> list[Usuario]:
        """Lee datos/usuarios.json y reconstruye una lista de objetos Usuario.

        Controla las excepciones:
        - FileNotFoundError: si el archivo aún no existe, retorna lista vacía.
        - json.JSONDecodeError: si el contenido no es JSON válido.
        - PermissionError: si no hay permisos de lectura.
        - KeyError: si un registro no contiene las claves esperadas.
        - ValueError: si los datos de un registro no pasan las validaciones de Usuario.
        """
        usuarios: list[Usuario] = []

        try:
            with open(self._ruta_usuarios, "r", encoding="utf-8") as archivo:
                datos: list[dict] = json.load(archivo)
        except FileNotFoundError:
            print("  [INFO] El archivo de usuarios no existe todavia. Se inicia con una coleccion vacia.")
            return usuarios
        except json.JSONDecodeError:
            print("  [ERROR] El archivo de usuarios no contiene un formato JSON valido. Se inicia con una coleccion vacia.")
            return usuarios
        except PermissionError:
            print("  [ERROR] No se tienen permisos suficientes para leer el archivo de usuarios.")
            return usuarios

        if not isinstance(datos, list):
            print("  [ERROR] La estructura del archivo JSON de usuarios no es una lista. Se inicia con una coleccion vacia.")
            return usuarios

        for indice, registro in enumerate(datos):
            try:
                identificacion: str = registro["identificacion"]
                nombre: str = registro["nombre"]
                correo: str = registro["correo"]

                usuario = Usuario(identificacion, nombre, correo)
                usuarios.append(usuario)
            except KeyError as error:
                print(f"  [ADVERTENCIA] Usuario registro {indice + 1}: falta la clave {error}. Se omitio este registro.")
            except ValueError as error:
                print(f"  [ADVERTENCIA] Usuario registro {indice + 1}: {error}. Se omitio este registro.")

        return usuarios

    def guardar_usuarios(self, usuarios: list[Usuario]) -> bool:
        """Convierte la lista de objetos Usuario a diccionarios y guarda en JSON.

        Controla las excepciones:
        - PermissionError: si no hay permisos de escritura.
        """
        lista_diccionarios: list[dict] = []
        for usuario in usuarios:
            lista_diccionarios.append(usuario.a_diccionario())

        try:
            directorio: str = os.path.dirname(self._ruta_usuarios)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            with open(self._ruta_usuarios, "w", encoding="utf-8") as archivo:
                json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("  [ERROR] No se tienen permisos suficientes para escribir el archivo de usuarios.")
            return False

    # ─────────────────────────────────────────────
    #  VENTAS
    # ─────────────────────────────────────────────

    def cargar_ventas(self) -> list[Venta]:
        """Lee datos/ventas.json y reconstruye una lista de objetos Venta.

        Controla las excepciones:
        - FileNotFoundError: si el archivo aún no existe, retorna lista vacía.
        - json.JSONDecodeError: si el contenido no es JSON válido.
        - PermissionError: si no hay permisos de lectura.
        - KeyError: si un registro no contiene las claves esperadas.
        - ValueError: si los datos de un registro no pasan las validaciones de Venta.
        """
        ventas: list[Venta] = []

        try:
            with open(self._ruta_ventas, "r", encoding="utf-8") as archivo:
                datos: list[dict] = json.load(archivo)
        except FileNotFoundError:
            print("  [INFO] El archivo de ventas no existe todavia. Se inicia con una coleccion vacia.")
            return ventas
        except json.JSONDecodeError:
            print("  [ERROR] El archivo de ventas no contiene un formato JSON valido. Se inicia con una coleccion vacia.")
            return ventas
        except PermissionError:
            print("  [ERROR] No se tienen permisos suficientes para leer el archivo de ventas.")
            return ventas

        if not isinstance(datos, list):
            print("  [ERROR] La estructura del archivo JSON de ventas no es una lista. Se inicia con una coleccion vacia.")
            return ventas

        for indice, registro in enumerate(datos):
            try:
                usuario_id: str = registro["usuario_id"]
                producto_codigo: str = registro["producto_codigo"]
                cantidad: int = registro["cantidad"]

                venta = Venta(usuario_id, producto_codigo, cantidad)
                ventas.append(venta)
            except KeyError as error:
                print(f"  [ADVERTENCIA] Venta registro {indice + 1}: falta la clave {error}. Se omitio este registro.")
            except ValueError as error:
                print(f"  [ADVERTENCIA] Venta registro {indice + 1}: {error}. Se omitio este registro.")

        return ventas

    def guardar_ventas(self, ventas: list[Venta]) -> bool:
        """Convierte la lista de objetos Venta a diccionarios y guarda en JSON.

        Controla las excepciones:
        - PermissionError: si no hay permisos de escritura.
        """
        lista_diccionarios: list[dict] = []
        for venta in ventas:
            lista_diccionarios.append(venta.a_diccionario())

        try:
            directorio: str = os.path.dirname(self._ruta_ventas)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            with open(self._ruta_ventas, "w", encoding="utf-8") as archivo:
                json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("  [ERROR] No se tienen permisos suficientes para escribir el archivo de ventas.")
            return False
