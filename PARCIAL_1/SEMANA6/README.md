# Sistema de Restaurante - POO en Python

**Estudiante:** Dayana Reyes

## Descripción del Sistema
Este proyecto es una aplicación modular en Python que representa los productos disponibles en un restaurante. La finalidad del sistema es administrar el menú del restaurante aplicando los principios fundamentales de la Programación Orientada a Objetos: herencia, encapsulación y polimorfismo. El sistema permite registrar comidas y bebidas, así como consultar la información detallada de cada producto.

## Estructura del Proyecto
El proyecto está organizado respetando una arquitectura modular para separar lógicamente sus componentes:
- `restaurante_app/modelos/`: Contiene las clases que representan las entidades del negocio: `Producto` (clase padre), `Platillo` y `Bebida` (clases hijas).
- `restaurante_app/servicios/`: Contiene la lógica de administración a través de la clase `Restaurante`, encargada de almacenar y gestionar los productos.
- `restaurante_app/main.py`: Es el punto de arranque de la aplicación donde se instancian los objetos, se agregan al restaurante y se muestran los resultados en la consola.

## Principios POO Aplicados

1. **Herencia:** Se implementó una relación lógica donde `Platillo` y `Bebida` son clases hijas que heredan de la clase base `Producto`. Esto permite reutilizar los atributos comunes (`nombre`, `precio`, `disponibilidad`) y agregar atributos específicos (`calorias` para platillos y `volumen_ml` para bebidas). Se utilizó `super().__init__()` en las clases hijas para inicializar la parte correspondiente a la clase padre.

2. **Encapsulación:** Se protegió el atributo `precio` de la clase `Producto` definiéndolo como privado (`__precio`). Su acceso y modificación están estrictamente controlados mediante los métodos `obtener_precio()` y `cambiar_precio()`. El método de modificación incluye una validación lógica que impide establecer un precio negativo o igual a cero, protegiendo así la integridad de los datos.

3. **Polimorfismo:** El método `mostrar_informacion()` fue definido en la clase padre y sobrescrito en ambas clases hijas para mostrar información detallada según el tipo de producto. Al recorrer la lista general de productos en la clase `Restaurante` (`mostrar_menu()`) y ejecutar este método, se evidencia el polimorfismo ya que el mismo llamado genera un comportamiento distinto dependiendo de si el objeto iterado es un Platillo o una Bebida.

## Reflexión
La aplicación de los principios de la Programación Orientada a Objetos en proyectos modulares de Python es fundamental para desarrollar software estructurado, reutilizable y fácil de mantener. La herencia evita la duplicidad de código; la encapsulación garantiza que los datos internos permanezcan seguros y consistentes, impidiendo su alteración desde fuera sin el uso de métodos controlados; y el polimorfismo dota al sistema de flexibilidad, permitiendo tratar distintas clases hijas a través de una interfaz común. Esto hace que el diseño del software sea robusto y escalable ante futuras ampliaciones.
