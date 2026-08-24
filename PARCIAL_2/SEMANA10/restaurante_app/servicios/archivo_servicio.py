import json
import os

from modelos.producto import Producto


class ArchivoServicio:
    """Servicio encargado de cargar y guardar productos mediante un archivo JSON."""

    def __init__(self, ruta_archivo: str) -> None:
        self._ruta_archivo: str = ruta_archivo

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
            with open(self._ruta_archivo, "r", encoding="utf-8") as archivo:
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
            print("  [ERROR] La estructura del archivo JSON no es una lista. Se inicia con una coleccion vacia.")
            return productos

        for indice, registro in enumerate(datos):
            try:
                codigo: str = registro["codigo"]
                nombre: str = registro["nombre"]
                categoria: str = registro["categoria"]
                precio: float = registro["precio"]

                producto = Producto(codigo, nombre, categoria, precio)
                productos.append(producto)
            except KeyError as error:
                print(f"  [ADVERTENCIA] Registro {indice + 1}: falta la clave {error}. Se omitio este registro.")
            except ValueError as error:
                print(f"  [ADVERTENCIA] Registro {indice + 1}: {error}. Se omitio este registro.")

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
            directorio: str = os.path.dirname(self._ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            with open(self._ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("  [ERROR] No se tienen permisos suficientes para escribir el archivo de productos.")
            return False
