# Sistema de Gestión de Restaurante

**Estudiante:** Dayana Reyes

## Descripción del Sistema
Este es un sistema básico de gestión de restaurante desarrollado en Python aplicando Programación Orientada a Objetos (POO). El sistema permite registrar productos del menú y clientes, así como visualizarlos de forma organizada.

## Estructura del Proyecto
El proyecto está dividido de forma modular en las siguientes carpetas:
- `modelos/producto.py`: Contiene la clase `Producto`, responsable de representar un ítem del restaurante.
- `modelos/cliente.py`: Contiene la clase `Cliente`, responsable de representar a las personas que son clientes del lugar.
- `servicios/restaurante.py`: Contiene la clase `Restaurante`, que administra las listas de productos y clientes.
- `main.py`: Punto de entrada que inicializa las instancias y ejecuta el programa.

## Tipos de datos utilizados
Para reflejar de forma correcta la naturaleza de los atributos, se han utilizado los siguientes tipos de datos básicos:
- `str` (texto): Para nombres, categorías y números de teléfono.
- `int` (enteros): Para edades de los clientes.
- `float` (decimales): Para el precio de los productos.
- `bool` (booleanos o lógicos): Para estados lógicos (si un producto está disponible `True`/`False` o si un cliente es VIP `True`/`False`).

Adicionalmente, se utilizan **listas** en la clase `Restaurante` para poder almacenar y gestionar múltiples instancias de objetos `Producto` y `Cliente`.

## Reflexión
El uso de identificadores descriptivos (nombres claros para variables, clases y métodos en estilo *snake_case* o *PascalCase*) hace que el código sea autodocumentado, limpio y fácil de leer para otros desarrolladores. Seleccionar los tipos de datos adecuados es fundamental para asegurar que la información tenga sentido, como operar matemáticamente con el precio o utilizar condicionales basados en booleanos. Finalmente, las listas nos permiten administrar conjuntos de objetos dinámicos sin tener que crear múltiples variables estáticas, facilitando la escalabilidad del sistema y promoviendo la creación de proyectos modulares más ordenados.
