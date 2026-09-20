import json
import os


class ArchivoServicio:
    """
    Servicio encargado de leer y escribir datos en archivos JSON.
    Centraliza las operaciones de lectura y escritura para que ninguna vista
    acceda directamente a los datos en disco.

    Semana 14: se incorpora el método escribir_json para permitir
    la persistencia de las operaciones realizadas sobre productos.
    """

    @staticmethod
    def leer_json(ruta_archivo):
        """
        Lee un archivo JSON y retorna su contenido como una lista de diccionarios.
        Si el archivo no existe o contiene un formato inválido, retorna una lista vacía.
        """
        if not os.path.exists(ruta_archivo):
            print(f"Advertencia: El archivo '{ruta_archivo}' no fue encontrado.")
            return []

        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        except json.JSONDecodeError:
            print(f"Error: El archivo '{ruta_archivo}' no tiene un formato JSON válido.")
            return []
        except Exception as e:
            print(f"Error inesperado al leer '{ruta_archivo}': {e}")
            return []

    @staticmethod
    def escribir_json(ruta_archivo, datos):
        """
        Escribe una lista de diccionarios en un archivo JSON.
        Crea el directorio si no existe. Retorna True si la operación
        fue exitosa, False en caso contrario.

        Args:
            ruta_archivo: Ruta completa del archivo JSON a escribir.
            datos: Lista de diccionarios a guardar.

        Returns:
            True si se guardó correctamente, False en caso de error.
        """
        try:
            directorio = os.path.dirname(ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al escribir en '{ruta_archivo}': {e}")
            return False
