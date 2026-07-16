# Restaurante App - Semana 7

**Estudiante:** Dayana Reyes

## Descripción del Sistema
Este proyecto es una aplicación modular en Python que simula la gestión básica de un restaurante. Permite registrar, listar y buscar productos y clientes mediante un menú interactivo en consola, cumpliendo con los requisitos de la Semana 7 de la asignatura Programación Orientada a Objetos.

## Estructura del Proyecto
El proyecto está organizado en una arquitectura por capas para separar las responsabilidades:
- `restaurante_app/modelos/`: Contiene las clases que representan las entidades del sistema (`Producto` y `Cliente`).
- `restaurante_app/servicios/`: Contiene la clase de servicio encargada de la lógica de negocio y administración de las entidades (`Restaurante`).
- `restaurante_app/main.py`: Punto de entrada de la aplicación que maneja la interacción con el usuario mediante un menú en consola.

## Conceptos Aplicados

### Constructores, `@property` y `@setter`
En la clase `Producto`, se utiliza el constructor tradicional `__init__` para inicializar los atributos. Además, se aplican los decoradores `@property` para permitir el acceso controlado a los datos y `@setter` para realizar validaciones. Por ejemplo, asegura que los nombres no estén vacíos y que el precio del producto sea mayor a cero, arrojando excepciones descriptivas si los datos son inválidos.

### `@dataclass`
En la clase `Cliente`, se utiliza el decorador `@dataclass`. Esta característica permite simplificar la creación de la clase y la definición de sus atributos (`id_cliente`, `nombre`, `correo`). Genera implícitamente métodos especiales como `__init__` y `__repr__`, resultando en un código más limpio y fácil de mantener para objetos destinados principalmente a almacenar datos.

### Menú Interactivo y Creación Dinámica de Objetos
Los objetos (productos y clientes) no se encuentran "quemados" (hardcoded) en el código del sistema. El programa requiere que el usuario ingrese la información mediante la consola utilizando la función `input()`. Estos datos son recolectados y enviados a los constructores correspondientes para crear las instancias de los objetos dinámicamente, para finalmente ser almacenados en las listas de la clase de servicio `Restaurante`.

## Reflexión
La creación de objetos a partir de datos ingresados por el usuario es un paso fundamental en el desarrollo de software aplicando la Programación Orientada a Objetos. Esto dota de flexibilidad y utilidad a las aplicaciones, permitiendo que el sistema procese y almacene información variable de forma dinámica, respondiendo a las necesidades reales sin requerir modificaciones en el código fuente por cada nuevo registro.
