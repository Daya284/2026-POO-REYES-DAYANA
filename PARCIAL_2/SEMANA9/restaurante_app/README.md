# Semana 9 - Estructuras de datos aplicadas al proyecto restaurante_app

## Estudiante

Dayana Kristel Reyes Feijoo

## Descripción del sistema

Este proyecto continúa la evolución del sistema de restaurante desarrollado durante semanas anteriores. En esta entrega se aplica el uso de estructuras de datos de Python para administrar de forma organizada la información de productos y usuarios, manteniendo la arquitectura modular con modelos, servicios y punto de entrada principal.

## Estructura del proyecto

restaurante_app/
├── modelos/
│ ├── **init**.py
│ ├── producto.py
│ └── usuario.py
├── servicios/
│ ├── **init**.py
│ └── restaurante.py
├── main.py
└── README.md

## Responsabilidad de cada archivo

- modelos/producto.py: define la clase Producto con codigo, nombre, categoria y precio.
- modelos/usuario.py: define la clase Usuario con identificacion, nombre y correo.
- servicios/restaurante.py: administra las colecciones del sistema, las validaciones y las operaciones de búsqueda, actualización, eliminación y listado.
- main.py: controla la interacción con el usuario mediante consola y comunica las acciones con el servicio.

## Uso de las estructuras de datos

### Lista (list)

Se usa una lista para almacenar la colección dinámica de productos y usuarios dentro de la clase Restaurante. Esto permite registrar, buscar, actualizar y eliminar elementos sin perder el orden de inserción.

### Tupla (tuple)

Se usa una tupla para mantener fijo el texto del menú principal del sistema. La información es estable durante la ejecución y no debe modificarse en tiempo de ejecución.

### Diccionario (dict)

Se usa un diccionario para relacionar cada opción del menú con la acción correspondiente del programa. Esto facilita la selección de funciones y mantiene el código más ordenado.

### Conjunto (set)

Se usa un conjunto para obtener las categorías únicas de los productos registrados, evitando duplicados y facilitando la visualización de valores distintos.

## Funcionalidades principales

- Registrar productos con validación de codigo duplicado.
- Buscar productos por codigo.
- Actualizar datos de un producto existente.
- Eliminar productos.
- Listar productos registrados.
- Registrar usuarios con validación de identificacion duplicada.
- Listar usuarios registrados.
- Mostrar categorías únicas disponibles.

## Ejecución del programa

1. Ubíquese en la carpeta del proyecto.
2. Ejecute el archivo principal:

python main.py

## Reflexión

La elección de la estructura de datos adecuada depende de la necesidad del problema. Las listas permiten colecciones dinámicas, las tuplas sirven para datos estáticos, los diccionarios optimizan la relación clave-valor y los conjuntos evitan duplicados. Usar cada una correctamente mejora la claridad, la eficiencia y la organización del software.
