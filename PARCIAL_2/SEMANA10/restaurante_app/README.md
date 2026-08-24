# Restaurante App - Semana 10

**Estudiante:** Dayana Reyes  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 10 — Persistencia de datos con JSON

---

## Descripción del sistema

Sistema de administración básica de un restaurante que permite gestionar productos y usuarios mediante un menú interactivo por consola. Esta versión incorpora **persistencia de productos** mediante un archivo JSON, permitiendo que los datos se conserven entre ejecuciones del programa.

---

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   └── productos.json          # Archivo de persistencia de productos
├── modelos/
│   ├── __init__.py
│   ├── producto.py              # Clase Producto con validaciones y conversión a diccionario
│   └── usuario.py               # Clase Usuario (permanece en memoria)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py      # Servicio de lectura y escritura de JSON
│   └── restaurante.py           # Servicio de administración de productos y usuarios
├── main.py                      # Punto de entrada y coordinación del menú
└── README.md                    # Documentación del proyecto
```

---

## Responsabilidad de cada componente

| Archivo | Responsabilidad |
|---------|----------------|
| `modelos/producto.py` | Define la clase `Producto` con validaciones mediante propiedades y el método `a_diccionario()` para convertir el objeto a un formato compatible con JSON. |
| `modelos/usuario.py` | Define la clase `Usuario` con validaciones. Su información permanece en memoria durante esta semana. |
| `servicios/restaurante.py` | Administra las colecciones de productos y usuarios. Ofrece operaciones de registrar, buscar, actualizar, eliminar y listar. Incluye el método `cargar_productos_iniciales()` para recibir los productos recuperados desde JSON. |
| `servicios/archivo_servicio.py` | Centraliza la lectura (`cargar_productos`) y escritura (`guardar_productos`) del archivo `datos/productos.json` utilizando `json.load()` y `json.dump()` con `with open()` y codificación UTF-8. |
| `main.py` | Crea los servicios, carga los productos almacenados al iniciar, coordina el menú interactivo y solicita el guardado tras cada operación que modifique la colección de productos. |

---

## Funcionamiento de productos.json

El archivo `datos/productos.json` almacena la colección de productos como una **lista de diccionarios**. Cada diccionario contiene las claves: `codigo`, `nombre`, `categoria` y `precio`.

Ejemplo del contenido del archivo:

```json
[
    {
        "codigo": "P001",
        "nombre": "Hamburguesa Clasica",
        "categoria": "Comida",
        "precio": 5.50
    },
    {
        "codigo": "P002",
        "nombre": "Jugo de Naranja",
        "categoria": "Bebidas",
        "precio": 2.00
    }
]
```

---

## Flujo de carga (al iniciar la aplicación)

1. `main.py` crea una instancia de `ArchivoServicio` con la ruta a `datos/productos.json`.
2. Se invoca `cargar_productos()` que intenta leer el archivo.
3. `json.load()` recupera la información almacenada.
4. Se valida que la estructura sea una lista.
5. Cada registro válido se convierte en un objeto `Producto(...)`.
6. Los objetos se entregan al servicio `Restaurante` mediante `cargar_productos_iniciales()`.
7. El menú trabaja normalmente con objetos `Producto`.

## Flujo de guardado (después de modificar productos)

1. El usuario registra, actualiza o elimina un producto mediante el menú.
2. `main.py` solicita la operación al servicio `Restaurante`.
3. `Restaurante` modifica la colección en memoria.
4. Los objetos `Producto` se convierten a diccionarios usando `a_diccionario()`.
5. `ArchivoServicio` utiliza `json.dump()` para escribir el archivo.
6. Se actualiza `datos/productos.json` con el estado actual.

---

## Excepciones controladas

| Excepción | Contexto de uso |
|-----------|----------------|
| `FileNotFoundError` | Si `productos.json` no existe todavía, el programa inicia con una colección vacía sin detenerse. |
| `json.JSONDecodeError` | Si el archivo existe pero su contenido no es JSON válido, se informa al usuario y se inicia con una colección vacía. |
| `PermissionError` | Si no hay permisos de lectura o escritura sobre el archivo, se notifica al usuario de forma controlada. |
| `KeyError` | Si un registro almacenado no contiene alguna de las claves esperadas (`codigo`, `nombre`, `categoria`, `precio`), se omite ese registro. |
| `ValueError` | Se mantiene para las validaciones de `Producto` (campos vacíos, precio no positivo) y para controlar datos inválidos sin detener el programa. |

---

## Instrucciones para ejecutar el programa

1. Abrir una terminal en la carpeta `restaurante_app/`.
2. Ejecutar el programa:

```bash
python main.py
```

3. Utilizar el menú numérico para interactuar con el sistema.

---

## Comprobación de persistencia

Para verificar que la persistencia funciona correctamente:

1. **Ejecutar** `main.py`.
2. **Registrar** uno o más productos mediante la opción 1 del menú.
3. **Verificar** que `datos/productos.json` contenga la información registrada.
4. **Cerrar** completamente el programa (opción 9).
5. **Ejecutar nuevamente** `main.py`.
6. **Listar** los productos (opción 5) y confirmar que los productos anteriores fueron recuperados.
7. **Actualizar o eliminar** un producto (opciones 3 o 4).
8. **Reiniciar** nuevamente y comprobar que el cambio también se conservó.

---

## Mejoras incorporadas en la Semana 10

- Incorporación de la carpeta `datos/` con el archivo `productos.json`.
- Creación del servicio `ArchivoServicio` para centralizar la persistencia.
- Método `a_diccionario()` en la clase `Producto` para serialización JSON.
- Método `cargar_productos_iniciales()` en el servicio `Restaurante`.
- Carga automática de productos al iniciar la aplicación.
- Guardado automático después de registrar, actualizar o eliminar productos.
- Manejo de excepciones específicas: `FileNotFoundError`, `json.JSONDecodeError`, `PermissionError`, `KeyError` y `ValueError`.
- Uso de `with open()` con `encoding="utf-8"` para lectura y escritura segura.
