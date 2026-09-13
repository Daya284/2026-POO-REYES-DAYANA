import json
import os


class ArchivoServicio:
    """
    Servicio encargado de leer los datos locales almacenados en archivos JSON.
    Centraliza la lectura de archivos para que ninguna vista acceda directamente
    a los datos en disco.
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
